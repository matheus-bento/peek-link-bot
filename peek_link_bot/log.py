from enum import Enum

class LoggingLevel(Enum):
    ERROR = 0
    WARNING = 1
    INFO = 2

def log(message, level):
    """
    Receives the message and logs it to stdout
    """

    level_tag = ""

    if (level == LoggingLevel.ERROR):
        level_tag = "(ERROR) "
    elif (level == LoggingLevel.WARNING):
        level_tag = "(WARNING) "
    else:
        level_tag = "(INFO) "

    print(level_tag + message)