from enum import Enum


class PostCodesJsonBodyCodeType(str, Enum):
    SOURCECODE = "SourceCode"
    TAG = "Tag"

    def __str__(self) -> str:
        return str(self.value)
