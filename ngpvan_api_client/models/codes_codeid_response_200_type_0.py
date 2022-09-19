from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodesCodeidResponse200Type0")


@attr.s(auto_attribs=True)
class CodesCodeidResponse200Type0:
    """
    Attributes:
        code_id (Union[Unset, int]):  Example: 20548.
        parent_code_id (Union[Unset, Any]):
        name (Union[Unset, str]):  Example: Digital ads.
        description (Union[Unset, str]):  Example: Used to mark people and contributions retrieved because of digital ad
            campaigns.
        code_type (Union[Unset, str]):  Example: SourceCode.
        date_created (Union[Unset, str]):  Example: 2017-10-05T12:59:00Z.
        date_modified (Union[Unset, str]):  Example: 2017-10-08T12:00:00Z.
        supported_entities (Union[Unset, Any]):
    """

    code_id: Union[Unset, int] = 0
    parent_code_id: Union[Unset, Any] = UNSET
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    code_type: Union[Unset, str] = UNSET
    date_created: Union[Unset, str] = UNSET
    date_modified: Union[Unset, str] = UNSET
    supported_entities: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code_id = self.code_id
        parent_code_id = self.parent_code_id
        name = self.name
        description = self.description
        code_type = self.code_type
        date_created = self.date_created
        date_modified = self.date_modified
        supported_entities = self.supported_entities

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code_id is not UNSET:
            field_dict["codeId"] = code_id
        if parent_code_id is not UNSET:
            field_dict["parentCodeId"] = parent_code_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
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

        description = d.pop("description", UNSET)

        code_type = d.pop("codeType", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        date_modified = d.pop("dateModified", UNSET)

        supported_entities = d.pop("supportedEntities", UNSET)

        codes_codeid_response_200_type_0 = cls(
            code_id=code_id,
            parent_code_id=parent_code_id,
            name=name,
            description=description,
            code_type=code_type,
            date_created=date_created,
            date_modified=date_modified,
            supported_entities=supported_entities,
        )

        codes_codeid_response_200_type_0.additional_properties = d
        return codes_codeid_response_200_type_0

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
