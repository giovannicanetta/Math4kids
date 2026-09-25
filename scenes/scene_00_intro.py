"""Scene 0 - opening card, and the closing summary card."""

from manim import (
    DOWN,
    UP,
    FadeIn,
    FadeOut,
    MathTex,
    VGroup,
    Write,
)

from theme import ACCENT, GOOD, SOFT, StoryScene, body, title, underline


class Intro(StoryScene):
    def construct(self):
        main = title("Powers turn adding into multiplying", size=48)
        line = underline(main)
        subtitle = body("and logs turn multiplying back into adding", size=32, color=SOFT)
        subtitle.next_to(main, DOWN, buff=0.8)
        hint = MathTex(r"2^{3+2} = 2^3 \times 2^2", color=GOOD, font_size=64)
        hint.next_to(subtitle, DOWN, buff=1.1)

        with self.say("Powers turn adding into multiplying."):
            self.play(Write(main), run_time=1.8)
            self.play(FadeIn(line), run_time=0.4)

        with self.say("And logs turn multiplying back into adding."):
            self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.0)

        with self.say(
            "This is where we are going: two to the three plus two "
            "equals two cubed times two squared."
        ):
            self.play(Write(hint), run_time=1.2)
            self.wait(0.5)

        self.play(FadeOut(VGroup(main, line, subtitle, hint)))


class Outro(StoryScene):
    def construct(self):
        heading = title("Two sides of the same idea").to_edge(UP, buff=0.8)
        with self.say("Powers and logs are two sides of the same idea."):
            self.play(Write(heading), run_time=1.2)

        cards = VGroup(
            VGroup(
                body("POWERS", size=30, color=ACCENT),
                MathTex(r"2^{3+2} = 2^3 \times 2^2", color=GOOD, font_size=46),
                body("add the presses, multiply the candies", size=24, color=SOFT),
            ).arrange(DOWN, buff=0.3),
            VGroup(
                body("LOGS", size=30, color=ACCENT),
                MathTex(r"\log_2 (8 \times 4) = 3 + 2", color=GOOD, font_size=46),
                body("multiply the numbers, add the questions", size=24, color=SOFT),
            ).arrange(DOWN, buff=0.3),
        ).arrange(DOWN, buff=1.3)
        cards.move_to(DOWN * 0.3)

        narration = [
            "With powers, you add the presses and the candies multiply.",
            "With logs, you multiply the numbers and the questions add up.",
        ]
        for card, line in zip(cards, narration):
            with self.say(line):
                self.play(FadeIn(card, shift=UP * 0.2), run_time=1.0)

        moral = body("that is why information is measured with a log", size=30, color=ACCENT)
        moral.next_to(cards, DOWN, buff=0.9)
        with self.say(
            "And that is why information is measured with a log: "
            "possibilities multiply, but information simply adds up."
        ):
            self.play(Write(moral), run_time=1.4)
            self.wait(0.5)

        self.play(FadeOut(VGroup(heading, cards, moral)))
