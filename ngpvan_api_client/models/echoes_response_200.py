from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="EchoesResponse200")


@attr.s(auto_attribs=True)
class EchoesResponse200:
    """
    Attributes:
        message (Union[Unset, str]):  Example: Hello, world.
        date_sent (Union[Unset, str]):  Example: 2021-01-01T00:00:00Z.
        delay_in_milliseconds (Union[Unset, Any]):
    """

    message: Union[Unset, str] = UNSET
    date_sent: Union[Unset, str] = UNSET
    delay_in_milliseconds: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        message = self.message
        date_sent = self.date_sent
        delay_in_milliseconds = self.delay_in_milliseconds

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if message is not UNSET:
            field_dict["message"] = message
        if date_sent is not UNSET:
            field_dict["dateSent"] = date_sent
        if delay_in_milliseconds is not UNSET:
            field_dict["delayInMilliseconds"] = delay_in_milliseconds

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        message = d.pop("message", UNSET)

        date_sent = d.pop("dateSent", UNSET)

        delay_in_milliseconds = d.pop("delayInMilliseconds", UNSET)

        echoes_response_200 = cls(
            message=message,
            date_sent=date_sent,
            delay_in_milliseconds=delay_in_milliseconds,
        )

        echoes_response_200.additional_properties = d
        return echoes_response_200

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
