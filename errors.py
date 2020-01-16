__all__ = ("RollError", "RollSyntaxError", "TooManyRolls")


class RollError(Exception):
    """Generic exception happened in the roll."""

    def __init__(self, msg):
        super().__init__(msg)


class RollSyntaxError(RollError):
    """Syntax error happened while parsing roll."""

    def __init__(self, msg, line, col):
        super().__init__(msg)
        self.line = line
        self.col = col


class TooManyRolls(RollError):
    """Too many dice rolled (in an individual dice or in rerolls)."""
    pass