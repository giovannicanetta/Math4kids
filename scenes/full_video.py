"""The whole story in one scene, in the order of the text."""

from theme import StoryScene

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


class PowersAndLogs(StoryScene):
    def construct(self):
        for index, chapter in enumerate(CHAPTERS):
            chapter.construct(self)
            self.clear()
            if index < len(CHAPTERS) - 1:
                self.chapter_break()
