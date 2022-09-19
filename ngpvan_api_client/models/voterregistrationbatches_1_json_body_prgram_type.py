from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Voterregistrationbatches1JsonBodyPrgramType")


@attr.s(auto_attribs=True)
class Voterregistrationbatches1JsonBodyPrgramType:
    """
    Attributes:
        program_type_id (Union[Unset, int]):  Default: 201.
    """

    program_type_id: Union[Unset, int] = 201
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        program_type_id = self.program_type_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if program_type_id is not UNSET:
            field_dict["programTypeId"] = program_type_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        program_type_id = d.pop("programTypeId", UNSET)

        voterregistrationbatches_1_json_body_prgram_type = cls(
            program_type_id=program_type_id,
        )

        voterregistrationbatches_1_json_body_prgram_type.additional_properties = d
        return voterregistrationbatches_1_json_body_prgram_type

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
