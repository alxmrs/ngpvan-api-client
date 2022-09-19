from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.peoplevanidcanvassresponses_json_body_canvass_context_phone_sms_opt_in_status import (
    PeoplevanidcanvassresponsesJsonBodyCanvassContextPhoneSmsOptInStatus,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevanidcanvassresponsesJsonBodyCanvassContextPhone")


@attr.s(auto_attribs=True)
class PeoplevanidcanvassresponsesJsonBodyCanvassContextPhone:
    """Optional; describes the context of the phone number used to contact the person

    Attributes:
        dialing_prefix (Union[Unset, str]): The country calling code of the number Default: '1'.
        phone_number (Union[Unset, str]): Required when inputTypeId is 1 (Phone) or 37 (SMS); the phone number you are
            using - without calling code/dialing prefix Default: '555-555-1234'.
        sms_opt_in_status (Union[Unset, PeoplevanidcanvassresponsesJsonBodyCanvassContextPhoneSmsOptInStatus]):
            Optional; Must be one of three values: `I` (Opt-In), `O` (Opt-Out), `U` (Unknown)
    """

    dialing_prefix: Union[Unset, str] = "1"
    phone_number: Union[Unset, str] = "555-555-1234"
    sms_opt_in_status: Union[Unset, PeoplevanidcanvassresponsesJsonBodyCanvassContextPhoneSmsOptInStatus] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        dialing_prefix = self.dialing_prefix
        phone_number = self.phone_number
        sms_opt_in_status: Union[Unset, str] = UNSET
        if not isinstance(self.sms_opt_in_status, Unset):
            sms_opt_in_status = self.sms_opt_in_status.value

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if dialing_prefix is not UNSET:
            field_dict["dialingPrefix"] = dialing_prefix
        if phone_number is not UNSET:
            field_dict["phoneNumber"] = phone_number
        if sms_opt_in_status is not UNSET:
            field_dict["smsOptInStatus"] = sms_opt_in_status

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        dialing_prefix = d.pop("dialingPrefix", UNSET)

        phone_number = d.pop("phoneNumber", UNSET)

        _sms_opt_in_status = d.pop("smsOptInStatus", UNSET)
        sms_opt_in_status: Union[Unset, PeoplevanidcanvassresponsesJsonBodyCanvassContextPhoneSmsOptInStatus]
        if isinstance(_sms_opt_in_status, Unset):
            sms_opt_in_status = UNSET
        else:
            sms_opt_in_status = PeoplevanidcanvassresponsesJsonBodyCanvassContextPhoneSmsOptInStatus(_sms_opt_in_status)

        peoplevanidcanvassresponses_json_body_canvass_context_phone = cls(
            dialing_prefix=dialing_prefix,
            phone_number=phone_number,
            sms_opt_in_status=sms_opt_in_status,
        )

        peoplevanidcanvassresponses_json_body_canvass_context_phone.additional_properties = d
        return peoplevanidcanvassresponses_json_body_canvass_context_phone

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
