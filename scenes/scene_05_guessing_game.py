"""Scene 5 - the guessing game: every yes/no question halves the possibilities."""

from manim import (
    DOWN,
    LEFT,
    RIGHT,
    UP,
    FadeIn,
    FadeOut,
    Indicate,
    MathTex,
    Square,
    Text,
    VGroup,
    Write,
)

from theme import ACCENT, GOOD, SOFT, StoryScene, body, write_title

DIM = "#39406b"


def number_tiles(count: int = 16) -> VGroup:
    tiles = VGroup()
    for value in range(1, count + 1):
        box = Square(side_length=0.72, color=ACCENT, fill_color="#1c2142", fill_opacity=1, stroke_width=3)
        label = Text(str(value), font_size=26, color=SOFT).move_to(box)
        tiles.add(VGroup(box, label))
    tiles.arrange(RIGHT, buff=0.14)
    return tiles


class GuessingGame(StoryScene):
    def construct(self):
        with self.say("Now the guessing game. This is the information part."):
            heading = write_title(self, "The guessing game")

        prompt = body('"I am thinking of a number from 1 to 16.\nYou may only ask yes/no questions."', size=28)
        prompt.next_to(heading, DOWN, buff=0.45)
        with self.say(
            "I am thinking of a number from one to sixteen. "
            "You may only ask yes or no questions."
        ):
            self.play(Write(prompt), run_time=1.6)

        tiles = number_tiles(16).scale(0.95)
        tiles.next_to(prompt, DOWN, buff=0.7)
        with self.say(
            "The smart way is to ask a question that cuts the possibilities in half each time."
        ):
            self.play(FadeIn(tiles, shift=UP * 0.2), run_time=1.0)

        question_line = body('"Is it more than 12?"  No', size=30, color=ACCENT)
        counter = MathTex(r"16 \text{ left}", color=GOOD, font_size=40)
        answer = MathTex(r"4 \text{ questions for } 16 \text{ numbers}", color=GOOD, font_size=40)
        log_line = MathTex(r"\log_2 16 = 4", color=GOOD, font_size=52)
        column = VGroup(question_line, counter, answer, log_line)
        column.arrange(DOWN, buff=0.45).next_to(tiles, DOWN, buff=0.6)
        question_line.set_opacity(0)
        self.play(Write(counter), run_time=0.5)

        steps = [
            ('"Is it more than 8?"  Yes', range(0, 8), 8, "Is it more than eight? Yes. Now eight numbers are left."),
            ('"Is it more than 12?"  No', range(12, 16), 4, "Is it more than twelve? No. Now four are left."),
            ('"Is it more than 10?"  No', range(10, 12), 2, "Is it more than ten? No. Now two are left."),
            ('"Is it 9?"  Yes!', range(9, 10), 1, "Is it nine? Yes. Done."),
        ]

        tally = VGroup()
        for index, (question, killed, left, line) in enumerate(steps, start=1):
            new_question = body(question, size=30, color=ACCENT)
            new_question.move_to(question_line)
            with self.say(line):
                self.play(question_line.animate.become(new_question), run_time=0.6)
                self.play(
                    *[tiles[i].animate.set_opacity(0.18) for i in killed],
                    run_time=0.7,
                )
                new_counter = MathTex(rf"{left} \text{{ left}}", color=GOOD, font_size=40).move_to(counter)
                self.play(counter.animate.become(new_counter), run_time=0.4)
            mark = MathTex(rf"Q_{index}", color=SOFT, font_size=30)
            tally.add(mark)
            tally.arrange(RIGHT, buff=0.35).to_corner(DOWN + RIGHT, buff=0.5)
            self.play(FadeIn(mark), run_time=0.25)

        with self.say(
            "That is four questions for sixteen numbers, and log base two of sixteen is four."
        ):
            self.play(Indicate(tiles[8], color=GOOD, scale_factor=1.4), run_time=1.0)
            self.play(Write(answer), run_time=0.9)
            self.play(Write(log_line), run_time=0.9)

        self.play(
            FadeOut(VGroup(prompt, tiles, counter, question_line, answer, tally)),
            log_line.animate.move_to(UP * 1.8),
            run_time=0.9,
        )

        table = VGroup(
            MathTex(r"32 \text{ numbers} \;\Rightarrow\; 5 \text{ questions}", color=SOFT, font_size=44),
            MathTex(r"1024 \text{ numbers} \;\Rightarrow\; 10 \text{ questions}", color=SOFT, font_size=44),
        ).arrange(DOWN, buff=0.5)
        table.next_to(log_line, DOWN, buff=0.9)
        table_lines = [
            "With thirty two numbers you need just one more question, "
            "because one question halves thirty two to sixteen.",
            "And with one thousand and twenty four numbers you need only ten questions.",
        ]
        for row, line in zip(table, table_lines):
            with self.say(line):
                self.play(FadeIn(row, shift=RIGHT * 0.2), run_time=0.7)

        moral = body("the log = how many yes/no questions = bits of information", size=30, color=ACCENT)
        moral.next_to(table, DOWN, buff=0.9)
        with self.say(
            "So the log is the number of yes or no questions you need to find the answer. "
            "That is exactly what bits of information means, "
            "and it is the idea behind Hartley's and Shannon's measure."
        ):
            self.play(Write(moral), run_time=1.5)
            self.wait(0.5)
        self.play(FadeOut(VGroup(heading, log_line, table, moral)))


class LogsAndDigits(StoryScene):
    """Another way to see it: in base 10 the log counts the digits, minus one."""

    def construct(self):
        with self.say(
            "There is another way to see it. In ordinary base ten numbers, "
            "the log is roughly how many digits a number has."
        ):
            heading = write_title(self, "Another way to see it: digits")

        rows = VGroup()
        for number, digits, log_value in (("10", 2, 1), ("1000", 4, 3)):
            numeral = MathTex(number, color=SOFT, font_size=64)
            digit_text = body(f"{digits} digits", size=28, color=ACCENT)
            log_text = MathTex(rf"\log_{{10}} {number} = {log_value}", color=GOOD, font_size=48)
            row = VGroup(numeral, digit_text, log_text).arrange(RIGHT, buff=1.1)
            rows.add(row)
        rows.arrange(DOWN, buff=1.0, aligned_edge=LEFT).next_to(heading, DOWN, buff=1.2)

        row_lines = [
            "Ten has two digits, and log base ten of ten is one.",
            "One thousand has four digits, and log base ten of one thousand is three.",
        ]
        for row, line in zip(rows, row_lines):
            with self.say(line):
                self.play(FadeIn(row[0], scale=0.7), run_time=0.5)
                self.play(Write(row[1]), run_time=0.5)
                self.play(Write(row[2]), run_time=0.7)

        note = body("the log is the number of zeros: digits minus 1", size=30, color=ACCENT)
        note.next_to(rows, DOWN, buff=1.0)
        with self.say(
            "It is the number of zeros, or the number of digits minus one, for these numbers."
        ):
            self.play(Write(note), run_time=1.2)

        moral = body(
            "A log measures how big a number is by counting\n"
            "how many multiplications build it, not by counting one by one.",
            size=28,
            color=SOFT,
        )
        moral.next_to(note, DOWN, buff=0.8)
        with self.say(
            "A log measures how big a number is by counting how many multiplications "
            "it takes to build it, not by counting one by one."
        ):
            self.play(Write(moral), run_time=2.0)
            self.wait(0.5)
        self.play(FadeOut(VGroup(heading, rows, note, moral)))
