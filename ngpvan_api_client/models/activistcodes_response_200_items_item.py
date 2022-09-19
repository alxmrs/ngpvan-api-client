from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ActivistcodesResponse200ItemsItem")


@attr.s(auto_attribs=True)
class ActivistcodesResponse200ItemsItem:
    """
    Attributes:
        activist_code_id (Union[Unset, int]):  Example: 3214.
        type (Union[Unset, str]):  Example: Volunteer.
        name (Union[Unset, str]):  Example: Precinct Captain.
        medium_name (Union[Unset, str]):  Example: P Capt.
        short_name (Union[Unset, str]):  Example: PC.
        description (Union[Unset, str]):  Example: Precinct Captain.
        script_question (Union[Unset, str]):  Example: Would you be willing to be a Precinct Captain?.
        status (Union[Unset, str]):  Example: Active.
    """

    activist_code_id: Union[Unset, int] = 0
    type: Union[Unset, str] = UNSET
    name: Union[Unset, str] = UNSET
    medium_name: Union[Unset, str] = UNSET
    short_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    script_question: Union[Unset, str] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        activist_code_id = self.activist_code_id
        type = self.type
        name = self.name
        medium_name = self.medium_name
        short_name = self.short_name
        description = self.description
        script_question = self.script_question
        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if activist_code_id is not UNSET:
            field_dict["activistCodeId"] = activist_code_id
        if type is not UNSET:
            field_dict["type"] = type
        if name is not UNSET:
            field_dict["name"] = name
        if medium_name is not UNSET:
            field_dict["mediumName"] = medium_name
        if short_name is not UNSET:
            field_dict["shortName"] = short_name
        if description is not UNSET:
            field_dict["description"] = description
        if script_question is not UNSET:
            field_dict["scriptQuestion"] = script_question
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        activist_code_id = d.pop("activistCodeId", UNSET)

        type = d.pop("type", UNSET)

        name = d.pop("name", UNSET)

        medium_name = d.pop("mediumName", UNSET)

        short_name = d.pop("shortName", UNSET)

        description = d.pop("description", UNSET)

        script_question = d.pop("scriptQuestion", UNSET)

        status = d.pop("status", UNSET)

        activistcodes_response_200_items_item = cls(
            activist_code_id=activist_code_id,
            type=type,
            name=name,
            medium_name=medium_name,
            short_name=short_name,
            description=description,
            script_question=script_question,
            status=status,
        )

        activistcodes_response_200_items_item.additional_properties = d
        return activistcodes_response_200_items_item

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
