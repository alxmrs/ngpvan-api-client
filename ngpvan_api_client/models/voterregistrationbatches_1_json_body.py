from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.voterregistrationbatches_1_json_body_form import Voterregistrationbatches1JsonBodyForm
from ..models.voterregistrationbatches_1_json_body_prgram_type import Voterregistrationbatches1JsonBodyPrgramType
from ..types import UNSET, Unset

T = TypeVar("T", bound="Voterregistrationbatches1JsonBody")


@attr.s(auto_attribs=True)
class Voterregistrationbatches1JsonBody:
    """
    Attributes:
        name (Union[Unset, str]):  Default: 'VR Batch'.
        description (Union[Unset, str]):  Default: 'VR Batch Description'.
        state_code (Union[Unset, str]):  Default: 'MA'.
        prgram_type (Union[Unset, Voterregistrationbatches1JsonBodyPrgramType]):
        form (Union[Unset, Voterregistrationbatches1JsonBodyForm]):
        person_type (Union[Unset, str]):  Default: 'Applicant'.
    """

    name: Union[Unset, str] = "VR Batch"
    description: Union[Unset, str] = "VR Batch Description"
    state_code: Union[Unset, str] = "MA"
    prgram_type: Union[Unset, Voterregistrationbatches1JsonBodyPrgramType] = UNSET
    form: Union[Unset, Voterregistrationbatches1JsonBodyForm] = UNSET
    person_type: Union[Unset, str] = "Applicant"
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        name = self.name
        description = self.description
        state_code = self.state_code
        prgram_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.prgram_type, Unset):
            prgram_type = self.prgram_type.to_dict()

        form: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.form, Unset):
            form = self.form.to_dict()

        person_type = self.person_type

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if state_code is not UNSET:
            field_dict["stateCode"] = state_code
        if prgram_type is not UNSET:
            field_dict["prgramType"] = prgram_type
        if form is not UNSET:
            field_dict["form"] = form
        if person_type is not UNSET:
            field_dict["personType"] = person_type

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        state_code = d.pop("stateCode", UNSET)

        _prgram_type = d.pop("prgramType", UNSET)
        prgram_type: Union[Unset, Voterregistrationbatches1JsonBodyPrgramType]
        if isinstance(_prgram_type, Unset):
            prgram_type = UNSET
        else:
            prgram_type = Voterregistrationbatches1JsonBodyPrgramType.from_dict(_prgram_type)

        _form = d.pop("form", UNSET)
        form: Union[Unset, Voterregistrationbatches1JsonBodyForm]
        if isinstance(_form, Unset):
            form = UNSET
        else:
            form = Voterregistrationbatches1JsonBodyForm.from_dict(_form)

        person_type = d.pop("personType", UNSET)

        voterregistrationbatches_1_json_body = cls(
            name=name,
            description=description,
            state_code=state_code,
            prgram_type=prgram_type,
            form=form,
            person_type=person_type,
        )

        voterregistrationbatches_1_json_body.additional_properties = d
        return voterregistrationbatches_1_json_body

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
