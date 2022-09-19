from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.peoplevanidnames_response_200_pronouns import PeoplevanidnamesResponse200Pronouns
from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevanidnamesResponse200")


@attr.s(auto_attribs=True)
class PeoplevanidnamesResponse200:
    """
    Attributes:
        van_id (Union[Unset, int]):  Example: 12345678.
        first_name (Union[Unset, str]):  Example: Steven.
        last_name (Union[Unset, str]):  Example: Brooks.
        middle_name (Union[Unset, str]):  Example: Allen.
        suffix (Union[Unset, str]):  Example: II.
        title (Union[Unset, str]):  Example: Mr..
        source_file_title (Union[Unset, Any]):
        source_file_first_name (Union[Unset, Any]):
        source_file_middle_name (Union[Unset, Any]):
        source_file_last_name (Union[Unset, Any]):
        source_file_suffix (Union[Unset, Any]):
        contact_mode (Union[Unset, str]):  Example: Person.
        organization_contact_common_name (Union[Unset, Any]):
        organization_contact_official_name (Union[Unset, Any]):
        salutation (Union[Unset, str]):  Example: Steven.
        formal_salutation (Union[Unset, str]):  Example: Mr. Brooks.
        additional_salutation (Union[Unset, Any]):
        pronouns (Union[Unset, PeoplevanidnamesResponse200Pronouns]):
        envelope_name (Union[Unset, str]):  Example: Steven A. Brooks.
        formal_envelope_name (Union[Unset, str]):  Example: Mr. Steven A. Brooks, II.
        additional_envelope_name (Union[Unset, Any]):
        contact_method_preference_code (Union[Unset, Any]):
        nickname (Union[Unset, str]):  Example: Steve.
        website (Union[Unset, Any]):
        professional_suffix (Union[Unset, str]):  Example: M.D..
        party (Union[Unset, Any]):
        employer (Union[Unset, Any]):
        occupation (Union[Unset, Any]):
        sex (Union[Unset, Any]):
        date_of_birth (Union[Unset, Any]):
        self_reported_race (Union[Unset, Any]):
        self_reported_ethnicity (Union[Unset, Any]):
        self_reported_races (Union[Unset, Any]):
        self_reported_ethnicities (Union[Unset, Any]):
        self_reported_genders (Union[Unset, Any]):
        self_reported_sexual_orientations (Union[Unset, Any]):
        self_reported_language_preference (Union[Unset, Any]):
        emails (Union[Unset, Any]):
        phones (Union[Unset, Any]):
        addresses (Union[Unset, Any]):
        recorded_addresses (Union[Unset, Any]):
        identifiers (Union[Unset, Any]):
        codes (Union[Unset, Any]):
        custom_fields (Union[Unset, Any]):
        primary_custom_field (Union[Unset, Any]):
        contribution_summary (Union[Unset, Any]):
        suppressions (Union[Unset, Any]):
        casework_cases (Union[Unset, Any]):
        casework_issues (Union[Unset, Any]):
        casework_stories (Union[Unset, Any]):
        notes (Union[Unset, Any]):
        scores (Union[Unset, Any]):
        custom_properties (Union[Unset, Any]):
        election_records (Union[Unset, Any]):
        membership_status (Union[Unset, Any]):
        organization_roles (Union[Unset, Any]):
        districts (Union[Unset, Any]):
        survey_question_responses (Union[Unset, Any]):
        finder_number (Union[Unset, Any]):
        biography_image_url (Union[Unset, Any]):
        primary_contact (Union[Unset, Any]):
    """

    van_id: Union[Unset, int] = 0
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    middle_name: Union[Unset, str] = UNSET
    suffix: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    source_file_title: Union[Unset, Any] = UNSET
    source_file_first_name: Union[Unset, Any] = UNSET
    source_file_middle_name: Union[Unset, Any] = UNSET
    source_file_last_name: Union[Unset, Any] = UNSET
    source_file_suffix: Union[Unset, Any] = UNSET
    contact_mode: Union[Unset, str] = UNSET
    organization_contact_common_name: Union[Unset, Any] = UNSET
    organization_contact_official_name: Union[Unset, Any] = UNSET
    salutation: Union[Unset, str] = UNSET
    formal_salutation: Union[Unset, str] = UNSET
    additional_salutation: Union[Unset, Any] = UNSET
    pronouns: Union[Unset, PeoplevanidnamesResponse200Pronouns] = UNSET
    envelope_name: Union[Unset, str] = UNSET
    formal_envelope_name: Union[Unset, str] = UNSET
    additional_envelope_name: Union[Unset, Any] = UNSET
    contact_method_preference_code: Union[Unset, Any] = UNSET
    nickname: Union[Unset, str] = UNSET
    website: Union[Unset, Any] = UNSET
    professional_suffix: Union[Unset, str] = UNSET
    party: Union[Unset, Any] = UNSET
    employer: Union[Unset, Any] = UNSET
    occupation: Union[Unset, Any] = UNSET
    sex: Union[Unset, Any] = UNSET
    date_of_birth: Union[Unset, Any] = UNSET
    self_reported_race: Union[Unset, Any] = UNSET
    self_reported_ethnicity: Union[Unset, Any] = UNSET
    self_reported_races: Union[Unset, Any] = UNSET
    self_reported_ethnicities: Union[Unset, Any] = UNSET
    self_reported_genders: Union[Unset, Any] = UNSET
    self_reported_sexual_orientations: Union[Unset, Any] = UNSET
    self_reported_language_preference: Union[Unset, Any] = UNSET
    emails: Union[Unset, Any] = UNSET
    phones: Union[Unset, Any] = UNSET
    addresses: Union[Unset, Any] = UNSET
    recorded_addresses: Union[Unset, Any] = UNSET
    identifiers: Union[Unset, Any] = UNSET
    codes: Union[Unset, Any] = UNSET
    custom_fields: Union[Unset, Any] = UNSET
    primary_custom_field: Union[Unset, Any] = UNSET
    contribution_summary: Union[Unset, Any] = UNSET
    suppressions: Union[Unset, Any] = UNSET
    casework_cases: Union[Unset, Any] = UNSET
    casework_issues: Union[Unset, Any] = UNSET
    casework_stories: Union[Unset, Any] = UNSET
    notes: Union[Unset, Any] = UNSET
    scores: Union[Unset, Any] = UNSET
    custom_properties: Union[Unset, Any] = UNSET
    election_records: Union[Unset, Any] = UNSET
    membership_status: Union[Unset, Any] = UNSET
    organization_roles: Union[Unset, Any] = UNSET
    districts: Union[Unset, Any] = UNSET
    survey_question_responses: Union[Unset, Any] = UNSET
    finder_number: Union[Unset, Any] = UNSET
    biography_image_url: Union[Unset, Any] = UNSET
    primary_contact: Union[Unset, Any] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        van_id = self.van_id
        first_name = self.first_name
        last_name = self.last_name
        middle_name = self.middle_name
        suffix = self.suffix
        title = self.title
        source_file_title = self.source_file_title
        source_file_first_name = self.source_file_first_name
        source_file_middle_name = self.source_file_middle_name
        source_file_last_name = self.source_file_last_name
        source_file_suffix = self.source_file_suffix
        contact_mode = self.contact_mode
        organization_contact_common_name = self.organization_contact_common_name
        organization_contact_official_name = self.organization_contact_official_name
        salutation = self.salutation
        formal_salutation = self.formal_salutation
        additional_salutation = self.additional_salutation
        pronouns: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.pronouns, Unset):
            pronouns = self.pronouns.to_dict()

        envelope_name = self.envelope_name
        formal_envelope_name = self.formal_envelope_name
        additional_envelope_name = self.additional_envelope_name
        contact_method_preference_code = self.contact_method_preference_code
        nickname = self.nickname
        website = self.website
        professional_suffix = self.professional_suffix
        party = self.party
        employer = self.employer
        occupation = self.occupation
        sex = self.sex
        date_of_birth = self.date_of_birth
        self_reported_race = self.self_reported_race
        self_reported_ethnicity = self.self_reported_ethnicity
        self_reported_races = self.self_reported_races
        self_reported_ethnicities = self.self_reported_ethnicities
        self_reported_genders = self.self_reported_genders
        self_reported_sexual_orientations = self.self_reported_sexual_orientations
        self_reported_language_preference = self.self_reported_language_preference
        emails = self.emails
        phones = self.phones
        addresses = self.addresses
        recorded_addresses = self.recorded_addresses
        identifiers = self.identifiers
        codes = self.codes
        custom_fields = self.custom_fields
        primary_custom_field = self.primary_custom_field
        contribution_summary = self.contribution_summary
        suppressions = self.suppressions
        casework_cases = self.casework_cases
        casework_issues = self.casework_issues
        casework_stories = self.casework_stories
        notes = self.notes
        scores = self.scores
        custom_properties = self.custom_properties
        election_records = self.election_records
        membership_status = self.membership_status
        organization_roles = self.organization_roles
        districts = self.districts
        survey_question_responses = self.survey_question_responses
        finder_number = self.finder_number
        biography_image_url = self.biography_image_url
        primary_contact = self.primary_contact

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if van_id is not UNSET:
            field_dict["vanId"] = van_id
        if first_name is not UNSET:
            field_dict["firstName"] = first_name
        if last_name is not UNSET:
            field_dict["lastName"] = last_name
        if middle_name is not UNSET:
            field_dict["middleName"] = middle_name
        if suffix is not UNSET:
            field_dict["suffix"] = suffix
        if title is not UNSET:
            field_dict["title"] = title
        if source_file_title is not UNSET:
            field_dict["sourceFileTitle"] = source_file_title
        if source_file_first_name is not UNSET:
            field_dict["sourceFileFirstName"] = source_file_first_name
        if source_file_middle_name is not UNSET:
            field_dict["sourceFileMiddleName"] = source_file_middle_name
        if source_file_last_name is not UNSET:
            field_dict["sourceFileLastName"] = source_file_last_name
        if source_file_suffix is not UNSET:
            field_dict["sourceFileSuffix"] = source_file_suffix
        if contact_mode is not UNSET:
            field_dict["contactMode"] = contact_mode
        if organization_contact_common_name is not UNSET:
            field_dict["organizationContactCommonName"] = organization_contact_common_name
        if organization_contact_official_name is not UNSET:
            field_dict["organizationContactOfficialName"] = organization_contact_official_name
        if salutation is not UNSET:
            field_dict["salutation"] = salutation
        if formal_salutation is not UNSET:
            field_dict["formalSalutation"] = formal_salutation
        if additional_salutation is not UNSET:
            field_dict["additionalSalutation"] = additional_salutation
        if pronouns is not UNSET:
            field_dict["pronouns"] = pronouns
        if envelope_name is not UNSET:
            field_dict["envelopeName"] = envelope_name
        if formal_envelope_name is not UNSET:
            field_dict["formalEnvelopeName"] = formal_envelope_name
        if additional_envelope_name is not UNSET:
            field_dict["additionalEnvelopeName"] = additional_envelope_name
        if contact_method_preference_code is not UNSET:
            field_dict["contactMethodPreferenceCode"] = contact_method_preference_code
        if nickname is not UNSET:
            field_dict["nickname"] = nickname
        if website is not UNSET:
            field_dict["website"] = website
        if professional_suffix is not UNSET:
            field_dict["professionalSuffix"] = professional_suffix
        if party is not UNSET:
            field_dict["party"] = party
        if employer is not UNSET:
            field_dict["employer"] = employer
        if occupation is not UNSET:
            field_dict["occupation"] = occupation
        if sex is not UNSET:
            field_dict["sex"] = sex
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if self_reported_race is not UNSET:
            field_dict["selfReportedRace"] = self_reported_race
        if self_reported_ethnicity is not UNSET:
            field_dict["selfReportedEthnicity"] = self_reported_ethnicity
        if self_reported_races is not UNSET:
            field_dict["selfReportedRaces"] = self_reported_races
        if self_reported_ethnicities is not UNSET:
            field_dict["selfReportedEthnicities"] = self_reported_ethnicities
        if self_reported_genders is not UNSET:
            field_dict["selfReportedGenders"] = self_reported_genders
        if self_reported_sexual_orientations is not UNSET:
            field_dict["selfReportedSexualOrientations"] = self_reported_sexual_orientations
        if self_reported_language_preference is not UNSET:
            field_dict["selfReportedLanguagePreference"] = self_reported_language_preference
        if emails is not UNSET:
            field_dict["emails"] = emails
        if phones is not UNSET:
            field_dict["phones"] = phones
        if addresses is not UNSET:
            field_dict["addresses"] = addresses
        if recorded_addresses is not UNSET:
            field_dict["recordedAddresses"] = recorded_addresses
        if identifiers is not UNSET:
            field_dict["identifiers"] = identifiers
        if codes is not UNSET:
            field_dict["codes"] = codes
        if custom_fields is not UNSET:
            field_dict["customFields"] = custom_fields
        if primary_custom_field is not UNSET:
            field_dict["primaryCustomField"] = primary_custom_field
        if contribution_summary is not UNSET:
            field_dict["contributionSummary"] = contribution_summary
        if suppressions is not UNSET:
            field_dict["suppressions"] = suppressions
        if casework_cases is not UNSET:
            field_dict["caseworkCases"] = casework_cases
        if casework_issues is not UNSET:
            field_dict["caseworkIssues"] = casework_issues
        if casework_stories is not UNSET:
            field_dict["caseworkStories"] = casework_stories
        if notes is not UNSET:
            field_dict["notes"] = notes
        if scores is not UNSET:
            field_dict["scores"] = scores
        if custom_properties is not UNSET:
            field_dict["customProperties"] = custom_properties
        if election_records is not UNSET:
            field_dict["electionRecords"] = election_records
        if membership_status is not UNSET:
            field_dict["membershipStatus"] = membership_status
        if organization_roles is not UNSET:
            field_dict["organizationRoles"] = organization_roles
        if districts is not UNSET:
            field_dict["districts"] = districts
        if survey_question_responses is not UNSET:
            field_dict["surveyQuestionResponses"] = survey_question_responses
        if finder_number is not UNSET:
            field_dict["finderNumber"] = finder_number
        if biography_image_url is not UNSET:
            field_dict["biographyImageUrl"] = biography_image_url
        if primary_contact is not UNSET:
            field_dict["primaryContact"] = primary_contact

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        van_id = d.pop("vanId", UNSET)

        first_name = d.pop("firstName", UNSET)

        last_name = d.pop("lastName", UNSET)

        middle_name = d.pop("middleName", UNSET)

        suffix = d.pop("suffix", UNSET)

        title = d.pop("title", UNSET)

        source_file_title = d.pop("sourceFileTitle", UNSET)

        source_file_first_name = d.pop("sourceFileFirstName", UNSET)

        source_file_middle_name = d.pop("sourceFileMiddleName", UNSET)

        source_file_last_name = d.pop("sourceFileLastName", UNSET)

        source_file_suffix = d.pop("sourceFileSuffix", UNSET)

        contact_mode = d.pop("contactMode", UNSET)

        organization_contact_common_name = d.pop("organizationContactCommonName", UNSET)

        organization_contact_official_name = d.pop("organizationContactOfficialName", UNSET)

        salutation = d.pop("salutation", UNSET)

        formal_salutation = d.pop("formalSalutation", UNSET)

        additional_salutation = d.pop("additionalSalutation", UNSET)

        _pronouns = d.pop("pronouns", UNSET)
        pronouns: Union[Unset, PeoplevanidnamesResponse200Pronouns]
        if isinstance(_pronouns, Unset):
            pronouns = UNSET
        else:
            pronouns = PeoplevanidnamesResponse200Pronouns.from_dict(_pronouns)

        envelope_name = d.pop("envelopeName", UNSET)

        formal_envelope_name = d.pop("formalEnvelopeName", UNSET)

        additional_envelope_name = d.pop("additionalEnvelopeName", UNSET)

        contact_method_preference_code = d.pop("contactMethodPreferenceCode", UNSET)

        nickname = d.pop("nickname", UNSET)

        website = d.pop("website", UNSET)

        professional_suffix = d.pop("professionalSuffix", UNSET)

        party = d.pop("party", UNSET)

        employer = d.pop("employer", UNSET)

        occupation = d.pop("occupation", UNSET)

        sex = d.pop("sex", UNSET)

        date_of_birth = d.pop("dateOfBirth", UNSET)

        self_reported_race = d.pop("selfReportedRace", UNSET)

        self_reported_ethnicity = d.pop("selfReportedEthnicity", UNSET)

        self_reported_races = d.pop("selfReportedRaces", UNSET)

        self_reported_ethnicities = d.pop("selfReportedEthnicities", UNSET)

        self_reported_genders = d.pop("selfReportedGenders", UNSET)

        self_reported_sexual_orientations = d.pop("selfReportedSexualOrientations", UNSET)

        self_reported_language_preference = d.pop("selfReportedLanguagePreference", UNSET)

        emails = d.pop("emails", UNSET)

        phones = d.pop("phones", UNSET)

        addresses = d.pop("addresses", UNSET)

        recorded_addresses = d.pop("recordedAddresses", UNSET)

        identifiers = d.pop("identifiers", UNSET)

        codes = d.pop("codes", UNSET)

        custom_fields = d.pop("customFields", UNSET)

        primary_custom_field = d.pop("primaryCustomField", UNSET)

        contribution_summary = d.pop("contributionSummary", UNSET)

        suppressions = d.pop("suppressions", UNSET)

        casework_cases = d.pop("caseworkCases", UNSET)

        casework_issues = d.pop("caseworkIssues", UNSET)

        casework_stories = d.pop("caseworkStories", UNSET)

        notes = d.pop("notes", UNSET)

        scores = d.pop("scores", UNSET)

        custom_properties = d.pop("customProperties", UNSET)

        election_records = d.pop("electionRecords", UNSET)

        membership_status = d.pop("membershipStatus", UNSET)

        organization_roles = d.pop("organizationRoles", UNSET)

        districts = d.pop("districts", UNSET)

        survey_question_responses = d.pop("surveyQuestionResponses", UNSET)

        finder_number = d.pop("finderNumber", UNSET)

        biography_image_url = d.pop("biographyImageUrl", UNSET)

        primary_contact = d.pop("primaryContact", UNSET)

        peoplevanidnames_response_200 = cls(
            van_id=van_id,
            first_name=first_name,
            last_name=last_name,
            middle_name=middle_name,
            suffix=suffix,
            title=title,
            source_file_title=source_file_title,
            source_file_first_name=source_file_first_name,
            source_file_middle_name=source_file_middle_name,
            source_file_last_name=source_file_last_name,
            source_file_suffix=source_file_suffix,
            contact_mode=contact_mode,
            organization_contact_common_name=organization_contact_common_name,
            organization_contact_official_name=organization_contact_official_name,
            salutation=salutation,
            formal_salutation=formal_salutation,
            additional_salutation=additional_salutation,
            pronouns=pronouns,
            envelope_name=envelope_name,
            formal_envelope_name=formal_envelope_name,
            additional_envelope_name=additional_envelope_name,
            contact_method_preference_code=contact_method_preference_code,
            nickname=nickname,
            website=website,
            professional_suffix=professional_suffix,
            party=party,
            employer=employer,
            occupation=occupation,
            sex=sex,
            date_of_birth=date_of_birth,
            self_reported_race=self_reported_race,
            self_reported_ethnicity=self_reported_ethnicity,
            self_reported_races=self_reported_races,
            self_reported_ethnicities=self_reported_ethnicities,
            self_reported_genders=self_reported_genders,
            self_reported_sexual_orientations=self_reported_sexual_orientations,
            self_reported_language_preference=self_reported_language_preference,
            emails=emails,
            phones=phones,
            addresses=addresses,
            recorded_addresses=recorded_addresses,
            identifiers=identifiers,
            codes=codes,
            custom_fields=custom_fields,
            primary_custom_field=primary_custom_field,
            contribution_summary=contribution_summary,
            suppressions=suppressions,
            casework_cases=casework_cases,
            casework_issues=casework_issues,
            casework_stories=casework_stories,
            notes=notes,
            scores=scores,
            custom_properties=custom_properties,
            election_records=election_records,
            membership_status=membership_status,
            organization_roles=organization_roles,
            districts=districts,
            survey_question_responses=survey_question_responses,
            finder_number=finder_number,
            biography_image_url=biography_image_url,
            primary_contact=primary_contact,
        )

        peoplevanidnames_response_200.additional_properties = d
        return peoplevanidnames_response_200

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
