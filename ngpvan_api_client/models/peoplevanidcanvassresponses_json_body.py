from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.peoplevanidcanvassresponses_json_body_canvass_context import (
    PeoplevanidcanvassresponsesJsonBodyCanvassContext,
)
from ..models.peoplevanidcanvassresponses_json_body_responses_item import (
    PeoplevanidcanvassresponsesJsonBodyResponsesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="PeoplevanidcanvassresponsesJsonBody")


@attr.s(auto_attribs=True)
class PeoplevanidcanvassresponsesJsonBody:
    """
    Attributes:
        canvass_context (Union[Unset, PeoplevanidcanvassresponsesJsonBodyCanvassContext]): Optional; describes the
            context in which this Canvass Response was created
        result_code_id (Union[Unset, int]): Optional; specifies the [Result Code](ref:canvass-
            responses#canvassresponsesresultcodes) of this Response. If no `resultCodeId` is specified, `responses` must be
            specified. Conversely, if `responses` are specified, `resultCodeId` must be null (a result of *Canvassed* is
            implied). The `resultCodeId` must be a valid Result Code in the current context. Default: 205.
        responses (Union[Unset, List[PeoplevanidcanvassresponsesJsonBodyResponsesItem]]): Optional; an array of Script
            Responses. If specified, `resultCodeId` must be null. Each Script Response has a property that determines the
            response's type. This array can contain multiple types.
    """

    canvass_context: Union[Unset, PeoplevanidcanvassresponsesJsonBodyCanvassContext] = UNSET
    result_code_id: Union[Unset, int] = 205
    responses: Union[Unset, List[PeoplevanidcanvassresponsesJsonBodyResponsesItem]] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        canvass_context: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.canvass_context, Unset):
            canvass_context = self.canvass_context.to_dict()

        result_code_id = self.result_code_id
        responses: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.responses, Unset):
            responses = []
            for responses_item_data in self.responses:
                responses_item = responses_item_data.to_dict()

                responses.append(responses_item)

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if canvass_context is not UNSET:
            field_dict["canvassContext"] = canvass_context
        if result_code_id is not UNSET:
            field_dict["resultCodeId"] = result_code_id
        if responses is not UNSET:
            field_dict["responses"] = responses

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        _canvass_context = d.pop("canvassContext", UNSET)
        canvass_context: Union[Unset, PeoplevanidcanvassresponsesJsonBodyCanvassContext]
        if isinstance(_canvass_context, Unset):
            canvass_context = UNSET
        else:
            canvass_context = PeoplevanidcanvassresponsesJsonBodyCanvassContext.from_dict(_canvass_context)

        result_code_id = d.pop("resultCodeId", UNSET)

        responses = []
        _responses = d.pop("responses", UNSET)
        for responses_item_data in _responses or []:
            responses_item = PeoplevanidcanvassresponsesJsonBodyResponsesItem.from_dict(responses_item_data)

            responses.append(responses_item)

        peoplevanidcanvassresponses_json_body = cls(
            canvass_context=canvass_context,
            result_code_id=result_code_id,
            responses=responses,
        )

        peoplevanidcanvassresponses_json_body.additional_properties = d
        return peoplevanidcanvassresponses_json_body

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
