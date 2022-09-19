from enum import Enum


class PeoplepersonidtypepersonidcanvassresponsesJsonBodyResponsesItemAction(str, Enum):
    APPLY = "Apply"
    REMOVE = "Remove"

    def __str__(self) -> str:
        return str(self.value)
