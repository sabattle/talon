from talon import Context, registry, app

ctx = Context()


def _add_keys():
    """
    Put this in a launch listener so it runs after knausj
    """
    special_keys = registry.lists["user.special_key"][0].copy()
    special_keys["del"] = special_keys.pop("delete")
    ctx.lists["self.special_key"] = special_keys


app.register("launch", _add_keys)
