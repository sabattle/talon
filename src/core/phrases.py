from talon import Module, actions
from talon.grammar import Capture
from typing import Optional


mod = Module()


@mod.capture(rule="<word>")
def word(m: Capture) -> str:
    """A single word"""
    return actions.dictate.parse_words(m)[0]


@mod.capture(rule="<phrase>")
def phrase(m: Capture) -> str:
    """A phrase composed of multiple words"""
    return " ".join(actions.dictate.parse_words(m))


@mod.action_class
class Actions:
    def insert_phrase(phrase: str, formatters: Optional[str] = None) -> None:  # type: ignore[misc]
        """Inserts a phrase"""
        # do work to phrase here
        actions.insert(phrase)
