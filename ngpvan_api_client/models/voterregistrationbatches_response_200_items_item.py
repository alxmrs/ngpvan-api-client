from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.voterregistrationbatches_response_200_items_item_form import (
    VoterregistrationbatchesResponse200ItemsItemForm,
)
from ..models.voterregistrationbatches_response_200_items_item_program_type import (
    VoterregistrationbatchesResponse200ItemsItemProgramType,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="VoterregistrationbatchesResponse200ItemsItem")


@attr.s(auto_attribs=True)
class VoterregistrationbatchesResponse200ItemsItem:
    """
    Attributes:
        voter_registration_batch_id (Union[Unset, int]):  Example: 100.
        name (Union[Unset, str]):  Example: VR Batch.
        description (Union[Unset, str]):  Example: VR Batch Description.
        state_code (Union[Unset, str]):  Example: MA.
        form (Union[Unset, VoterregistrationbatchesResponse200ItemsItemForm]):
        status (Union[Unset, str]):  Example: Entering.
        program_type (Union[Unset, VoterregistrationbatchesResponse200ItemsItemProgramType]):
        person_type (Union[Unset, str]):  Example: Applicant.
        date_created (Union[Unset, str]):  Example: 2019-08-01T00:00:00Z.
    """

    voter_registration_batch_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    state_code: Union[Unset, str] = UNSET
    form: Union[Unset, VoterregistrationbatchesResponse200ItemsItemForm] = UNSET
    status: Union[Unset, str] = UNSET
    program_type: Union[Unset, VoterregistrationbatchesResponse200ItemsItemProgramType] = UNSET
    person_type: Union[Unset, str] = UNSET
    date_created: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        voter_registration_batch_id = self.voter_registration_batch_id
        name = self.name
        description = self.description
        state_code = self.state_code
        form: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.form, Unset):
            form = self.form.to_dict()

        status = self.status
        program_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.program_type, Unset):
            program_type = self.program_type.to_dict()

        person_type = self.person_type
        date_created = self.date_created

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if voter_registration_batch_id is not UNSET:
            field_dict["voterRegistrationBatchId"] = voter_registration_batch_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if state_code is not UNSET:
            field_dict["stateCode"] = state_code
        if form is not UNSET:
            field_dict["form"] = form
        if status is not UNSET:
            field_dict["status"] = status
        if program_type is not UNSET:
            field_dict["programType"] = program_type
        if person_type is not UNSET:
            field_dict["personType"] = person_type
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        voter_registration_batch_id = d.pop("voterRegistrationBatchId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        state_code = d.pop("stateCode", UNSET)

        _form = d.pop("form", UNSET)
        form: Union[Unset, VoterregistrationbatchesResponse200ItemsItemForm]
        if isinstance(_form, Unset):
            form = UNSET
        else:
            form = VoterregistrationbatchesResponse200ItemsItemForm.from_dict(_form)

        status = d.pop("status", UNSET)

        _program_type = d.pop("programType", UNSET)
        program_type: Union[Unset, VoterregistrationbatchesResponse200ItemsItemProgramType]
        if isinstance(_program_type, Unset):
            program_type = UNSET
        else:
            program_type = VoterregistrationbatchesResponse200ItemsItemProgramType.from_dict(_program_type)

        person_type = d.pop("personType", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        voterregistrationbatches_response_200_items_item = cls(
            voter_registration_batch_id=voter_registration_batch_id,
            name=name,
            description=description,
            state_code=state_code,
            form=form,
            status=status,
            program_type=program_type,
            person_type=person_type,
            date_created=date_created,
        )

        voterregistrationbatches_response_200_items_item.additional_properties = d
        return voterregistrationbatches_response_200_items_item

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
