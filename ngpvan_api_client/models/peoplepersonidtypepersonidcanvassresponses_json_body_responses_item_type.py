from enum import Enum


class PeoplepersonidtypepersonidcanvassresponsesJsonBodyResponsesItemType(str, Enum):
    ACTIVISTCODE = "ActivistCode"
    SURVEYRESPONSE = "SurveyResponse"
    VOLUNTEERACTIVITY = "VolunteerActivity"

    def __str__(self) -> str:
        return str(self.value)
