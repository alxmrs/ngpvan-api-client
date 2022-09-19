from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.get_people_not_enough_search_parameters_errors_item import GetPeopleNotEnoughSearchParametersErrorsItem
from ..types import UNSET, Unset

T = TypeVar("T", bound="GetPeopleNotEnoughSearchParameters")


@attr.s(auto_attribs=True)
class GetPeopleNotEnoughSearchParameters:
    """
    Attributes:
        errors (Union[Unset, List[GetPeopleNotEnoughSearchParametersErrorsItem]]):
    """

    errors: Union[Unset, List[GetPeopleNotEnoughSearchParametersErrorsItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        errors: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.errors, Unset):
            errors = []
            for errors_item_data in self.errors:
                errors_item = errors_item_data.to_dict()

                errors.append(errors_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if errors is not UNSET:
            field_dict["errors"] = errors

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        errors = []
        _errors = d.pop("errors", UNSET)
        for errors_item_data in _errors or []:
            errors_item = GetPeopleNotEnoughSearchParametersErrorsItem.from_dict(errors_item_data)

            errors.append(errors_item)

        get_people_not_enough_search_parameters = cls(
            errors=errors,
        )

        get_people_not_enough_search_parameters.additional_properties = d
        return get_people_not_enough_search_parameters

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
