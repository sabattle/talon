from talon import Module, Context
from yaml import safe_load
from pathlib import Path
from ..config import BASE_DIR

KEYMAPS_PATH = Path(BASE_DIR, "keymaps")

mod = Module()
mod.list("letter_key", desc="All letter keys")
mod.list("symbol_key", desc="All symbol keys")
mod.list("special_key", desc="All special keys")
mod.list("arrow_key", desc="All arrow keys")
mod.list("modifier_key", desc="All modifier keys")
mod.list("function_key", desc="All function keys")


ctx = Context()


def _load_lists():
    for file in KEYMAPS_PATH.iterdir():
        with open(file, "r") as stream:
            stem = file.stem
            list_name = stem if stem[-1] != "s" else stem[:-1]
            ctx.lists[f"user.{list_name}"] = safe_load(stream)


# Letter Key
@mod.capture(rule="{self.letter_key}")
def letter_key(m) -> str:
    "One letter key"
    return m.letter_key


# Number Key
# Exclusively used with "Unmodified Key" capture
@mod.capture(rule="{self.number_key}")
def number_key(m) -> str:
    "One number key"
    return m.number_key


# Symbol Key
@mod.capture(rule="{self.symbol_key}")
def symbol_key(m) -> str:
    "One symbol key"
    return m.symbol_key


# Special Key
@mod.capture(rule="{self.special_key}")
def special_key(m) -> str:
    "One special key"
    return m.special_key


# Arrow Key
@mod.capture(rule="{self.arrow_key}")
def arrow_key(m) -> str:
    "One directional arrow key"
    return m.arrow_key


# Modifier Keys
@mod.capture(rule="{self.modifier_key}+")
def modifier_keys(m) -> str:
    "One or more modifier keys"
    return "-".join(m.modifier_key_list)


# Unmodified Key
@mod.capture(
    rule="( <self.letter_key> | <self.number_key> | <self.symbol_key> "
    "| <self.special_key> | <self.arrow_key> | <self.function_key> )"
)
def unmodified_key(m) -> str:
    "A single key with no modifiers"
    return str(m)


# Function Key
@mod.capture(rule="{self.function_key}")
def function_key(m) -> str:
    "One function key"
    return m.function_key


_load_lists()
