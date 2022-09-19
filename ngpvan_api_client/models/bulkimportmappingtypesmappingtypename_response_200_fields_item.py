from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkimportmappingtypesmappingtypenameResponse200FieldsItem")


@attr.s(auto_attribs=True)
class BulkimportmappingtypesmappingtypenameResponse200FieldsItem:
    """
    Attributes:
        name (Union[Unset, str]):  Example: MailingAddress.
        description (Union[Unset, str]):  Example: Address Line 1.
        has_predefined_values (Union[Unset, bool]):  Default: True.
        is_required (Union[Unset, bool]):  Default: True.
        can_be_mapped_to_column (Union[Unset, bool]):  Default: True. Example: True.
        parents (Union[Unset, Any]):
    """

    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    has_predefined_values: Union[Unset, bool] = True
    is_required: Union[Unset, bool] = True
    can_be_mapped_to_column: Union[Unset, bool] = True
    parents: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        has_predefined_values = self.has_predefined_values
        is_required = self.is_required
        can_be_mapped_to_column = self.can_be_mapped_to_column
        parents = self.parents

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if has_predefined_values is not UNSET:
            field_dict["hasPredefinedValues"] = has_predefined_values
        if is_required is not UNSET:
            field_dict["isRequired"] = is_required
        if can_be_mapped_to_column is not UNSET:
            field_dict["canBeMappedToColumn"] = can_be_mapped_to_column
        if parents is not UNSET:
            field_dict["parents"] = parents

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        has_predefined_values = d.pop("hasPredefinedValues", UNSET)

        is_required = d.pop("isRequired", UNSET)

        can_be_mapped_to_column = d.pop("canBeMappedToColumn", UNSET)

        parents = d.pop("parents", UNSET)

        bulkimportmappingtypesmappingtypename_response_200_fields_item = cls(
            name=name,
            description=description,
            has_predefined_values=has_predefined_values,
            is_required=is_required,
            can_be_mapped_to_column=can_be_mapped_to_column,
            parents=parents,
        )

        bulkimportmappingtypesmappingtypename_response_200_fields_item.additional_properties = d
        return bulkimportmappingtypesmappingtypename_response_200_fields_item

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
