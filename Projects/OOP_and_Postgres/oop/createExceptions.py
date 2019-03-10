class MissingLabelError(KeyError):
    pass

class PageFoundFoundError(LookupError):
    pass

class IncorrectPasswordError(ValueError):
    pass

class IncorrectUsernameError(ValueError):
    pass

class APIThrottleLimitError(RuntimeError):
    pass
