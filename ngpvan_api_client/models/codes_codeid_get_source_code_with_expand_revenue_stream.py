from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.codes_codeid_get_source_code_with_expand_revenue_stream_type import (
    CodesCodeidGetSourceCodeWithExpandRevenueStreamType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodesCodeidGetSourceCodeWithExpandRevenueStream")


@attr.s(auto_attribs=True)
class CodesCodeidGetSourceCodeWithExpandRevenueStream:
    """
    Attributes:
        revenue_stream_id (Union[Unset, int]):  Example: 179.
        name (Union[Unset, str]):  Example: API Revenue Stream for Source Codes.
        type (Union[Unset, CodesCodeidGetSourceCodeWithExpandRevenueStreamType]):
        status (Union[Unset, str]):  Example: Active.
    """

    revenue_stream_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    type: Union[Unset, CodesCodeidGetSourceCodeWithExpandRevenueStreamType] = UNSET
    status: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        revenue_stream_id = self.revenue_stream_id
        name = self.name
        type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.to_dict()

        status = self.status

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if revenue_stream_id is not UNSET:
            field_dict["revenueStreamId"] = revenue_stream_id
        if name is not UNSET:
            field_dict["name"] = name
        if type is not UNSET:
            field_dict["type"] = type
        if status is not UNSET:
            field_dict["status"] = status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        revenue_stream_id = d.pop("revenueStreamId", UNSET)

        name = d.pop("name", UNSET)

        _type = d.pop("type", UNSET)
        type: Union[Unset, CodesCodeidGetSourceCodeWithExpandRevenueStreamType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = CodesCodeidGetSourceCodeWithExpandRevenueStreamType.from_dict(_type)

        status = d.pop("status", UNSET)

        codes_codeid_get_source_code_with_expand_revenue_stream = cls(
            revenue_stream_id=revenue_stream_id,
            name=name,
            type=type,
            status=status,
        )

        codes_codeid_get_source_code_with_expand_revenue_stream.additional_properties = d
        return codes_codeid_get_source_code_with_expand_revenue_stream

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
