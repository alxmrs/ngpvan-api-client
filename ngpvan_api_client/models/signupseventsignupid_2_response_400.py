from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.signupseventsignupid_2_response_400_errors_item import Signupseventsignupid2Response400ErrorsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="Signupseventsignupid2Response400")


@attr.s(auto_attribs=True)
class Signupseventsignupid2Response400:
    """
    Attributes:
        errors (Union[Unset, List[Signupseventsignupid2Response400ErrorsItem]]):
    """

    errors: Union[Unset, List[Signupseventsignupid2Response400ErrorsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()

                errors.append(errors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = Signupseventsignupid2Response400ErrorsItem.from_dict(errors_item_data)

            errors.append(errors_item)

        signupseventsignupid_2_response_400 = cls(
            errors=errors,
        )

        signupseventsignupid_2_response_400.additional_properties = d
        return signupseventsignupid_2_response_400

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
