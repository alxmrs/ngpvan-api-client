import datetime
from typing import Any, Dict, List, Type, TypeVar, Union

import attr
from dateutil.parser import isoparse

from ..models.peoplevanidcanvassresponses_json_body_canvass_context_phone import (
    PeoplevanidcanvassresponsesJsonBodyCanvassContextPhone,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevanidcanvassresponsesJsonBodyCanvassContext")


@attr.s(auto_attribs=True)
class PeoplevanidcanvassresponsesJsonBodyCanvassContext:
    """Optional; describes the context in which this Canvass Response was created

    Attributes:
        contact_type_id (Union[Unset, int]): Optional; a valid [Contact Type ID](ref:canvassresponsescontacttypes)
        input_type_id (Union[Unset, int]): Optional; a valid [Input Type ID](ref:canvassresponsesinputtypes)  (defaults
            to `11` → API) Default: 11.
        date_canvassed (Union[Unset, datetime.date]): Optional; the ISO 8601 formatted date that the canvass attempt was
            made (defaults to today’s date)
        phone_id (Union[Unset, int]): Optional; the identifier of the phone number that was called when canvassing this
            person. May result in a phone suppression in the event of certain kinds of Result Codes (e.g., Wrong Number.)
        skip_matching (Union[Unset, bool]): Optional; if set to `true`, skips matching/de-duping of contact history.
            Defaults to a null value, aka `false`.
        omit_activist_code_contact_history (Union[Unset, bool]): Optional; if set to `true`, no contact history record
            will be created if `responses` contains only Activist Codes
        phone (Union[Unset, PeoplevanidcanvassresponsesJsonBodyCanvassContextPhone]): Optional; describes the context of
            the phone number used to contact the person
        campaign_id (Union[Unset, int]): Optional; a valid [Campaign ID](ref:campaigns). Required if `contentId` is also
            specified.
        content_id (Union[Unset, int]): Optional; a valid Content ID. If specified, the Content's corresponding Campaign
            must be specified as `campaignId`.
    """

    contact_type_id: Union[Unset, int] = UNSET
    input_type_id: Union[Unset, int] = 11
    date_canvassed: Union[Unset, datetime.date] = UNSET
    phone_id: Union[Unset, int] = UNSET
    skip_matching: Union[Unset, bool] = UNSET
    omit_activist_code_contact_history: Union[Unset, bool] = UNSET
    phone: Union[Unset, PeoplevanidcanvassresponsesJsonBodyCanvassContextPhone] = UNSET
    campaign_id: Union[Unset, int] = UNSET
    content_id: Union[Unset, int] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        contact_type_id = self.contact_type_id
        input_type_id = self.input_type_id
        date_canvassed: Union[Unset, str] = UNSET
        if not isinstance(self.date_canvassed, Unset):
            date_canvassed = self.date_canvassed.isoformat()

        phone_id = self.phone_id
        skip_matching = self.skip_matching
        omit_activist_code_contact_history = self.omit_activist_code_contact_history
        phone: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.phone, Unset):
            phone = self.phone.to_dict()

        campaign_id = self.campaign_id
        content_id = self.content_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if contact_type_id is not UNSET:
            field_dict["contactTypeId"] = contact_type_id
        if input_type_id is not UNSET:
            field_dict["inputTypeId"] = input_type_id
        if date_canvassed is not UNSET:
            field_dict["dateCanvassed"] = date_canvassed
        if phone_id is not UNSET:
            field_dict["phoneId"] = phone_id
        if skip_matching is not UNSET:
            field_dict["skipMatching"] = skip_matching
        if omit_activist_code_contact_history is not UNSET:
            field_dict["omitActivistCodeContactHistory"] = omit_activist_code_contact_history
        if phone is not UNSET:
            field_dict["phone"] = phone
        if campaign_id is not UNSET:
            field_dict["campaignId"] = campaign_id
        if content_id is not UNSET:
            field_dict["contentId"] = content_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        contact_type_id = d.pop("contactTypeId", UNSET)

        input_type_id = d.pop("inputTypeId", UNSET)

        _date_canvassed = d.pop("dateCanvassed", UNSET)
        date_canvassed: Union[Unset, datetime.date]
        if isinstance(_date_canvassed, Unset):
            date_canvassed = UNSET
        else:
            date_canvassed = isoparse(_date_canvassed).date()

        phone_id = d.pop("phoneId", UNSET)

        skip_matching = d.pop("skipMatching", UNSET)

        omit_activist_code_contact_history = d.pop("omitActivistCodeContactHistory", UNSET)

        _phone = d.pop("phone", UNSET)
        phone: Union[Unset, PeoplevanidcanvassresponsesJsonBodyCanvassContextPhone]
        if isinstance(_phone, Unset):
            phone = UNSET
        else:
            phone = PeoplevanidcanvassresponsesJsonBodyCanvassContextPhone.from_dict(_phone)

        campaign_id = d.pop("campaignId", UNSET)

        content_id = d.pop("contentId", UNSET)

        peoplevanidcanvassresponses_json_body_canvass_context = cls(
            contact_type_id=contact_type_id,
            input_type_id=input_type_id,
            date_canvassed=date_canvassed,
            phone_id=phone_id,
            skip_matching=skip_matching,
            omit_activist_code_contact_history=omit_activist_code_contact_history,
            phone=phone,
            campaign_id=campaign_id,
            content_id=content_id,
        )

        peoplevanidcanvassresponses_json_body_canvass_context.additional_properties = d
        return peoplevanidcanvassresponses_json_body_canvass_context

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
