go <user.arrow_keys>: key(arrow_keys)
<user.letter_key>: key(letter_key)
(ship | uppercase) <user.letter_keys> [(lowercase | sunk)]:
    user.insert_formatted(letter_keys, "ALL_CAPS")
<user.symbol_key>: key(symbol_key)
<user.function_key>: key(function_key)
<user.special_key>: key(special_key)
<user.modifiers> <user.unmodified_key>: key("{modifiers}-{unmodified_key}")
press <user.modifiers>: key(modifiers)
