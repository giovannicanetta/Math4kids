"""Scene 1 - the magic doubling box: pressing the button doubles the candies."""

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    FadeIn,
    FadeOut,
    Indicate,
    MathTex,
    Scene,
    VGroup,
    Write,
)

from theme import ACCENT, GOOD, SOFT, DoublingBox, body, chain, setup_style, write_title


class MagicDoublingBox(Scene):
    def construct(self):
        setup_style()
        heading = write_title(self, "A magic doubling box")

        box = DoublingBox(width=4.4, height=2.8).shift(LEFT * 3.3 + DOWN * 0.4)
        self.play(FadeIn(box, shift=UP * 0.3), run_time=1.0)

        rule = body("Each press doubles\nthe candies inside.", size=26)
        start = body("It starts with 1 candy.", size=26, color=GOOD)
        press_label = body("Press 3 times", size=30, color=ACCENT)
        trail = chain([1], size=32)
        power = MathTex(r"2^3 = 8", color=GOOD, font_size=54)

        column = VGroup(rule, start, press_label, trail, power)
        column.arrange(DOWN, buff=0.45, aligned_edge=LEFT)
        column.next_to(box, RIGHT, buff=0.7).align_to(box, UP).shift(UP * 0.3)
        trail_spot = trail.get_corner(LEFT + UP)

        self.play(Write(rule), run_time=1.2)
        self.play(Write(start), run_time=0.9)
        self.wait(0.4)

        # --- three presses -------------------------------------------------
        self.play(Write(press_label), run_time=0.6)
        self.play(FadeIn(trail), run_time=0.4)

        values = [1, 2, 4, 8]
        for step in range(3):
            box.press(self)
            new_trail = chain(values[: step + 2], size=32)
            new_trail.move_to(trail_spot, aligned_edge=LEFT + UP)
            self.play(trail.animate.become(new_trail), run_time=0.4)

        self.play(Write(power), run_time=0.9)
        self.play(Indicate(power, color=GOOD), run_time=0.8)
        self.wait(0.8)

        # --- two presses ----------------------------------------------------
        self.play(FadeOut(VGroup(rule, start, press_label, trail, power)), run_time=0.6)
        box.reset(self, 1)

        press_label2 = body("Press 2 times", size=30, color=ACCENT)
        trail2 = chain([1], size=32)
        power2 = MathTex(r"2^2 = 4", color=GOOD, font_size=54)
        column2 = VGroup(press_label2, trail2, power2)
        column2.arrange(DOWN, buff=0.55, aligned_edge=LEFT)
        column2.next_to(box, RIGHT, buff=0.7)
        trail2_spot = trail2.get_corner(LEFT + UP)

        self.play(Write(press_label2), run_time=0.6)
        self.play(FadeIn(trail2), run_time=0.4)

        values2 = [1, 2, 4]
        for step in range(2):
            box.press(self)
            new_trail = chain(values2[: step + 2], size=32)
            new_trail.move_to(trail2_spot, aligned_edge=LEFT + UP)
            self.play(trail2.animate.become(new_trail), run_time=0.4)

        self.play(Write(power2), run_time=0.9)

        takeaway = body("presses  =  the little number up top", size=28, color=SOFT)
        takeaway.next_to(column2, DOWN, buff=0.9).align_to(column2, LEFT)
        self.play(Write(takeaway), run_time=1.0)
        self.wait(1.5)
        self.play(FadeOut(VGroup(heading, box, column2, takeaway)))
