"""Scene 2 - 3 presses then 2 more: adding presses multiplies the candies."""

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    Circumscribe,
    FadeIn,
    FadeOut,
    MathTex,
    Scene,
    SurroundingRectangle,
    Transform,
    VGroup,
    Write,
)

from theme import ACCENT, GOOD, SOFT, DoublingBox, body, setup_style, write_title


class AddingPresses(Scene):
    def construct(self):
        setup_style()
        heading = write_title(self, "Press 3 times, then 2 more")

        box = DoublingBox(width=4.2, height=2.7).shift(LEFT * 3.6 + DOWN * 0.5)
        self.play(FadeIn(box, shift=UP * 0.3), run_time=0.8)

        count = MathTex("1", color=GOOD, font_size=56)
        count.next_to(box.shell, LEFT, buff=0.4)
        self.play(FadeIn(count))

        tally = MathTex(r"3 + 2 = 5 \text{ presses}", color=ACCENT, font_size=40)
        step_one = body("First 3 presses", size=26, color=SOFT)
        got_eight = MathTex(r"2^3 = 8 \text{ candies}", color=GOOD, font_size=38)
        step_two = body("2 more presses\ndouble it twice", size=26, color=SOFT)
        times_four = MathTex(r"\times 2 \;\times 2 \;=\; \times 4", color=ACCENT, font_size=38)
        result = MathTex(r"8 \times 4 = 32", color=GOOD, font_size=46)
        also = MathTex(r"2^5 = 32", color=GOOD, font_size=46)

        column = VGroup(tally, step_one, got_eight, step_two, times_four, result, also)
        column.arrange(DOWN, buff=0.35, aligned_edge=LEFT)
        column.next_to(box, RIGHT, buff=0.6).to_edge(UP, buff=1.3)

        self.play(Write(tally), run_time=0.9)
        self.play(Write(step_one), run_time=0.6)

        for value in (2, 4, 8):
            box.press(self, run_time=0.6)
            self.play(Transform(count, MathTex(str(value), color=GOOD, font_size=56).move_to(count)), run_time=0.3)

        self.play(Write(got_eight), run_time=0.8)
        self.play(Circumscribe(got_eight, color=GOOD), run_time=1.0)

        # --- two more presses ------------------------------------------------
        self.play(Write(step_two), run_time=0.8)
        self.play(Write(times_four), run_time=0.8)

        for value in (16, 32):
            box.press(self, run_time=0.6)
            self.play(Transform(count, MathTex(str(value), color=GOOD, font_size=56).move_to(count)), run_time=0.3)

        self.play(Write(result), run_time=0.9)
        self.play(Write(also), run_time=0.8)
        self.wait(1.0)

        # --- the rule ----------------------------------------------------------
        self.play(
            FadeOut(VGroup(box, count, tally, step_one, got_eight, step_two, times_four)),
            VGroup(result, also).animate.arrange(RIGHT, buff=1.2).move_to(UP * 1.6),
            run_time=1.0,
        )

        rule = MathTex(r"2^{3+2}", r"=", r"2^3", r"\times", r"2^2", font_size=90)
        rule.set_color_by_tex("2^{3+2}", ACCENT)
        rule.set_color_by_tex("2^3", GOOD)
        rule.set_color_by_tex("2^2", GOOD)
        rule.move_to(DOWN * 0.8)
        self.play(Write(rule), run_time=1.6)

        caption = body("added presses  ->  multiplied candies", size=30, color=ACCENT)
        caption.next_to(rule, DOWN, buff=0.8)
        self.play(Write(caption), run_time=1.0)
        self.play(Circumscribe(rule, color=ACCENT), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(VGroup(heading, result, also, rule, caption)))


class AllTheTwos(Scene):
    """The simpler way to see it: all the 2s written in a row."""

    def construct(self):
        setup_style()
        heading = write_title(self, "It is just all the 2s in a row")

        left = MathTex(r"(2\times 2\times 2)", r"\times", r"(2 \times 2)", font_size=70)
        left[0].set_color(GOOD)
        left[2].set_color(ACCENT)
        left.move_to(UP * 1.0)
        self.play(Write(left), run_time=1.5)

        brace_a = SurroundingRectangle(left[0], color=GOOD, buff=0.15)
        brace_b = SurroundingRectangle(left[2], color=ACCENT, buff=0.15)
        label_a = body("three 2s", size=26, color=GOOD).next_to(brace_a, UP, buff=0.25)
        label_b = body("two 2s", size=26, color=ACCENT).next_to(brace_b, UP, buff=0.25)
        self.play(FadeIn(brace_a), Write(label_a), run_time=0.7)
        self.play(FadeIn(brace_b), Write(label_b), run_time=0.7)
        self.wait(0.6)

        flat = MathTex(r"2\times 2\times 2\times 2\times 2", font_size=70, color=SOFT)
        flat.move_to(DOWN * 0.6)
        self.play(Transform(left.copy(), flat), run_time=1.4)
        self.add(flat)

        five = body("three 2s + two 2s = five 2s", size=32, color=ACCENT)
        five.next_to(flat, DOWN, buff=0.7)
        self.play(Write(five), run_time=1.0)

        final = MathTex(r"= 2^5 = 32", color=GOOD, font_size=64)
        final.next_to(five, DOWN, buff=0.6)
        self.play(Write(final), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(VGroup(heading, left, brace_a, brace_b, label_a, label_b, flat, five, final)))
