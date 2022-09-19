from enum import Enum


class PutCodesCodeidJsonBodyCodeType(str, Enum):
    SOURCECODE = "SourceCode"
    TAG = "Tag"

    def __str__(self) -> str:
        return str(self.value)
