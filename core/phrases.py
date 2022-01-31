from talon import Module, actions
from talon.grammar import Phrase
from typing import Union

mod = Module()


@mod.capture(rule="<word>")
def word(m) -> str:
    """A single word"""
    return actions.dictate.parse_words(m)[0]


@mod.capture(rule="<phrase>")
def phrase(m) -> str:
    """A phrase composed of multiple words"""
    return " ".join(actions.dictate.parse_words(m))


@mod.action_class
class Actions:
    def insert_phrase(phrase: Union[str, Phrase]):
        """Inserts a phrase"""
        # do work to phrase here
        actions.insert(phrase)
