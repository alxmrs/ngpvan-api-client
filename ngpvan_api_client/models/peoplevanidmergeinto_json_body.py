from typing import Any, Dict, List, Type, TypeVar

import attr

T = TypeVar("T", bound="PeoplevanidmergeintoJsonBody")


@attr.s(auto_attribs=True)
class PeoplevanidmergeintoJsonBody:
    """
    Attributes:
        van_id (int): VANID for the **Target** record (the record that survives the merge)
    """

    van_id: int
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        van_id = self.van_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "vanId": van_id,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        van_id = d.pop("vanId")

        peoplevanidmergeinto_json_body = cls(
            van_id=van_id,
        )

        peoplevanidmergeinto_json_body.additional_properties = d
        return peoplevanidmergeinto_json_body

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
