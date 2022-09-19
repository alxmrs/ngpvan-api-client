from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.post_codes_json_body_code_type import PostCodesJsonBodyCodeType
from ..models.post_codes_json_body_supported_entities_item import PostCodesJsonBodySupportedEntitiesItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="PostCodesJsonBody")


@attr.s(auto_attribs=True)
class PostCodesJsonBody:
    """
    Attributes:
        name (str):
        parent_code_id (Union[Unset, int]):
        code_type (Union[Unset, PostCodesJsonBodyCodeType]): Defaults to `SourceCode` if not specified
        supported_entities (Union[Unset, List[PostCodesJsonBodySupportedEntitiesItem]]): Only relevant for `codeType`
            `Tag`. Use `isSourceCodeApplicable` for `SourceCode`.
        is_source_code_applicable (Union[Unset, bool]): Only relevant for `codeType` `SourceCode`
        description (Union[Unset, str]):
    """

    name: str
    parent_code_id: Union[Unset, int] = UNSET
    code_type: Union[Unset, PostCodesJsonBodyCodeType] = UNSET
    supported_entities: Union[Unset, List[PostCodesJsonBodySupportedEntitiesItem]] = UNSET
    is_source_code_applicable: Union[Unset, bool] = UNSET
    description: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        parent_code_id = self.parent_code_id
        code_type: Union[Unset, str] = UNSET
        if not isinstance(self.code_type, Unset):
            code_type = self.code_type.value

        supported_entities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.supported_entities, Unset):
            supported_entities = []
            for supported_entities_item_data in self.supported_entities:
                supported_entities_item = supported_entities_item_data.to_dict()

                supported_entities.append(supported_entities_item)

        is_source_code_applicable = self.is_source_code_applicable
        description = self.description

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "name": name,
            }
        )
        if parent_code_id is not UNSET:
            field_dict["parentCodeId"] = parent_code_id
        if code_type is not UNSET:
            field_dict["codeType"] = code_type
        if supported_entities is not UNSET:
            field_dict["supportedEntities"] = supported_entities
        if is_source_code_applicable is not UNSET:
            field_dict["isSourceCodeApplicable"] = is_source_code_applicable
        if description is not UNSET:
            field_dict["description"] = description

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name")

        parent_code_id = d.pop("parentCodeId", UNSET)

        _code_type = d.pop("codeType", UNSET)
        code_type: Union[Unset, PostCodesJsonBodyCodeType]
        if isinstance(_code_type, Unset):
            code_type = UNSET
        else:
            code_type = PostCodesJsonBodyCodeType(_code_type)

        supported_entities = []
        _supported_entities = d.pop("supportedEntities", UNSET)
        for supported_entities_item_data in _supported_entities or []:
            supported_entities_item = PostCodesJsonBodySupportedEntitiesItem.from_dict(supported_entities_item_data)

            supported_entities.append(supported_entities_item)

        is_source_code_applicable = d.pop("isSourceCodeApplicable", UNSET)

        description = d.pop("description", UNSET)

        post_codes_json_body = cls(
            name=name,
            parent_code_id=parent_code_id,
            code_type=code_type,
            supported_entities=supported_entities,
            is_source_code_applicable=is_source_code_applicable,
            description=description,
        )

        post_codes_json_body.additional_properties = d
        return post_codes_json_body

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
