"""The whole story in one scene, in the order of the text."""

from manim import Scene

from scene_00_intro import Intro, Outro
from scene_01_doubling_box import MagicDoublingBox
from scene_02_adding_presses import AddingPresses, AllTheTwos
from scene_03_logs_undo import LogIsTheUndoButton, WhyHartleyUsedLogs
from scene_04_what_is_a_log import CuttingInHalf, WhatIsALog
from scene_05_guessing_game import GuessingGame, LogsAndDigits

CHAPTERS = [
    Intro,
    MagicDoublingBox,
    AddingPresses,
    AllTheTwos,
    LogIsTheUndoButton,
    WhyHartleyUsedLogs,
    WhatIsALog,
    CuttingInHalf,
    GuessingGame,
    LogsAndDigits,
    Outro,
]


class PowersAndLogs(Scene):
    def construct(self):
        for chapter in CHAPTERS:
            chapter.construct(self)
            self.clear()
