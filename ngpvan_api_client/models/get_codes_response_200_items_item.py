from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_codes_response_200_items_item_supported_entities_item import (
    GetCodesResponse200ItemsItemSupportedEntitiesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetCodesResponse200ItemsItem")


@attr.s(auto_attribs=True)
class GetCodesResponse200ItemsItem:
    """
    Attributes:
        code_id (Union[Unset, int]):  Example: 20515.
        parent_code_id (Union[Unset, int]):  Example: 20513.
        name (Union[Unset, str]):  Example: Labor.
        code_type (Union[Unset, str]):  Example: Tag.
        date_created (Union[Unset, str]):  Example: 2015-04-05T12:59:00Z.
        date_modified (Union[Unset, str]):  Example: 2015-05-01T09:59:00Z.
        supported_entities (Union[Unset, List[GetCodesResponse200ItemsItemSupportedEntitiesItem]]):
    """

    code_id: Union[Unset, int] = 0
    parent_code_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    code_type: Union[Unset, str] = UNSET
    date_created: Union[Unset, str] = UNSET
    date_modified: Union[Unset, str] = UNSET
    supported_entities: Union[Unset, List[GetCodesResponse200ItemsItemSupportedEntitiesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code_id = self.code_id
        parent_code_id = self.parent_code_id
        name = self.name
        code_type = self.code_type
        date_created = self.date_created
        date_modified = self.date_modified
        supported_entities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.supported_entities, Unset):
            supported_entities = []
            for supported_entities_item_data in self.supported_entities:
                supported_entities_item = supported_entities_item_data.to_dict()

                supported_entities.append(supported_entities_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code_id is not UNSET:
            field_dict["codeId"] = code_id
        if parent_code_id is not UNSET:
            field_dict["parentCodeId"] = parent_code_id
        if name is not UNSET:
            field_dict["name"] = name
        if code_type is not UNSET:
            field_dict["codeType"] = code_type
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if date_modified is not UNSET:
            field_dict["dateModified"] = date_modified
        if supported_entities is not UNSET:
            field_dict["supportedEntities"] = supported_entities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code_id = d.pop("codeId", UNSET)

        parent_code_id = d.pop("parentCodeId", UNSET)

        name = d.pop("name", UNSET)

        code_type = d.pop("codeType", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        date_modified = d.pop("dateModified", UNSET)

        supported_entities = []
        _supported_entities = d.pop("supportedEntities", UNSET)
        for supported_entities_item_data in _supported_entities or []:
            supported_entities_item = GetCodesResponse200ItemsItemSupportedEntitiesItem.from_dict(
                supported_entities_item_data
            )

            supported_entities.append(supported_entities_item)

        get_codes_response_200_items_item = cls(
            code_id=code_id,
            parent_code_id=parent_code_id,
            name=name,
            code_type=code_type,
            date_created=date_created,
            date_modified=date_modified,
            supported_entities=supported_entities,
        )

        get_codes_response_200_items_item.additional_properties = d
        return get_codes_response_200_items_item

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
