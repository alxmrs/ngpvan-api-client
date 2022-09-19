from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.minivanexports_response_200_items_item_created_by import MinivanexportsResponse200ItemsItemCreatedBy
from ..types import UNSET, Unset

T = TypeVar("T", bound="MinivanexportsResponse200ItemsItem")


@attr.s(auto_attribs=True)
class MinivanexportsResponse200ItemsItem:
    """
    Attributes:
        minivan_export_id (Union[Unset, int]):  Example: 13149.
        name (Union[Unset, str]):  Example: Tulip City: Precinct 43 Turf 01.
        date_created (Union[Unset, str]):  Example: 2021-03-04T13:35:07.09Z.
        created_by (Union[Unset, MinivanexportsResponse200ItemsItemCreatedBy]):
        canvassers (Union[Unset, Any]):
        event_signups (Union[Unset, Any]):
        database_mode (Union[Unset, int]):
    """

    minivan_export_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    date_created: Union[Unset, str] = UNSET
    created_by: Union[Unset, MinivanexportsResponse200ItemsItemCreatedBy] = UNSET
    canvassers: Union[Unset, Any] = UNSET
    event_signups: Union[Unset, Any] = UNSET
    database_mode: Union[Unset, int] = 0
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        minivan_export_id = self.minivan_export_id
        name = self.name
        date_created = self.date_created
        created_by: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.created_by, Unset):
            created_by = self.created_by.to_dict()

        canvassers = self.canvassers
        event_signups = self.event_signups
        database_mode = self.database_mode

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if minivan_export_id is not UNSET:
            field_dict["minivanExportId"] = minivan_export_id
        if name is not UNSET:
            field_dict["name"] = name
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if created_by is not UNSET:
            field_dict["createdBy"] = created_by
        if canvassers is not UNSET:
            field_dict["canvassers"] = canvassers
        if event_signups is not UNSET:
            field_dict["eventSignups"] = event_signups
        if database_mode is not UNSET:
            field_dict["databaseMode"] = database_mode

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        minivan_export_id = d.pop("minivanExportId", UNSET)

        name = d.pop("name", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        _created_by = d.pop("createdBy", UNSET)
        created_by: Union[Unset, MinivanexportsResponse200ItemsItemCreatedBy]
        if isinstance(_created_by, Unset):
            created_by = UNSET
        else:
            created_by = MinivanexportsResponse200ItemsItemCreatedBy.from_dict(_created_by)

        canvassers = d.pop("canvassers", UNSET)

        event_signups = d.pop("eventSignups", UNSET)

        database_mode = d.pop("databaseMode", UNSET)

        minivanexports_response_200_items_item = cls(
            minivan_export_id=minivan_export_id,
            name=name,
            date_created=date_created,
            created_by=created_by,
            canvassers=canvassers,
            event_signups=event_signups,
            database_mode=database_mode,
        )

        minivanexports_response_200_items_item.additional_properties = d
        return minivanexports_response_200_items_item

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
