from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="ReportedsexualorientationsResponse200ItemsItem")


@attr.s(auto_attribs=True)
class ReportedsexualorientationsResponse200ItemsItem:
    """
    Attributes:
        reported_sexual_orientation_id (Union[Unset, int]):  Example: 2.
        reported_sexual_orientation_name (Union[Unset, str]):  Example: Androsexual.
    """

    reported_sexual_orientation_id: Union[Unset, int] = 0
    reported_sexual_orientation_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        reported_sexual_orientation_id = self.reported_sexual_orientation_id
        reported_sexual_orientation_name = self.reported_sexual_orientation_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if reported_sexual_orientation_id is not UNSET:
            field_dict["reportedSexualOrientationId"] = reported_sexual_orientation_id
        if reported_sexual_orientation_name is not UNSET:
            field_dict["reportedSexualOrientationName"] = reported_sexual_orientation_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        reported_sexual_orientation_id = d.pop("reportedSexualOrientationId", UNSET)

        reported_sexual_orientation_name = d.pop("reportedSexualOrientationName", UNSET)

        reportedsexualorientations_response_200_items_item = cls(
            reported_sexual_orientation_id=reported_sexual_orientation_id,
            reported_sexual_orientation_name=reported_sexual_orientation_name,
        )

        reportedsexualorientations_response_200_items_item.additional_properties = d
        return reportedsexualorientations_response_200_items_item

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
