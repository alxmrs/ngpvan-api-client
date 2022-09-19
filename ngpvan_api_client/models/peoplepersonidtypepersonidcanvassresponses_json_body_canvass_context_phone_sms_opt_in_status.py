from enum import Enum


class PeoplepersonidtypepersonidcanvassresponsesJsonBodyCanvassContextPhoneSmsOptInStatus(str, Enum):
    I = "I"
    O = "O"
    U = "U"

    def __str__(self) -> str:
        return str(self.value)
