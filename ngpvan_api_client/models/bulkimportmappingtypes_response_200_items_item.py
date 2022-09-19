from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.bulkimportmappingtypes_response_200_items_item_fields_item import (
    BulkimportmappingtypesResponse200ItemsItemFieldsItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="BulkimportmappingtypesResponse200ItemsItem")


@attr.s(auto_attribs=True)
class BulkimportmappingtypesResponse200ItemsItem:
    """
    Attributes:
        name (Union[Unset, str]):  Example: MailingAddress.
        display_name (Union[Unset, str]):  Example: Apply Mailing Address.
        upload_type (Union[Unset, Any]):
        allow_multiple_mode (Union[Unset, str]):  Example: Single.
        resource_types (Union[Unset, List[str]]):
        fields (Union[Unset, List[BulkimportmappingtypesResponse200ItemsItemFieldsItem]]):
    """

    name: Union[Unset, str] = UNSET
    display_name: Union[Unset, str] = UNSET
    upload_type: Union[Unset, Any] = UNSET
    allow_multiple_mode: Union[Unset, str] = UNSET
    resource_types: Union[Unset, List[str]] = UNSET
    fields: Union[Unset, List[BulkimportmappingtypesResponse200ItemsItemFieldsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        display_name = self.display_name
        upload_type = self.upload_type
        allow_multiple_mode = self.allow_multiple_mode
        resource_types: Union[Unset, List[str]] = UNSET
        if not isinstance(self.resource_types, Unset):
            resource_types = self.resource_types

        fields: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.fields, Unset):
            fields = []
            for fields_item_data in self.fields:
                fields_item = fields_item_data.to_dict()

                fields.append(fields_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if display_name is not UNSET:
            field_dict["displayName"] = display_name
        if upload_type is not UNSET:
            field_dict["uploadType"] = upload_type
        if allow_multiple_mode is not UNSET:
            field_dict["allowMultipleMode"] = allow_multiple_mode
        if resource_types is not UNSET:
            field_dict["resourceTypes"] = resource_types
        if fields is not UNSET:
            field_dict["fields"] = fields

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        display_name = d.pop("displayName", UNSET)

        upload_type = d.pop("uploadType", UNSET)

        allow_multiple_mode = d.pop("allowMultipleMode", UNSET)

        resource_types = cast(List[str], d.pop("resourceTypes", UNSET))

        fields = []
        _fields = d.pop("fields", UNSET)
        for fields_item_data in _fields or []:
            fields_item = BulkimportmappingtypesResponse200ItemsItemFieldsItem.from_dict(fields_item_data)

            fields.append(fields_item)

        bulkimportmappingtypes_response_200_items_item = cls(
            name=name,
            display_name=display_name,
            upload_type=upload_type,
            allow_multiple_mode=allow_multiple_mode,
            resource_types=resource_types,
            fields=fields,
        )

        bulkimportmappingtypes_response_200_items_item.additional_properties = d
        return bulkimportmappingtypes_response_200_items_item

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
