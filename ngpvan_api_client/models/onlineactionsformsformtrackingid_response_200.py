from typing import Any, Dict, List, Type, TypeVar, Union, cast

import attr

from ..models.onlineactionsformsformtrackingid_response_200_confirmation_email_data import (
    OnlineactionsformsformtrackingidResponse200ConfirmationEmailData,
)
from ..models.onlineactionsformsformtrackingid_response_200_designation import (
    OnlineactionsformsformtrackingidResponse200Designation,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="OnlineactionsformsformtrackingidResponse200")


@attr.s(auto_attribs=True)
class OnlineactionsformsformtrackingidResponse200:
    """
    Attributes:
        form_tracking_id (Union[Unset, str]):  Example: j_STKe8rYxkEVvg2.
        form_name (Union[Unset, str]):  Example: My Event Form.
        form_type (Union[Unset, str]):  Example: EventSignupForm.
        form_type_id (Union[Unset, int]):  Example: 11.
        date_created (Union[Unset, str]):  Example: 2019-12-09T00:09:00Z.
        created_by_email (Union[Unset, str]):  Example: invalid@fake.ngpvan.com.
        date_modified (Union[Unset, str]):  Example: 2019-12-11T03:47:00Z.
        modified_by_email (Union[Unset, str]):  Example: invalid@fake.ngpvan.com.
        is_active (Union[Unset, bool]):  Default: True. Example: True.
        designation (Union[Unset, OnlineactionsformsformtrackingidResponse200Designation]):
        confirmation_email_data (Union[Unset, OnlineactionsformsformtrackingidResponse200ConfirmationEmailData]):
        activist_codes (Union[Unset, List[int]]):
        event_id (Union[Unset, int]):  Example: 123456.
        code_id (Union[Unset, Any]):
        campaign_id (Union[Unset, int]):  Example: 7777.
        is_confirmed_opt_in_enabled (Union[Unset, bool]):  Default: True.
    """

    form_tracking_id: Union[Unset, str] = UNSET
    form_name: Union[Unset, str] = UNSET
    form_type: Union[Unset, str] = UNSET
    form_type_id: Union[Unset, int] = 0
    date_created: Union[Unset, str] = UNSET
    created_by_email: Union[Unset, str] = UNSET
    date_modified: Union[Unset, str] = UNSET
    modified_by_email: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = True
    designation: Union[Unset, OnlineactionsformsformtrackingidResponse200Designation] = UNSET
    confirmation_email_data: Union[Unset, OnlineactionsformsformtrackingidResponse200ConfirmationEmailData] = UNSET
    activist_codes: Union[Unset, List[int]] = UNSET
    event_id: Union[Unset, int] = 0
    code_id: Union[Unset, Any] = UNSET
    campaign_id: Union[Unset, int] = 0
    is_confirmed_opt_in_enabled: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        form_tracking_id = self.form_tracking_id
        form_name = self.form_name
        form_type = self.form_type
        form_type_id = self.form_type_id
        date_created = self.date_created
        created_by_email = self.created_by_email
        date_modified = self.date_modified
        modified_by_email = self.modified_by_email
        is_active = self.is_active
        designation: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.designation, Unset):
            designation = self.designation.to_dict()

        confirmation_email_data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.confirmation_email_data, Unset):
            confirmation_email_data = self.confirmation_email_data.to_dict()

        activist_codes: Union[Unset, List[int]] = UNSET
        if not isinstance(self.activist_codes, Unset):
            activist_codes = self.activist_codes

        event_id = self.event_id
        code_id = self.code_id
        campaign_id = self.campaign_id
        is_confirmed_opt_in_enabled = self.is_confirmed_opt_in_enabled

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if form_tracking_id is not UNSET:
            field_dict["formTrackingId"] = form_tracking_id
        if form_name is not UNSET:
            field_dict["formName"] = form_name
        if form_type is not UNSET:
            field_dict["formType"] = form_type
        if form_type_id is not UNSET:
            field_dict["formTypeId"] = form_type_id
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if created_by_email is not UNSET:
            field_dict["createdByEmail"] = created_by_email
        if date_modified is not UNSET:
            field_dict["dateModified"] = date_modified
        if modified_by_email is not UNSET:
            field_dict["modifiedByEmail"] = modified_by_email
        if is_active is not UNSET:
            field_dict["isActive"] = is_active
        if designation is not UNSET:
            field_dict["designation"] = designation
        if confirmation_email_data is not UNSET:
            field_dict["confirmationEmailData"] = confirmation_email_data
        if activist_codes is not UNSET:
            field_dict["activistCodes"] = activist_codes
        if event_id is not UNSET:
            field_dict["eventId"] = event_id
        if code_id is not UNSET:
            field_dict["codeId"] = code_id
        if campaign_id is not UNSET:
            field_dict["campaignId"] = campaign_id
        if is_confirmed_opt_in_enabled is not UNSET:
            field_dict["isConfirmedOptInEnabled"] = is_confirmed_opt_in_enabled

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        form_tracking_id = d.pop("formTrackingId", UNSET)

        form_name = d.pop("formName", UNSET)

        form_type = d.pop("formType", UNSET)

        form_type_id = d.pop("formTypeId", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        created_by_email = d.pop("createdByEmail", UNSET)

        date_modified = d.pop("dateModified", UNSET)

        modified_by_email = d.pop("modifiedByEmail", UNSET)

        is_active = d.pop("isActive", UNSET)

        _designation = d.pop("designation", UNSET)
        designation: Union[Unset, OnlineactionsformsformtrackingidResponse200Designation]
        if isinstance(_designation, Unset):
            designation = UNSET
        else:
            designation = OnlineactionsformsformtrackingidResponse200Designation.from_dict(_designation)

        _confirmation_email_data = d.pop("confirmationEmailData", UNSET)
        confirmation_email_data: Union[Unset, OnlineactionsformsformtrackingidResponse200ConfirmationEmailData]
        if isinstance(_confirmation_email_data, Unset):
            confirmation_email_data = UNSET
        else:
            confirmation_email_data = OnlineactionsformsformtrackingidResponse200ConfirmationEmailData.from_dict(
                _confirmation_email_data
            )

        activist_codes = cast(List[int], d.pop("activistCodes", UNSET))

        event_id = d.pop("eventId", UNSET)

        code_id = d.pop("codeId", UNSET)

        campaign_id = d.pop("campaignId", UNSET)

        is_confirmed_opt_in_enabled = d.pop("isConfirmedOptInEnabled", UNSET)

        onlineactionsformsformtrackingid_response_200 = cls(
            form_tracking_id=form_tracking_id,
            form_name=form_name,
            form_type=form_type,
            form_type_id=form_type_id,
            date_created=date_created,
            created_by_email=created_by_email,
            date_modified=date_modified,
            modified_by_email=modified_by_email,
            is_active=is_active,
            designation=designation,
            confirmation_email_data=confirmation_email_data,
            activist_codes=activist_codes,
            event_id=event_id,
            code_id=code_id,
            campaign_id=campaign_id,
            is_confirmed_opt_in_enabled=is_confirmed_opt_in_enabled,
        )

        onlineactionsformsformtrackingid_response_200.additional_properties = d
        return onlineactionsformsformtrackingid_response_200

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
