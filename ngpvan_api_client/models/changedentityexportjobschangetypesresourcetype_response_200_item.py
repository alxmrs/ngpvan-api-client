from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ChangedentityexportjobschangetypesresourcetypeResponse200Item")


@attr.s(auto_attribs=True)
class ChangedentityexportjobschangetypesresourcetypeResponse200Item:
    """
    Attributes:
        change_type_id (Union[Unset, str]):  Example: 1.
        change_type_name (Union[Unset, str]):  Example: CreatedOrUpdated.
        description (Union[Unset, str]):  Example: Indicates that the last change to the record was a create or update.
    """

    change_type_id: Union[Unset, str] = UNSET
    change_type_name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        change_type_id = self.change_type_id
        change_type_name = self.change_type_name
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if change_type_id is not UNSET:
            field_dict["ChangeTypeID"] = change_type_id
        if change_type_name is not UNSET:
            field_dict["ChangeTypeName"] = change_type_name
        if description is not UNSET:
            field_dict["Description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        change_type_id = d.pop("ChangeTypeID", UNSET)

        change_type_name = d.pop("ChangeTypeName", UNSET)

        description = d.pop("Description", UNSET)

        changedentityexportjobschangetypesresourcetype_response_200_item = cls(
            change_type_id=change_type_id,
            change_type_name=change_type_name,
            description=description,
        )

        changedentityexportjobschangetypesresourcetype_response_200_item.additional_properties = d
        return changedentityexportjobschangetypesresourcetype_response_200_item

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
