"""Scene 6 - what "8 possibilities" really means, and how bits count them.

Two notes arrive: message A says which of 8 doors hides the treasure, message B
says which of 4 weathers it is. Counting the codes needed to write each note is
where "bits" come from, and combining the notes is where the log identity shows
up on its own.
"""

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    Create,
    FadeIn,
    FadeOut,
    Indicate,
    MathTex,
    Rectangle,
    SurroundingRectangle,
    Text,
    VGroup,
    Write,
)


from theme import ACCENT, GOOD, SOFT, StoryScene, body, write_title

DOOR_BODY = "#2d3561"
DIM = "#39406b"

WEATHERS = ["sunny", "cloudy", "rainy", "snowy"]
DOOR_CODES = ["000", "001", "010", "011", "100", "101", "110", "111"]
WEATHER_CODES = ["00", "01", "10", "11"]


def door(number: int, scale: float = 1.0) -> VGroup:
    """A little numbered door."""
    panel = Rectangle(
        width=0.62, height=1.0,
        color=ACCENT, fill_color=DOOR_BODY, fill_opacity=1, stroke_width=3,
    )
    knob = MathTex(r"\bullet", color=ACCENT, font_size=26)
    knob.move_to(panel.get_right() + LEFT * 0.14)
    label = Text(str(number), font_size=22, color=SOFT)
    label.move_to(panel.get_top() + DOWN * 0.28)
    return VGroup(panel, knob, label).scale(scale)


def doors(count: int = 8, scale: float = 1.0) -> VGroup:
    row = VGroup(*[door(n, scale) for n in range(1, count + 1)])
    row.arrange(RIGHT, buff=0.18)
    return row


def weather_cards() -> VGroup:
    cards = VGroup()
    for name in WEATHERS:
        card = Rectangle(
            width=1.5, height=0.72,
            color=ACCENT, fill_color=DOOR_BODY, fill_opacity=1, stroke_width=3,
        )
        label = Text(name, font_size=22, color=SOFT).move_to(card)
        cards.add(VGroup(card, label))
    cards.arrange(RIGHT, buff=0.22)
    return cards


class WhatPossibilitiesMean(StoryScene):
    """"Possibilities" = the messages that could arrive, before you know which."""

    def construct(self):
        with self.say('What does "eight possibilities" mean?'):
            heading = write_title(self, 'What "8 possibilities" means')

        definition = body(
            "possibilities = the messages that could be sent,\nbefore you know which one it really is",
            size=28,
        )
        definition.next_to(heading, DOWN, buff=0.5)
        with self.say(
            "Possibilities counts the messages that could be sent, "
            "before you know which one actually is."
        ):
            self.play(Write(definition), run_time=1.6)

        label_a = body("Message A: which door hides the treasure", size=28, color=ACCENT)
        row = doors(8)
        group_a = VGroup(label_a, row).arrange(DOWN, buff=0.45)
        group_a.next_to(definition, DOWN, buff=0.7)

        with self.say(
            "Message A: a friend hides a treasure behind one of eight doors, "
            "and sends you a note saying which door."
        ):
            self.play(Write(label_a), run_time=1.0)
            self.play(Create(row), run_time=1.2)

        count_a = MathTex(r"8 \text{ possibilities}", color=GOOD, font_size=42)
        count_a.next_to(row, DOWN, buff=0.45)
        with self.say(
            "Before the note arrives there are eight things it could say: "
            "door one, door two, door three, all the way to door eight."
        ):
            for tile in row:
                self.play(Indicate(tile, color=GOOD, scale_factor=1.12), run_time=0.22)
            self.play(Write(count_a), run_time=0.8)

        self.play(FadeOut(VGroup(definition, group_a, count_a)), run_time=0.7)

        label_b = body("Message B: today's weather", size=28, color=ACCENT)
        cards = weather_cards()
        count_b = MathTex(r"4 \text{ possibilities}", color=GOOD, font_size=42)
        group_b = VGroup(label_b, cards, count_b).arrange(DOWN, buff=0.5)
        group_b.next_to(heading, DOWN, buff=0.9)

        with self.say(
            "Message B: your friend tells you today's weather, "
            "and it is always one of four kinds: sunny, cloudy, rainy or snowy."
        ):
            self.play(Write(label_b), run_time=0.9)
            for card in cards:
                self.play(FadeIn(card, shift=UP * 0.2), run_time=0.4)
            self.play(Write(count_b), run_time=0.8)

        point = body(
            "the information is not in the words of the note,\n"
            "it is in how much uncertainty the note removes",
            size=28,
            color=ACCENT,
        )
        point.next_to(group_b, DOWN, buff=0.8)
        with self.say(
            "The information is not in the words of the note. "
            "It is in how much uncertainty the note removes. "
            "Message A picks one answer out of eight, and message B picks one out of four. "
            "Picking out of more options tells you more."
        ):
            self.play(Write(point), run_time=2.0)

        self.play(FadeOut(VGroup(group_b, point)), run_time=0.7)

        only_one = doors(1).scale(1.4)
        always = body("the treasure is always behind door 1", size=28)
        nothing = body("the note tells you nothing new", size=30, color=ACCENT)
        zero = MathTex(r"\log 1 = 0", color=GOOD, font_size=60)
        tail = VGroup(only_one, always, nothing, zero).arrange(DOWN, buff=0.5)
        tail.move_to(DOWN * 0.3)

        with self.say(
            "And if there were only one possibility, say the treasure is always behind door one, "
            "then the note tells you nothing new. That is why the log of one is zero."
        ):
            self.play(Create(only_one), run_time=0.7)
            self.play(Write(always), run_time=1.0)
            self.play(Write(nothing), run_time=1.0)
            self.play(Write(zero), run_time=1.0)
            self.wait(0.5)
        self.play(FadeOut(VGroup(heading, tail)))


class BitsAndCodes(StoryScene):
    """A bit is one yes/no answer: how many does it take to pin the message down?"""

    def construct(self):
        with self.say("Now the connection with bits."):
            heading = write_title(self, "The connection with bits")

        idea = body(
            "a bit is the answer to one yes/no question, written as 1 or 0\n"
            "how many yes/no answers pin down the message?",
            size=28,
        )
        idea.next_to(heading, DOWN, buff=0.45)
        with self.say(
            "A bit is the answer to one yes or no question, written as a one or a zero. "
            "So you can ask: how many yes or no answers does it take to pin down the message?"
        ):
            self.play(Write(idea), run_time=2.2)

        left_col = VGroup()
        right_col = VGroup()
        for index, code in enumerate(DOOR_CODES):
            entry = VGroup(
                Text(f"door {index + 1}", font_size=26, color=SOFT),
                MathTex(r"\rightarrow", color=ACCENT, font_size=30),
                Text(code, font_size=28, color=GOOD),
            ).arrange(RIGHT, buff=0.3)
            (left_col if index < 4 else right_col).add(entry)
        left_col.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        right_col.arrange(DOWN, buff=0.28, aligned_edge=LEFT)
        table = VGroup(left_col, right_col).arrange(RIGHT, buff=1.2)
        table.next_to(idea, DOWN, buff=0.6)

        with self.say(
            "Message A, the eight doors: give every door a code of three zeros and ones."
        ):
            self.play(FadeIn(left_col, shift=RIGHT * 0.2), run_time=1.0)
            self.play(FadeIn(right_col, shift=RIGHT * 0.2), run_time=1.0)

        facts = VGroup(
            MathTex(r"3 \text{ digits}: \; 2 \times 2 \times 2 = 8 \text{ codes}", color=SOFT, font_size=38),
            MathTex(r"2 \text{ digits}: \; \text{only } 4 \text{ codes, not enough}", color=SOFT, font_size=38),
            MathTex(r"\log_2 8 = 3 \text{ bits}", color=GOOD, font_size=46),
        ).arrange(DOWN, buff=0.35)
        facts.next_to(table, DOWN, buff=0.55)

        fact_lines = [
            "Three digits give exactly two times two times two, which is eight codes, one per door.",
            "Two digits would give only four codes, which is not enough.",
            "So message A carries three bits, and log base two of eight is three.",
        ]
        for fact, line in zip(facts, fact_lines):
            with self.say(line):
                self.play(Write(fact), run_time=1.0)

        self.play(FadeOut(VGroup(idea, facts)), table.animate.next_to(heading, DOWN, buff=0.7), run_time=0.8)

        question = body('the first digit answers: "is it in the upper half, doors 5-8?"', size=28, color=ACCENT)
        question.next_to(table, DOWN, buff=0.7)
        upper_half = SurroundingRectangle(right_col, color=GOOD, buff=0.2, stroke_width=4)
        with self.say(
            "Each digit is the answer to one yes or no question. "
            "The first digit answers: is it in the upper half, doors five to eight? "
            "And so on for the digits after it."
        ):
            self.play(Write(question), run_time=1.6)
            self.play(Create(upper_half), run_time=0.9)

        self.play(FadeOut(VGroup(table, question, upper_half)), run_time=0.7)

        names = VGroup(*[Text(name, font_size=28, color=SOFT) for name in WEATHERS])
        names.arrange(DOWN, buff=0.32, aligned_edge=RIGHT)
        arrows = VGroup(*[MathTex(r"\rightarrow", color=ACCENT, font_size=32) for _ in WEATHERS])
        codes_col = VGroup(*[Text(code, font_size=30, color=GOOD) for code in WEATHER_CODES])
        codes_col.arrange(DOWN, buff=0.32, aligned_edge=LEFT)
        for arrow, name in zip(arrows, names):
            arrow.next_to(name, RIGHT, buff=0.3)
        codes_col.next_to(arrows, RIGHT, buff=0.3)
        for code, name in zip(codes_col, names):
            code.match_y(name)
        weather_rows = VGroup(names, arrows, codes_col)
        weather_facts = VGroup(
            MathTex(r"2 \text{ digits}: \; 2 \times 2 = 4 \text{ codes}", color=SOFT, font_size=38),
            MathTex(r"\log_2 4 = 2 \text{ bits}", color=GOOD, font_size=46),
        ).arrange(DOWN, buff=0.35)
        weather_block = VGroup(weather_rows, weather_facts).arrange(DOWN, buff=0.6)
        weather_block.move_to(DOWN * 0.3)

        with self.say(
            "Message B, the four weathers: sunny is zero zero, cloudy is zero one, "
            "rainy is one zero, snowy is one one."
        ):
            self.play(FadeIn(weather_rows, shift=UP * 0.2), run_time=1.2)
        with self.say(
            "Two digits give two times two, which is four codes. "
            "So message B carries two bits, and log base two of four is two."
        ):
            self.play(Write(weather_facts[0]), run_time=1.0)
            self.play(Write(weather_facts[1]), run_time=1.0)

        self.play(FadeOut(weather_block), run_time=0.7)

        rule = VGroup(
            body("the general rule", size=30, color=ACCENT),
            MathTex(r"k \text{ bits label } 2^k \text{ possibilities}", color=SOFT, font_size=46),
            MathTex(r"2^k = N \quad \Longleftrightarrow \quad k = \log_2 N", color=GOOD, font_size=52),
        ).arrange(DOWN, buff=0.6)
        rule.move_to(DOWN * 0.3)
        with self.say(
            "The general rule: with k bits you can label two to the k possibilities. "
            "So the number of bits you need is the k with two to the k equal to N, "
            "which is k equals log base two of N."
        ):
            self.play(Write(rule[0]), run_time=0.8)
            self.play(Write(rule[1]), run_time=1.2)
            self.play(Write(rule[2]), run_time=1.6)
            self.wait(0.5)
        self.play(FadeOut(VGroup(heading, rule)))


class SendingBothMessages(StoryScene):
    """Both notes at once: the possibilities multiply while the bits add."""

    def construct(self):
        with self.say("Now your friend sends both notes, the door and the weather."):
            heading = write_title(self, "Sending both messages")

        multiply = VGroup(
            body("every door can go with every weather", size=28),
            MathTex(r"8 \times 4 = 32 \text{ possible combined messages}", color=ACCENT, font_size=44),
            body('"door 3, rainy"        "door 7, sunny"', size=26, color=SOFT),
        ).arrange(DOWN, buff=0.45)
        multiply.next_to(heading, DOWN, buff=0.6)

        with self.say(
            "The possibilities multiply. Every door can go with every weather, "
            "so there are eight times four, that is thirty two possible combined messages, "
            "like door three rainy, or door seven sunny."
        ):
            self.play(Write(multiply[0]), run_time=1.2)
            self.play(Write(multiply[1]), run_time=1.4)
            self.play(Write(multiply[2]), run_time=1.2)

        codes = VGroup(
            Text("010", font_size=44, color=GOOD),
            MathTex(r"+", color=SOFT, font_size=44),
            Text("10", font_size=44, color=GOOD),
            MathTex(r"=", color=SOFT, font_size=44),
            Text("01010", font_size=44, color=ACCENT),
        ).arrange(RIGHT, buff=0.35)
        caption = body("door 3            rainy            both notes", size=24)
        caption.next_to(codes, DOWN, buff=0.3)
        bits = MathTex(r"3 + 2 = 5 \text{ bits}", color=GOOD, font_size=48)
        stack = VGroup(codes, caption, bits).arrange(DOWN, buff=0.45)
        stack.next_to(multiply, DOWN, buff=0.7)

        with self.say(
            "But the bits add. Write the door code and then the weather code: "
            "door three is zero one zero, rainy is one zero, "
            "together that is zero one zero one zero. Three bits plus two bits is five bits."
        ):
            self.play(Write(codes), run_time=1.6)
            self.play(FadeIn(caption), run_time=0.6)
            self.play(Write(bits), run_time=1.0)

        check = MathTex(r"\log_2 32 = 5, \qquad 2^5 = 32 \text{ codes}", color=SOFT, font_size=40)
        check.next_to(stack, DOWN, buff=0.5)
        with self.say(
            "Check: log base two of thirty two is five, "
            "and five bits give exactly two to the five, that is thirty two codes."
        ):
            self.play(Write(check), run_time=1.4)

        self.play(FadeOut(VGroup(multiply, stack, check)), run_time=0.8)

        identity = MathTex(
            r"\log_2(8 \times 4) = \log_2 8 + \log_2 4", color=ACCENT, font_size=56
        )
        numbers = MathTex(r"5 = 3 + 2", color=GOOD, font_size=56)
        moral = body(
            "possibilities multiply when you combine messages,\n"
            "but information should add up, like weights or lengths",
            size=28,
        )
        block = VGroup(identity, numbers, moral).arrange(DOWN, buff=0.6)
        block.move_to(DOWN * 0.3)

        with self.say(
            "This is the whole point of using the log: "
            "log of eight times four equals log of eight plus log of four, and five is three plus two."
        ):
            self.play(Write(identity), run_time=1.8)
            self.play(Write(numbers), run_time=1.0)
        with self.say(
            "Possibilities multiply when you combine messages, "
            "but information should add up, like weights or lengths. "
            "The log is the function that turns one into the other."
        ):
            self.play(Write(moral), run_time=2.0)

        self.play(FadeOut(block), run_time=0.7)

        caveat = VGroup(
            body("one caveat", size=30, color=ACCENT),
            body(
                "this counting assumes every possibility is equally likely,\n"
                "as in Hartley's setting",
                size=28,
            ),
            body(
                "if it almost always rains, the weather note tells you\n"
                "less than 2 bits on average - that is Shannon's entropy",
                size=28,
            ),
        ).arrange(DOWN, buff=0.55)
        caveat.move_to(DOWN * 0.3)

        with self.say(
            "One caveat: this counting assumes every possibility is equally likely, "
            "as in Hartley's setting."
        ):
            self.play(Write(caveat[0]), run_time=0.8)
            self.play(Write(caveat[1]), run_time=1.6)
        with self.say(
            "If it almost always rains, the weather note tells you less than two bits on average. "
            "Shannon's entropy handles that case."
        ):
            self.play(Write(caveat[2]), run_time=1.8)
            self.wait(0.5)
        self.play(FadeOut(VGroup(heading, caveat)))
