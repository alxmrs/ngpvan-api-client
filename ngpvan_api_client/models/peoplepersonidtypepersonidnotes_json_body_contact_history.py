import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplepersonidtypepersonidnotesJsonBodyContactHistory")


@attr.s(auto_attribs=True)
class PeoplepersonidtypepersonidnotesJsonBodyContactHistory:
    """
    Attributes:
        contact_type_id (Union[Unset, str]): Optional; a valid [Contact Type
            ID](https://everyaction.readme.io/reference#canvassresponsescontacttypes) Default: '82'.
        input_type_id (Union[Unset, str]): Optional; a valid [Input Type
            ID](https://everyaction.readme.io/reference#canvassresponsesinputtypes) (defaults to `11` → API) Default: '11'.
        date_canvassed (Union[Unset, datetime.date]): Optional; the [ISO 8601](http://en.wikipedia.org/wiki/ISO_8601)
            formatted date that the canvass attempt was made (defaults to today’s date) Default:
            isoparse('2020-01-09T15:24:18Z').date().
        result_code_id (Union[Unset, str]): Optional; specifies the [Result
            Code](https://everyaction.readme.io/reference#canvassresponsesresultcodes) of this Contact History. If no
            `resultCodeId` is specified, a result of *Canvassed* is applied. The `resultCodeId` must be a valid [Result
            Code](https://everyaction.readme.io/reference#canvassresponsesresultcodes) in the current context. Default:
            '205'.
    """

    contact_type_id: Union[Unset, str] = "82"
    input_type_id: Union[Unset, str] = "11"
    date_canvassed: Union[Unset, datetime.date] = isoparse("2020-01-09T15:24:18Z").date()
    result_code_id: Union[Unset, str] = "205"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact_type_id = self.contact_type_id
        input_type_id = self.input_type_id
        date_canvassed: Union[Unset, str] = UNSET
        if not isinstance(self.date_canvassed, Unset):
            date_canvassed = self.date_canvassed.isoformat()

        result_code_id = self.result_code_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact_type_id is not UNSET:
            field_dict["contactTypeId"] = contact_type_id
        if input_type_id is not UNSET:
            field_dict["inputTypeId"] = input_type_id
        if date_canvassed is not UNSET:
            field_dict["dateCanvassed"] = date_canvassed
        if result_code_id is not UNSET:
            field_dict["resultCodeId"] = result_code_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contact_type_id = d.pop("contactTypeId", UNSET)

        input_type_id = d.pop("inputTypeId", UNSET)

        _date_canvassed = d.pop("dateCanvassed", UNSET)
        date_canvassed: Union[Unset, datetime.date]
        if isinstance(_date_canvassed, Unset):
            date_canvassed = UNSET
        else:
            date_canvassed = isoparse(_date_canvassed).date()

        result_code_id = d.pop("resultCodeId", UNSET)

        peoplepersonidtypepersonidnotes_json_body_contact_history = cls(
            contact_type_id=contact_type_id,
            input_type_id=input_type_id,
            date_canvassed=date_canvassed,
            result_code_id=result_code_id,
        )

        peoplepersonidtypepersonidnotes_json_body_contact_history.additional_properties = d
        return peoplepersonidtypepersonidnotes_json_body_contact_history

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
