from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.put_codes_json_body_codes_item_supported_entities_item import (
    PutCodesJsonBodyCodesItemSupportedEntitiesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutCodesJsonBodyCodesItem")


@attr.s(auto_attribs=True)
class PutCodesJsonBodyCodesItem:
    """
    Attributes:
        parent_code_id (Union[Unset, int]):  Default: 1002316.
        name (Union[Unset, str]):  Default: 'Labor'.
        description (Union[Unset, str]):  Default: 'The tag for describing Labor'.
        supported_entities (Union[Unset, List[PutCodesJsonBodyCodesItemSupportedEntitiesItem]]):
        code_type (Union[Unset, str]):  Default: 'Tag'.
    """

    parent_code_id: Union[Unset, int] = 1002316
    name: Union[Unset, str] = "Labor"
    description: Union[Unset, str] = "The tag for describing Labor"
    supported_entities: Union[Unset, List[PutCodesJsonBodyCodesItemSupportedEntitiesItem]] = UNSET
    code_type: Union[Unset, str] = "Tag"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        parent_code_id = self.parent_code_id
        name = self.name
        description = self.description
        supported_entities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.supported_entities, Unset):
            supported_entities = []
            for supported_entities_item_data in self.supported_entities:
                supported_entities_item = supported_entities_item_data.to_dict()

                supported_entities.append(supported_entities_item)

        code_type = self.code_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if parent_code_id is not UNSET:
            field_dict["parentCodeId"] = parent_code_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if supported_entities is not UNSET:
            field_dict["supportedEntities"] = supported_entities
        if code_type is not UNSET:
            field_dict["codeType"] = code_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        parent_code_id = d.pop("parentCodeId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        supported_entities = []
        _supported_entities = d.pop("supportedEntities", UNSET)
        for supported_entities_item_data in _supported_entities or []:
            supported_entities_item = PutCodesJsonBodyCodesItemSupportedEntitiesItem.from_dict(
                supported_entities_item_data
            )

            supported_entities.append(supported_entities_item)

        code_type = d.pop("codeType", UNSET)

        put_codes_json_body_codes_item = cls(
            parent_code_id=parent_code_id,
            name=name,
            description=description,
            supported_entities=supported_entities,
            code_type=code_type,
        )

        put_codes_json_body_codes_item.additional_properties = d
        return put_codes_json_body_codes_item

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
