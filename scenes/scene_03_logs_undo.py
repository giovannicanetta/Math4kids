"""Scene 3 - the log is the undo button, and it turns multiplying into adding."""

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    Arrow,
    Circle,
    Create,
    FadeIn,
    FadeOut,
    Indicate,
    MathTex,
    Scene,
    Text,
    VGroup,
    Write,
)

from theme import ACCENT, GOOD, SOFT, body, setup_style, write_title


class LogIsTheUndoButton(Scene):
    def construct(self):
        setup_style()
        heading = write_title(self, "Logs go the other way")

        undo = Circle(radius=0.7, color=GOOD, fill_color="#123a33", fill_opacity=1, stroke_width=5)
        undo_text = Text("UNDO", font_size=22, color=GOOD, weight="BOLD").move_to(undo)
        undo_group = VGroup(undo, undo_text).to_edge(LEFT, buff=1.6).shift(UP * 1.4)

        question = body('"How many presses made\nthis many candies?"', size=30, color=SOFT)
        question.next_to(undo_group, RIGHT, buff=0.8)

        self.play(Create(undo), Write(undo_text), run_time=0.8)
        self.play(Write(question), run_time=1.2)
        self.wait(0.4)

        rows = VGroup()
        for candies, presses in ((8, 3), (4, 2), (32, 5)):
            lhs = MathTex(rf"{candies} \text{{ candies}}", color=SOFT, font_size=40)
            arrow = Arrow(LEFT, RIGHT, color=GOOD, buff=0, stroke_width=4).scale(0.7)
            rhs = MathTex(rf"\log_2 {candies} = {presses}", color=GOOD, font_size=44)
            row = VGroup(lhs, arrow, rhs).arrange(RIGHT, buff=0.4)
            rows.add(row)
        rows.arrange(DOWN, buff=0.55, aligned_edge=LEFT).move_to(DOWN * 0.9)

        for row in rows:
            self.play(FadeIn(row, shift=RIGHT * 0.3), run_time=0.7)
        self.wait(0.6)

        note = MathTex(r"5 = 3 + 2", color=ACCENT, font_size=52)
        note.next_to(rows, DOWN, buff=0.6)
        self.play(Write(note), run_time=0.8)
        self.play(Indicate(rows[2], color=ACCENT), run_time=1.0)
        self.wait(1.2)

        self.play(FadeOut(VGroup(undo_group, question, rows, note)), run_time=0.8)

        pair = VGroup(
            MathTex(r"8 \times 4 = 32", color=SOFT, font_size=56),
            MathTex(r"\log_2 8 + \log_2 4 = \log_2 32", color=GOOD, font_size=56),
        ).arrange(DOWN, buff=0.9)
        self.play(Write(pair[0]), run_time=0.9)
        self.play(Write(pair[1]), run_time=1.4)

        moral = body("Powers: adding  ->  multiplying.\nLogs: multiplying  ->  adding.", size=32, color=ACCENT)
        moral.next_to(pair, DOWN, buff=0.9)
        self.play(Write(moral), run_time=1.4)
        self.wait(1.5)
        self.play(FadeOut(VGroup(heading, pair, moral)))


class WhyHartleyUsedLogs(Scene):
    """Combining two messages multiplies the possibilities; the log adds them up."""

    def construct(self):
        setup_style()
        heading = write_title(self, "Why Hartley used the log")

        left = VGroup(
            body("Message A", size=28, color=SOFT),
            MathTex(r"8 \text{ possibilities}", color=ACCENT, font_size=40),
            MathTex(r"\log_2 8 = 3 \text{ bits}", color=GOOD, font_size=40),
        ).arrange(DOWN, buff=0.35)
        right = VGroup(
            body("Message B", size=28, color=SOFT),
            MathTex(r"4 \text{ possibilities}", color=ACCENT, font_size=40),
            MathTex(r"\log_2 4 = 2 \text{ bits}", color=GOOD, font_size=40),
        ).arrange(DOWN, buff=0.35)
        VGroup(left, right).arrange(RIGHT, buff=2.0).shift(UP * 1.2)

        self.play(FadeIn(left, shift=UP * 0.2), run_time=0.8)
        self.play(FadeIn(right, shift=UP * 0.2), run_time=0.8)

        together = body("Send both together", size=30, color=SOFT).shift(DOWN * 0.7)
        self.play(Write(together), run_time=0.7)

        multiplied = MathTex(r"8 \times 4 = 32 \text{ possibilities}", color=ACCENT, font_size=48)
        multiplied.next_to(together, DOWN, buff=0.5)
        added = MathTex(r"3 + 2 = 5 \text{ bits}", color=GOOD, font_size=48)
        added.next_to(multiplied, DOWN, buff=0.45)

        self.play(Write(multiplied), run_time=1.0)
        self.play(Write(added), run_time=1.0)

        moral = body("possibilities multiply, information adds", size=28, color=ACCENT)
        moral.next_to(added, DOWN, buff=0.6)
        self.play(Write(moral), run_time=1.1)
        self.wait(1.5)
        self.play(FadeOut(VGroup(heading, left, right, together, multiplied, added, moral)))
