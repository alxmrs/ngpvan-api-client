from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="Financialbatches1JsonBody")


@attr.s(auto_attribs=True)
class Financialbatches1JsonBody:
    """
    Attributes:
        financial_batch_number (Union[Unset, int]): Required; User-specified identifier for this batch. Must be unique
            within this context. Default: 8675308.
        financial_batch_name (Union[Unset, str]): User-specified name for this batch. Must be unique within this
            context. Must not be `Unassigned` Default: 'Example Batch'.
        designation_id (Union[Unset, int]): Required; [Designation](ref#designations) to associate this Financial Batch
            with. Default: 122.
        expected_contribution_count (Union[Unset, int]): If set, the number of contributions expected for this batch.
            The total count of contributions in the batch must match the expected count in order to close the batch.
            Default: 10.
        expected_contribution_total_amount (Union[Unset, float]): If set, the total monetary amount of contributions
            expected for this batch. The total amount of contributions in the batch must match the expected amount in order
            to close the batch. Default: 500.03.
    """

    financial_batch_number: Union[Unset, int] = 8675308
    financial_batch_name: Union[Unset, str] = "Example Batch"
    designation_id: Union[Unset, int] = 122
    expected_contribution_count: Union[Unset, int] = 10
    expected_contribution_total_amount: Union[Unset, float] = 500.03
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        financial_batch_number = self.financial_batch_number
        financial_batch_name = self.financial_batch_name
        designation_id = self.designation_id
        expected_contribution_count = self.expected_contribution_count
        expected_contribution_total_amount = self.expected_contribution_total_amount

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if financial_batch_number is not UNSET:
            field_dict["financialBatchNumber"] = financial_batch_number
        if financial_batch_name is not UNSET:
            field_dict["financialBatchName"] = financial_batch_name
        if designation_id is not UNSET:
            field_dict["designationId"] = designation_id
        if expected_contribution_count is not UNSET:
            field_dict["expectedContributionCount"] = expected_contribution_count
        if expected_contribution_total_amount is not UNSET:
            field_dict["expectedContributionTotalAmount"] = expected_contribution_total_amount

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        financial_batch_number = d.pop("financialBatchNumber", UNSET)

        financial_batch_name = d.pop("financialBatchName", UNSET)

        designation_id = d.pop("designationId", UNSET)

        expected_contribution_count = d.pop("expectedContributionCount", UNSET)

        expected_contribution_total_amount = d.pop("expectedContributionTotalAmount", UNSET)

        financialbatches_1_json_body = cls(
            financial_batch_number=financial_batch_number,
            financial_batch_name=financial_batch_name,
            designation_id=designation_id,
            expected_contribution_count=expected_contribution_count,
            expected_contribution_total_amount=expected_contribution_total_amount,
        )

        financialbatches_1_json_body.additional_properties = d
        return financialbatches_1_json_body

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
