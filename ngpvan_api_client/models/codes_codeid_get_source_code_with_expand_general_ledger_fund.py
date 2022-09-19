from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="CodesCodeidGetSourceCodeWithExpandGeneralLedgerFund")


@attr.s(auto_attribs=True)
class CodesCodeidGetSourceCodeWithExpandGeneralLedgerFund:
    """
    Attributes:
        general_ledger_fund_id (Union[Unset, int]):  Example: 68.
        name (Union[Unset, str]):  Example: API General Ledger Fund.
        description (Union[Unset, str]):  Example: API General Ledger Fund for Source Code.
        is_active (Union[Unset, bool]):  Default: True. Example: True.
    """

    general_ledger_fund_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    is_active: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        general_ledger_fund_id = self.general_ledger_fund_id
        name = self.name
        description = self.description
        is_active = self.is_active

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if general_ledger_fund_id is not UNSET:
            field_dict["generalLedgerFundId"] = general_ledger_fund_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if is_active is not UNSET:
            field_dict["isActive"] = is_active

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        general_ledger_fund_id = d.pop("generalLedgerFundId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        is_active = d.pop("isActive", UNSET)

        codes_codeid_get_source_code_with_expand_general_ledger_fund = cls(
            general_ledger_fund_id=general_ledger_fund_id,
            name=name,
            description=description,
            is_active=is_active,
        )

        codes_codeid_get_source_code_with_expand_general_ledger_fund.additional_properties = d
        return codes_codeid_get_source_code_with_expand_general_ledger_fund

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
