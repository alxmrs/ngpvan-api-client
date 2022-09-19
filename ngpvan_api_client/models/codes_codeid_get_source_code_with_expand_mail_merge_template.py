from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodesCodeidGetSourceCodeWithExpandMailMergeTemplate")


@attr.s(auto_attribs=True)
class CodesCodeidGetSourceCodeWithExpandMailMergeTemplate:
    """
    Attributes:
        mail_merge_template_id (Union[Unset, int]):  Example: 337.
        name (Union[Unset, str]):  Example: API Mail Merge Template for Tests.
    """

    mail_merge_template_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        mail_merge_template_id = self.mail_merge_template_id
        name = self.name

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if mail_merge_template_id is not UNSET:
            field_dict["mailMergeTemplateId"] = mail_merge_template_id
        if name is not UNSET:
            field_dict["name"] = name

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        mail_merge_template_id = d.pop("mailMergeTemplateId", UNSET)

        name = d.pop("name", UNSET)

        codes_codeid_get_source_code_with_expand_mail_merge_template = cls(
            mail_merge_template_id=mail_merge_template_id,
            name=name,
        )

        codes_codeid_get_source_code_with_expand_mail_merge_template.additional_properties = d
        return codes_codeid_get_source_code_with_expand_mail_merge_template

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
