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
    VGroup,
    Write,
)

from theme import ACCENT, GOOD, SOFT, DoublingBox, StoryScene, body, chain, write_title


class MagicDoublingBox(StoryScene):
    def construct(self):
        with self.say("Start with a magic doubling box."):
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

        with self.say(
            "Each time you press its button, the number of candies inside doubles. "
            "It starts with one candy."
        ):
            self.play(Write(rule), run_time=1.2)
            self.play(Write(start), run_time=0.9)

        # --- three presses -------------------------------------------------
        with self.say("Press three times."):
            self.play(Write(press_label), run_time=0.6)
            self.play(FadeIn(trail), run_time=0.4)

        values = [1, 2, 4, 8]
        lines = [
            "One candy becomes two.",
            "Two candies become four.",
            "Four candies become eight.",
        ]
        for step in range(3):
            with self.say(lines[step]):
                box.press(self)
                new_trail = chain(values[: step + 2], size=32)
                new_trail.move_to(trail_spot, aligned_edge=LEFT + UP)
                self.play(trail.animate.become(new_trail), run_time=0.4)

        with self.say("Three presses give eight candies. That is two cubed equals eight."):
            self.play(Write(power), run_time=0.9)
            self.play(Indicate(power, color=GOOD), run_time=0.8)

        # --- two presses ----------------------------------------------------
        with self.say("Now start again with one candy, and press only two times."):
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
        lines2 = ["One candy becomes two.", "Two candies become four."]
        for step in range(2):
            with self.say(lines2[step]):
                box.press(self)
                new_trail = chain(values2[: step + 2], size=32)
                new_trail.move_to(trail2_spot, aligned_edge=LEFT + UP)
                self.play(trail2.animate.become(new_trail), run_time=0.4)

        with self.say("Two presses give four candies. That is two squared equals four."):
            self.play(Write(power2), run_time=0.9)

        takeaway = body("presses  =  the little number up top", size=28, color=SOFT)
        takeaway.next_to(column2, DOWN, buff=0.9).align_to(column2, LEFT)
        with self.say(
            "So the number of presses is the little number written up on top."
        ):
            self.play(Write(takeaway), run_time=1.0)
            self.wait(0.5)
        self.play(FadeOut(VGroup(heading, box, column2, takeaway)))
