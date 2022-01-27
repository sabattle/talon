from talon import Context

ctx = Context()

ctx.lists["user.letter"] = {
    "air": "a",
    "bat": "b",
    "cap": "c",
    "drum": "d",
    "each": "e",
    "fine": "f",
    "gust": "g",
    "harp": "h",
    "ink": "i",
    "joy": "j",
    "crunch": "k",
    "look": "l",
    "made": "m",
    "near": "n",
    "odd": "o",
    "pit": "p",
    "quench": "q",
    "red": "r",
    "sun": "s",
    "trap": "t",
    "urge": "u",
    "vest": "v",
    "whale": "w",
    "plex": "x",
    "yank": "y",
    "zip": "z",
}

ctx.lists["user.special_key"] = {
    "shock": "enter",
    "escape": "escape",
    "push": "home",
    "pop": "end",
    "insert": "insert",
    "pagedown": "pagedown",
    "page down": "pagedown",
    "pageup": "pageup",
    "page up": "pageup",
    "space": "space",
    "tab": "tab",
    "junk": "backspace",
    "trash": "delete",
}


@ctx.capture("user.letter", rule="{user.letter}")
def letter(m):
    return str(m)


@ctx.capture("user.special_key", rule="{user.special_key}")
def special_key(m):
    return str(m)
