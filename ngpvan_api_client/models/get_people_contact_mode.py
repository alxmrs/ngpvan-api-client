from enum import Enum


class GetPeopleContactMode(str, Enum):
    PERSON = "Person"
    ORGANIZATION = "Organization"

    def __str__(self) -> str:
        return str(self.value)
