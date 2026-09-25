"""Scene 4 - what a log is: counting steps of multiplying instead of adding."""

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    Arrow,
    FadeIn,
    FadeOut,
    Indicate,
    MathTex,
    Scene,
    VGroup,
    Write,
)

from pizza import pizza_with_slices
from theme import ACCENT, GOOD, SOFT, body, setup_style, write_title


def ladder(values, color=SOFT, label=r"\times 2"):
    """A row ``1 -> 2 -> 4 -> 8`` with an annotated arrow between each pair."""
    group = VGroup()
    arrows = VGroup()
    numbers = VGroup()
    for index, value in enumerate(values):
        number = MathTex(str(value), color=color, font_size=54)
        numbers.add(number)
        if index:
            arrow = Arrow(LEFT, RIGHT, buff=0, color=ACCENT, stroke_width=4).scale(0.55)
            tag = MathTex(label, color=ACCENT, font_size=30)
            arrows.add(VGroup(arrow, tag))
    pieces = VGroup()
    for index, number in enumerate(numbers):
        if index:
            pieces.add(arrows[index - 1])
        pieces.add(number)
    pieces.arrange(RIGHT, buff=0.35)
    for arrow, _ in zip(arrows, arrows):
        arrow[1].next_to(arrow[0], UP, buff=0.12)
    group.add(pieces)
    group.numbers = numbers
    group.arrows = arrows
    return group


class WhatIsALog(Scene):
    def construct(self):
        setup_style()
        heading = write_title(self, "What is a log?")

        question = body('"How many times do I multiply by 2 to reach this number?"', size=30, color=SOFT)
        question.next_to(heading, DOWN, buff=0.6)
        self.play(Write(question), run_time=1.4)

        examples = [
            ([1, 2, 4, 8], r"\log_2 8 = 3"),
            ([1, 2, 4, 8, 16], r"\log_2 16 = 4"),
        ]
        anchor = question
        drawn = VGroup()
        for values, answer in examples:
            row = ladder(values)
            row.next_to(anchor, DOWN, buff=1.0).to_edge(LEFT, buff=1.4)
            self.play(FadeIn(row.numbers[0]), run_time=0.3)
            for index in range(1, len(values)):
                self.play(
                    FadeIn(row.arrows[index - 1], shift=RIGHT * 0.2),
                    FadeIn(row.numbers[index], shift=RIGHT * 0.2),
                    run_time=0.45,
                )
            result = MathTex(answer, color=GOOD, font_size=50)
            result.next_to(row, RIGHT, buff=0.9)
            self.play(Write(result), run_time=0.7)
            drawn.add(row, result)
            anchor = row

        zero = MathTex(r"\log_2 1 = 0", color=GOOD, font_size=50)
        zero_note = body("1 is where you start: no multiplying needed", size=26, color=SOFT)
        zero.next_to(anchor, DOWN, buff=1.1).to_edge(LEFT, buff=1.4)
        zero_note.next_to(zero, RIGHT, buff=0.6)
        self.play(Write(zero), run_time=0.7)
        self.play(Write(zero_note), run_time=1.0)
        self.wait(0.8)

        moral = body("counting counts +1 steps.  a log counts  x2  steps.", size=30, color=ACCENT)
        moral.next_to(zero, DOWN, buff=1.1).to_edge(LEFT, buff=1.4)
        self.play(Write(moral), run_time=1.3)
        self.wait(1.5)
        self.play(FadeOut(VGroup(heading, question, drawn, zero, zero_note, moral)))


class CuttingInHalf(Scene):
    """The same question backwards: how many halvings to get down to 1?"""

    def construct(self):
        setup_style()
        heading = write_title(self, "Going backwards: cutting in half")

        pizza_note = body("How many times can you halve it before only 1 is left?", size=30)
        pizza_note.next_to(heading, DOWN, buff=0.5)
        self.play(Write(pizza_note), run_time=1.2)

        slices = [16, 8, 4, 2, 1]
        pizzas = VGroup(*[pizza_with_slices(n).scale(0.8) for n in slices])
        pizzas.arrange(RIGHT, buff=0.55).shift(DOWN * 0.2)

        labels = VGroup()
        for pizza, n in zip(pizzas, slices):
            label = MathTex(str(n), color=SOFT, font_size=40).next_to(pizza, DOWN, buff=0.25)
            labels.add(label)

        self.play(FadeIn(pizzas[0], scale=0.6), Write(labels[0]), run_time=0.8)
        arrows = VGroup()
        for index in range(1, len(slices)):
            arrow = Arrow(
                pizzas[index - 1].get_right(), pizzas[index].get_left(),
                buff=0.12, color=ACCENT, stroke_width=4,
            )
            tag = MathTex(r"\div 2", color=ACCENT, font_size=28).next_to(arrow, UP, buff=0.1)
            arrows.add(VGroup(arrow, tag))
            self.play(
                FadeIn(arrows[index - 1]),
                FadeIn(pizzas[index], scale=0.6),
                Write(labels[index]),
                run_time=0.6,
            )

        count = body("4 halvings", size=32, color=GOOD).next_to(pizzas, DOWN, buff=0.9)
        answer = MathTex(r"\log_2 16 = 4", color=GOOD, font_size=56).next_to(count, DOWN, buff=0.4)
        self.play(Write(count), run_time=0.7)
        self.play(Write(answer), run_time=0.9)
        self.play(Indicate(answer, color=GOOD), run_time=0.9)
        self.wait(1.5)
        self.play(FadeOut(VGroup(heading, pizza_note, pizzas, labels, arrows, count, answer)))
