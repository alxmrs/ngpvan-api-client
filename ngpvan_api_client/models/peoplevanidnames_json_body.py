from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevanidnamesJsonBody")


@attr.s(auto_attribs=True)
class PeoplevanidnamesJsonBody:
    """
    Attributes:
        title (Union[Unset, str]): Optional; an honorific
        first_name (Union[Unset, str]): Optional; a person’s first name
        middle_name (Union[Unset, str]): Optional; a person’s middle name
        last_name (Union[Unset, str]): Optional; a person’s last name
        suffix (Union[Unset, str]): Optional; part of name following last name, e.g. "Jr."
        professional_suffix (Union[Unset, str]): Optional; a person's professional suffix, e.g. "M.D."
        nickname (Union[Unset, str]): Optional; a person's preferred informal name
        salutation (Union[Unset, str]): Optional; preferred greeting for correspondence; defaults to a person's
            `firstName`
        additional_salutation (Union[Unset, str]): Optional; additional preferred greeting for correspondence; defaults
            to `organizationContactCommonName` for organizations
        formal_salutation (Union[Unset, str]): Optional; preferred formal greeting for correspondence; defaults to
            `title` and `lastName` for people or "Friends" for organizations
        envelope_name (Union[Unset, str]): Optional; preferred name to use for mailings; defaults to the person's full
            name, including their middle initial, or `organizationContactCommonName` depending on the contact type
        formal_envelope_name (Union[Unset, str]): Optional; preferred formal name to use for mailings; defaults to the
            person's full name, including their middle initial, title, and suffix, or `organizationContactOfficialName`
            depending on the contact type
        additional_envelope_name (Union[Unset, str]): Optional; additional preferred name to use for mailings
        pronouns (Union[Unset, str]): Optional; a person's pronouns
        organization_contact_common_name (Union[Unset, str]): Optional; an organization's common name
        organization_contact_official_name (Union[Unset, str]): Optional; an organization's official name
    """

    title: Union[Unset, str] = UNSET
    first_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    suffix: Union[Unset, str] = UNSET
    professional_suffix: Union[Unset, str] = UNSET
    nickname: Union[Unset, str] = UNSET
    salutation: Union[Unset, str] = UNSET
    additional_salutation: Union[Unset, str] = UNSET
    formal_salutation: Union[Unset, str] = UNSET
    envelope_name: Union[Unset, str] = UNSET
    formal_envelope_name: Union[Unset, str] = UNSET
    additional_envelope_name: Union[Unset, str] = UNSET
    pronouns: Union[Unset, str] = UNSET
    organization_contact_common_name: Union[Unset, str] = UNSET
    organization_contact_official_name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        title = self.title
        first_name = self.first_name
        middle_name = self.middle_name
        last_name = self.last_name
        suffix = self.suffix
        professional_suffix = self.professional_suffix
        nickname = self.nickname
        salutation = self.salutation
        additional_salutation = self.additional_salutation
        formal_salutation = self.formal_salutation
        envelope_name = self.envelope_name
        formal_envelope_name = self.formal_envelope_name
        additional_envelope_name = self.additional_envelope_name
        pronouns = self.pronouns
        organization_contact_common_name = self.organization_contact_common_name
        organization_contact_official_name = self.organization_contact_official_name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if title is not UNSET:
            field_dict["title"] = title
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if professional_suffix is not UNSET:
            field_dict["professionalSuffix"] = professional_suffix
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if additional_salutation is not UNSET:
            field_dict["additionalSalutation"] = additional_salutation
        if formal_salutation is not UNSET:
            field_dict["formalSalutation"] = formal_salutation
        if envelope_name is not UNSET:
            field_dict["envelopeName"] = envelope_name
        if formal_envelope_name is not UNSET:
            field_dict["formalEnvelopeName"] = formal_envelope_name
        if additional_envelope_name is not UNSET:
            field_dict["additionalEnvelopeName"] = additional_envelope_name
        if pronouns is not UNSET:
            field_dict["pronouns"] = pronouns
        if organization_contact_common_name is not UNSET:
            field_dict["organizationContactCommonName"] = organization_contact_common_name
        if organization_contact_official_name is not UNSET:
            field_dict["organizationContactOfficialName"] = organization_contact_official_name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        title = d.pop("title", UNSET)

        first_name = d.pop("firstName", UNSET)

        middle_name = d.pop("middleName", UNSET)

        last_name = d.pop("lastName", UNSET)

        suffix = d.pop("suffix", UNSET)

        professional_suffix = d.pop("professionalSuffix", UNSET)

        nickname = d.pop("nickname", UNSET)

        salutation = d.pop("salutation", UNSET)

        additional_salutation = d.pop("additionalSalutation", UNSET)

        formal_salutation = d.pop("formalSalutation", UNSET)

        envelope_name = d.pop("envelopeName", UNSET)

        formal_envelope_name = d.pop("formalEnvelopeName", UNSET)

        additional_envelope_name = d.pop("additionalEnvelopeName", UNSET)

        pronouns = d.pop("pronouns", UNSET)

        organization_contact_common_name = d.pop("organizationContactCommonName", UNSET)

        organization_contact_official_name = d.pop("organizationContactOfficialName", UNSET)

        peoplevanidnames_json_body = cls(
            title=title,
            first_name=first_name,
            middle_name=middle_name,
            last_name=last_name,
            suffix=suffix,
            professional_suffix=professional_suffix,
            nickname=nickname,
            salutation=salutation,
            additional_salutation=additional_salutation,
            formal_salutation=formal_salutation,
            envelope_name=envelope_name,
            formal_envelope_name=formal_envelope_name,
            additional_envelope_name=additional_envelope_name,
            pronouns=pronouns,
            organization_contact_common_name=organization_contact_common_name,
            organization_contact_official_name=organization_contact_official_name,
        )

        peoplevanidnames_json_body.additional_properties = d
        return peoplevanidnames_json_body

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
