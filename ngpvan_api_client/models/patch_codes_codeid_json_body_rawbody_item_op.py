from enum import Enum


class PatchCodesCodeidJsonBodyRAWBODYItemOp(str, Enum):
    ADD = "add"
    REMOVE = "remove"
    REPLACE = "replace"
    COPY = "copy"
    MOVE = "move"
    TEST = "test"

    def __str__(self) -> str:
        return str(self.value)
