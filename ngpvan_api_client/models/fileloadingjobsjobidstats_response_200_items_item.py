from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

T = TypeVar("T", bound="FileloadingjobsjobidstatsResponse200ItemsItem")


@attr.s(auto_attribs=True)
class FileloadingjobsjobidstatsResponse200ItemsItem:
    """
    Attributes:
        count_bad_rows (Union[Unset, int]):
        percent_matched (Union[Unset, int]):  Example: 100.
        count_phones_added (Union[Unset, int]):  Example: 1.
        action_type (Union[Unset, str]):  Example: PhonesFile.
        count_total_rows (Union[Unset, int]):  Example: 1.
        count_matched_rows (Union[Unset, int]):  Example: 1.
    """

    count_bad_rows: Union[Unset, int] = 0
    percent_matched: Union[Unset, int] = 0
    count_phones_added: Union[Unset, int] = 0
    action_type: Union[Unset, str] = UNSET
    count_total_rows: Union[Unset, int] = 0
    count_matched_rows: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        count_bad_rows = self.count_bad_rows
        percent_matched = self.percent_matched
        count_phones_added = self.count_phones_added
        action_type = self.action_type
        count_total_rows = self.count_total_rows
        count_matched_rows = self.count_matched_rows

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if count_bad_rows is not UNSET:
            field_dict["countBadRows"] = count_bad_rows
        if percent_matched is not UNSET:
            field_dict["percentMatched"] = percent_matched
        if count_phones_added is not UNSET:
            field_dict["countPhonesAdded"] = count_phones_added
        if action_type is not UNSET:
            field_dict["actionType"] = action_type
        if count_total_rows is not UNSET:
            field_dict["countTotalRows"] = count_total_rows
        if count_matched_rows is not UNSET:
            field_dict["countMatchedRows"] = count_matched_rows

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        count_bad_rows = d.pop("countBadRows", UNSET)

        percent_matched = d.pop("percentMatched", UNSET)

        count_phones_added = d.pop("countPhonesAdded", UNSET)

        action_type = d.pop("actionType", UNSET)

        count_total_rows = d.pop("countTotalRows", UNSET)

        count_matched_rows = d.pop("countMatchedRows", UNSET)

        fileloadingjobsjobidstats_response_200_items_item = cls(
            count_bad_rows=count_bad_rows,
            percent_matched=percent_matched,
            count_phones_added=count_phones_added,
            action_type=action_type,
            count_total_rows=count_total_rows,
            count_matched_rows=count_matched_rows,
        )

        fileloadingjobsjobidstats_response_200_items_item.additional_properties = d
        return fileloadingjobsjobidstats_response_200_items_item

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
