"""Scene 0 - opening card, and the closing summary card."""

from manim import (
    DOWN,
    UP,
    FadeIn,
    FadeOut,
    MathTex,
    Scene,
    VGroup,
    Write,
)

from theme import ACCENT, GOOD, SOFT, body, setup_style, title, underline


class Intro(Scene):
    def construct(self):
        setup_style()
        main = title("Powers turn adding into multiplying", size=48)
        line = underline(main)
        subtitle = body("and logs turn multiplying back into adding", size=32, color=SOFT)
        subtitle.next_to(main, DOWN, buff=0.8)

        self.play(Write(main), run_time=1.8)
        self.play(FadeIn(line), run_time=0.4)
        self.play(FadeIn(subtitle, shift=UP * 0.2), run_time=1.0)

        hint = MathTex(r"2^{3+2} = 2^3 \times 2^2", color=GOOD, font_size=64)
        hint.next_to(subtitle, DOWN, buff=1.1)
        self.play(Write(hint), run_time=1.2)
        self.wait(1.5)
        self.play(FadeOut(VGroup(main, line, subtitle, hint)))


class Outro(Scene):
    def construct(self):
        setup_style()
        heading = title("Two sides of the same idea").to_edge(UP, buff=0.8)
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

        for card in cards:
            self.play(FadeIn(card, shift=UP * 0.2), run_time=1.0)

        moral = body("that is why information is measured with a log", size=30, color=ACCENT)
        moral.next_to(cards, DOWN, buff=0.9)
        self.play(Write(moral), run_time=1.4)
        self.wait(2.0)
        self.play(FadeOut(VGroup(heading, cards, moral)))
