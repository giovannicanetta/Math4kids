"""Shared colours, fonts and reusable mobjects for the powers-and-logs videos."""

from manim import (
    BLACK,
    DOWN,
    LEFT,
    ORIGIN,
    RIGHT,
    UP,
    Circle,
    Dot,
    FadeIn,
    Line,
    FadeOut,
    MathTex,
    Polygon,
    RoundedRectangle,
    Tex,
    Text,
    VGroup,
    Write,
    config,
)
import numpy as np

BACKGROUND = "#10131f"
CANDY_PINK = "#ff5d8f"
CANDY_WRAP = "#ffd166"
BOX_BODY = "#2d3561"
BOX_EDGE = "#8fd3ff"
BUTTON_IDLE = "#ef476f"
BUTTON_HOT = "#ffd166"
ACCENT = "#8fd3ff"
GOOD = "#06d6a0"
SOFT = "#c8cfe8"

TITLE_KW = {"color": ACCENT, "weight": "BOLD"}


def setup_style() -> None:
    """Apply the shared look. Call once at the top of every scene's construct."""
    config.background_color = BACKGROUND


def title(text: str, size: float = 42) -> Text:
    return Text(text, font_size=size, **TITLE_KW)


def body(text: str, size: float = 30, color: str = SOFT) -> Text:
    return Text(text, font_size=size, color=color)


def candy(scale: float = 1.0) -> VGroup:
    """A wrapped sweet: a round body with two twisted ends."""
    core = Circle(radius=0.16, color=CANDY_PINK, fill_color=CANDY_PINK, fill_opacity=1, stroke_width=2)
    left = Polygon(
        [-0.16, 0.0, 0.0], [-0.30, 0.11, 0.0], [-0.30, -0.11, 0.0],
        color=CANDY_WRAP, fill_color=CANDY_WRAP, fill_opacity=1, stroke_width=1,
    )
    right = left.copy().rotate(np.pi, about_point=ORIGIN)
    return VGroup(core, left, right).scale(scale)


def candy_positions(n: int, columns: int, spacing: float) -> list:
    """Centred grid positions for ``n`` candies."""
    rows = int(np.ceil(n / columns))
    points = []
    for index in range(n):
        row, col = divmod(index, columns)
        in_row = min(columns, n - row * columns)
        x = (col - (in_row - 1) / 2) * spacing
        y = ((rows - 1) / 2 - row) * spacing
        points.append(np.array([x, y, 0.0]))
    return points


def fit_in_frame(mobject, margin: float = 0.6):
    """Shrink a mobject until it sits comfortably inside the camera frame."""
    max_width = config.frame_width - 2 * margin
    max_height = config.frame_height - 2 * margin
    factor = min(max_width / mobject.width, max_height / mobject.height, 1.0)
    return mobject.scale(factor)


class DoublingBox(VGroup):
    """The magic box: press the button and the candies inside double."""

    def __init__(self, width: float = 5.2, height: float = 3.4, start: int = 1):
        super().__init__()
        self.shell = RoundedRectangle(
            width=width, height=height, corner_radius=0.3,
            color=BOX_EDGE, fill_color=BOX_BODY, fill_opacity=1, stroke_width=5,
        )
        self.name = Text("DOUBLING BOX", font_size=20, color=ACCENT, weight="BOLD")
        self.name.next_to(self.shell.get_top(), DOWN, buff=0.18)
        self.button = Circle(
            radius=0.28, color=BUTTON_HOT,
            fill_color=BUTTON_IDLE, fill_opacity=1, stroke_width=4,
        )
        self.button.next_to(self.shell, DOWN, buff=0.35)
        self.button_label = Text("PRESS", font_size=20, color=SOFT)
        self.button_label.next_to(self.button, DOWN, buff=0.15)

        self.candies = VGroup(*[candy() for _ in range(start)])
        self._layout()

        self.add(self.shell, self.name, self.button, self.button_label, self.candies)

    @property
    def tray_center(self) -> np.ndarray:
        return self.shell.get_center() + DOWN * 0.25

    def _grid(self, count: int):
        """Columns, spacing and candy scale that keep ``count`` candies inside the box."""
        if count <= 2:
            return max(1, count), 0.85, 1.0
        if count <= 8:
            return 4, 0.80, 0.95
        if count <= 16:
            return 8, 0.62, 0.75
        return 8, 0.58, 0.62

    def _place(self, mobjects) -> list:
        count = len(mobjects)
        columns, spacing, scale = self._grid(count)
        spacing = min(spacing, (self.shell.width - 0.5) / columns)
        base_width = candy().width * min(1.0, spacing / 0.8)
        placed = []
        for item, point in zip(mobjects, candy_positions(count, columns, spacing)):
            target = item.copy()
            target.scale_to_fit_width(base_width * scale)
            target.set_opacity(1)
            target.move_to(self.tray_center + point)
            placed.append(target)
        return placed

    def _layout(self) -> None:
        for item, target in zip(self.candies, self._place(self.candies)):
            item.become(target)

    def press(self, scene, run_time: float = 0.9) -> None:
        """Animate one button press: the candies inside double."""
        clones = VGroup(*[c.copy() for c in self.candies])
        scene.play(
            self.button.animate.set_fill(BUTTON_HOT).scale(0.85),
            run_time=0.18,
        )
        scene.play(
            self.button.animate.set_fill(BUTTON_IDLE).scale(1 / 0.85),
            FadeIn(clones, scale=0.4),
            run_time=0.32,
        )
        scene.remove(clones)
        self.candies.add(*clones)
        targets = self._place(self.candies)
        scene.play(
            *[item.animate.become(target) for item, target in zip(self.candies, targets)],
            run_time=run_time,
        )

    def reset(self, scene, count: int = 1) -> None:
        scene.play(FadeOut(self.candies), run_time=0.3)
        self.remove(self.candies)
        self.candies = VGroup(*[candy() for _ in range(count)])
        self._layout()
        self.add(self.candies)
        scene.play(FadeIn(self.candies, scale=0.5), run_time=0.4)


def chain(values, color: str = SOFT, size: float = 40) -> VGroup:
    """``1 -> 2 -> 4 -> 8`` written as a row of numbers joined by arrows."""
    parts = VGroup()
    for i, value in enumerate(values):
        if i:
            parts.add(Tex(r"$\rightarrow$", color=ACCENT, font_size=size))
        parts.add(MathTex(str(value), color=color, font_size=size + 10))
    parts.arrange(RIGHT, buff=0.28)
    return parts


def counter(value: int, size: float = 44) -> VGroup:
    number = MathTex(str(value), color=GOOD, font_size=size + 16)
    word = Text("candies", font_size=size - 16, color=SOFT)
    word.next_to(number, RIGHT, buff=0.22).align_to(number, DOWN)
    return VGroup(number, word)


def underline(mobject, color: str = ACCENT) -> Line:
    return Line(
        mobject.get_corner(DOWN + LEFT), mobject.get_corner(DOWN + RIGHT),
        color=color, stroke_width=4,
    ).shift(DOWN * 0.12)


def bullet(text: str, size: float = 28) -> VGroup:
    dot = Dot(radius=0.06, color=ACCENT)
    label = Text(text, font_size=size, color=SOFT)
    label.next_to(dot, RIGHT, buff=0.22)
    return VGroup(dot, label)


def write_title(scene, text: str, run_time: float = 1.0) -> Text:
    heading = title(text).to_edge(UP, buff=0.5)
    scene.play(Write(heading), run_time=run_time)
    return heading


__all__ = [
    "ACCENT",
    "BACKGROUND",
    "BLACK",
    "DoublingBox",
    "GOOD",
    "SOFT",
    "body",
    "bullet",
    "candy",
    "candy_positions",
    "chain",
    "counter",
    "fit_in_frame",
    "setup_style",
    "title",
    "underline",
    "write_title",
]
