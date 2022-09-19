from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.put_codes_codeid_json_body_code_type import PutCodesCodeidJsonBodyCodeType
from ..models.put_codes_codeid_json_body_supported_entities import PutCodesCodeidJsonBodySupportedEntities
from ..types import UNSET, Unset

T = TypeVar("T", bound="PutCodesCodeidJsonBody")


@attr.s(auto_attribs=True)
class PutCodesCodeidJsonBody:
    """
    Attributes:
        code_id (int):
        name (str):
        parent_code_id (Union[Unset, int]):
        code_type (Union[Unset, PutCodesCodeidJsonBodyCodeType]): This property cannot change
        supported_entities (Union[Unset, PutCodesCodeidJsonBodySupportedEntities]):
    """

    code_id: int
    name: str
    parent_code_id: Union[Unset, int] = UNSET
    code_type: Union[Unset, PutCodesCodeidJsonBodyCodeType] = UNSET
    supported_entities: Union[Unset, PutCodesCodeidJsonBodySupportedEntities] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code_id = self.code_id
        name = self.name
        parent_code_id = self.parent_code_id
        code_type: Union[Unset, str] = UNSET
        if not isinstance(self.code_type, Unset):
            code_type = self.code_type.value

        supported_entities: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.supported_entities, Unset):
            supported_entities = self.supported_entities.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "codeId": code_id,
                "name": name,
            }
        )
        if parent_code_id is not UNSET:
            field_dict["parentCodeId"] = parent_code_id
        if code_type is not UNSET:
            field_dict["codeType"] = code_type
        if supported_entities is not UNSET:
            field_dict["supportedEntities"] = supported_entities

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code_id = d.pop("codeId")

        name = d.pop("name")

        parent_code_id = d.pop("parentCodeId", UNSET)

        _code_type = d.pop("codeType", UNSET)
        code_type: Union[Unset, PutCodesCodeidJsonBodyCodeType]
        if isinstance(_code_type, Unset):
            code_type = UNSET
        else:
            code_type = PutCodesCodeidJsonBodyCodeType(_code_type)

        _supported_entities = d.pop("supportedEntities", UNSET)
        supported_entities: Union[Unset, PutCodesCodeidJsonBodySupportedEntities]
        if isinstance(_supported_entities, Unset):
            supported_entities = UNSET
        else:
            supported_entities = PutCodesCodeidJsonBodySupportedEntities.from_dict(_supported_entities)

        put_codes_codeid_json_body = cls(
            code_id=code_id,
            name=name,
            parent_code_id=parent_code_id,
            code_type=code_type,
            supported_entities=supported_entities,
        )

        put_codes_codeid_json_body.additional_properties = d
        return put_codes_codeid_json_body

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
