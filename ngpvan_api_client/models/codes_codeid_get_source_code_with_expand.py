from typing import Any, Dict, List, Type, TypeVar, Union

import attr

from ..models.codes_codeid_get_source_code_with_expand_campaign import CodesCodeidGetSourceCodeWithExpandCampaign
from ..models.codes_codeid_get_source_code_with_expand_contact_type import CodesCodeidGetSourceCodeWithExpandContactType
from ..models.codes_codeid_get_source_code_with_expand_cost_center import CodesCodeidGetSourceCodeWithExpandCostCenter
from ..models.codes_codeid_get_source_code_with_expand_general_ledger_fund import (
    CodesCodeidGetSourceCodeWithExpandGeneralLedgerFund,
)
from ..models.codes_codeid_get_source_code_with_expand_mail_merge_template import (
    CodesCodeidGetSourceCodeWithExpandMailMergeTemplate,
)
from ..models.codes_codeid_get_source_code_with_expand_revenue_stream import (
    CodesCodeidGetSourceCodeWithExpandRevenueStream,
)
from ..models.codes_codeid_get_source_code_with_expand_supported_entities_item import (
    CodesCodeidGetSourceCodeWithExpandSupportedEntitiesItem,
)
from ..types import UNSET, Unset

T = TypeVar("T", bound="CodesCodeidGetSourceCodeWithExpand")


@attr.s(auto_attribs=True)
class CodesCodeidGetSourceCodeWithExpand:
    """
    Attributes:
        code_id (Union[Unset, int]):  Example: 1085455.
        parent_code_id (Union[Unset, int]):  Example: 1000479.
        name (Union[Unset, str]):  Example: API Functional Test Source Code.
        description (Union[Unset, str]):  Example: Source Code for API Functional Tests.
        code_path (Union[Unset, str]):  Example: API Source Code 1/API Functional Test Source Code.
        created_by_name (Union[Unset, str]):  Example: A user.
        date_created (Union[Unset, str]):  Example: 2022-03-01T12:00:00Z.
        supported_entities (Union[Unset, List[CodesCodeidGetSourceCodeWithExpandSupportedEntitiesItem]]):
        code_type (Union[Unset, str]):  Example: SourceCode.
        campaign (Union[Unset, CodesCodeidGetSourceCodeWithExpandCampaign]):
        contact_type (Union[Unset, CodesCodeidGetSourceCodeWithExpandContactType]):
        date_modified (Union[Unset, str]):  Example: 2022-03-01T12:00:00Z.
        revenue_stream_id (Union[Unset, int]):  Example: 179.
        general_ledger_fund (Union[Unset, CodesCodeidGetSourceCodeWithExpandGeneralLedgerFund]):
        cost_center (Union[Unset, CodesCodeidGetSourceCodeWithExpandCostCenter]):
        revenue_stream (Union[Unset, CodesCodeidGetSourceCodeWithExpandRevenueStream]):
        mail_merge_template (Union[Unset, CodesCodeidGetSourceCodeWithExpandMailMergeTemplate]):
        is_source_code_applicable (Union[Unset, bool]):  Default: True. Example: True.
    """

    code_id: Union[Unset, int] = 0
    parent_code_id: Union[Unset, int] = 0
    name: Union[Unset, str] = UNSET
    description: Union[Unset, str] = UNSET
    code_path: Union[Unset, str] = UNSET
    created_by_name: Union[Unset, str] = UNSET
    date_created: Union[Unset, str] = UNSET
    supported_entities: Union[Unset, List[CodesCodeidGetSourceCodeWithExpandSupportedEntitiesItem]] = UNSET
    code_type: Union[Unset, str] = UNSET
    campaign: Union[Unset, CodesCodeidGetSourceCodeWithExpandCampaign] = UNSET
    contact_type: Union[Unset, CodesCodeidGetSourceCodeWithExpandContactType] = UNSET
    date_modified: Union[Unset, str] = UNSET
    revenue_stream_id: Union[Unset, int] = 0
    general_ledger_fund: Union[Unset, CodesCodeidGetSourceCodeWithExpandGeneralLedgerFund] = UNSET
    cost_center: Union[Unset, CodesCodeidGetSourceCodeWithExpandCostCenter] = UNSET
    revenue_stream: Union[Unset, CodesCodeidGetSourceCodeWithExpandRevenueStream] = UNSET
    mail_merge_template: Union[Unset, CodesCodeidGetSourceCodeWithExpandMailMergeTemplate] = UNSET
    is_source_code_applicable: Union[Unset, bool] = True
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        code_id = self.code_id
        parent_code_id = self.parent_code_id
        name = self.name
        description = self.description
        code_path = self.code_path
        created_by_name = self.created_by_name
        date_created = self.date_created
        supported_entities: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.supported_entities, Unset):
            supported_entities = []
            for supported_entities_item_data in self.supported_entities:
                supported_entities_item = supported_entities_item_data.to_dict()

                supported_entities.append(supported_entities_item)

        code_type = self.code_type
        campaign: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.campaign, Unset):
            campaign = self.campaign.to_dict()

        contact_type: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.contact_type, Unset):
            contact_type = self.contact_type.to_dict()

        date_modified = self.date_modified
        revenue_stream_id = self.revenue_stream_id
        general_ledger_fund: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.general_ledger_fund, Unset):
            general_ledger_fund = self.general_ledger_fund.to_dict()

        cost_center: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.cost_center, Unset):
            cost_center = self.cost_center.to_dict()

        revenue_stream: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.revenue_stream, Unset):
            revenue_stream = self.revenue_stream.to_dict()

        mail_merge_template: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.mail_merge_template, Unset):
            mail_merge_template = self.mail_merge_template.to_dict()

        is_source_code_applicable = self.is_source_code_applicable

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if code_id is not UNSET:
            field_dict["codeId"] = code_id
        if parent_code_id is not UNSET:
            field_dict["parentCodeId"] = parent_code_id
        if name is not UNSET:
            field_dict["name"] = name
        if description is not UNSET:
            field_dict["description"] = description
        if code_path is not UNSET:
            field_dict["codePath"] = code_path
        if created_by_name is not UNSET:
            field_dict["createdByName"] = created_by_name
        if date_created is not UNSET:
            field_dict["dateCreated"] = date_created
        if supported_entities is not UNSET:
            field_dict["supportedEntities"] = supported_entities
        if code_type is not UNSET:
            field_dict["codeType"] = code_type
        if campaign is not UNSET:
            field_dict["campaign"] = campaign
        if contact_type is not UNSET:
            field_dict["contactType"] = contact_type
        if date_modified is not UNSET:
            field_dict["dateModified"] = date_modified
        if revenue_stream_id is not UNSET:
            field_dict["revenueStreamId"] = revenue_stream_id
        if general_ledger_fund is not UNSET:
            field_dict["generalLedgerFund"] = general_ledger_fund
        if cost_center is not UNSET:
            field_dict["costCenter"] = cost_center
        if revenue_stream is not UNSET:
            field_dict["revenueStream"] = revenue_stream
        if mail_merge_template is not UNSET:
            field_dict["mailMergeTemplate"] = mail_merge_template
        if is_source_code_applicable is not UNSET:
            field_dict["isSourceCodeApplicable"] = is_source_code_applicable

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        code_id = d.pop("codeId", UNSET)

        parent_code_id = d.pop("parentCodeId", UNSET)

        name = d.pop("name", UNSET)

        description = d.pop("description", UNSET)

        code_path = d.pop("codePath", UNSET)

        created_by_name = d.pop("createdByName", UNSET)

        date_created = d.pop("dateCreated", UNSET)

        supported_entities = []
        _supported_entities = d.pop("supportedEntities", UNSET)
        for supported_entities_item_data in _supported_entities or []:
            supported_entities_item = CodesCodeidGetSourceCodeWithExpandSupportedEntitiesItem.from_dict(
                supported_entities_item_data
            )

            supported_entities.append(supported_entities_item)

        code_type = d.pop("codeType", UNSET)

        _campaign = d.pop("campaign", UNSET)
        campaign: Union[Unset, CodesCodeidGetSourceCodeWithExpandCampaign]
        if isinstance(_campaign, Unset):
            campaign = UNSET
        else:
            campaign = CodesCodeidGetSourceCodeWithExpandCampaign.from_dict(_campaign)

        _contact_type = d.pop("contactType", UNSET)
        contact_type: Union[Unset, CodesCodeidGetSourceCodeWithExpandContactType]
        if isinstance(_contact_type, Unset):
            contact_type = UNSET
        else:
            contact_type = CodesCodeidGetSourceCodeWithExpandContactType.from_dict(_contact_type)

        date_modified = d.pop("dateModified", UNSET)

        revenue_stream_id = d.pop("revenueStreamId", UNSET)

        _general_ledger_fund = d.pop("generalLedgerFund", UNSET)
        general_ledger_fund: Union[Unset, CodesCodeidGetSourceCodeWithExpandGeneralLedgerFund]
        if isinstance(_general_ledger_fund, Unset):
            general_ledger_fund = UNSET
        else:
            general_ledger_fund = CodesCodeidGetSourceCodeWithExpandGeneralLedgerFund.from_dict(_general_ledger_fund)

        _cost_center = d.pop("costCenter", UNSET)
        cost_center: Union[Unset, CodesCodeidGetSourceCodeWithExpandCostCenter]
        if isinstance(_cost_center, Unset):
            cost_center = UNSET
        else:
            cost_center = CodesCodeidGetSourceCodeWithExpandCostCenter.from_dict(_cost_center)

        _revenue_stream = d.pop("revenueStream", UNSET)
        revenue_stream: Union[Unset, CodesCodeidGetSourceCodeWithExpandRevenueStream]
        if isinstance(_revenue_stream, Unset):
            revenue_stream = UNSET
        else:
            revenue_stream = CodesCodeidGetSourceCodeWithExpandRevenueStream.from_dict(_revenue_stream)

        _mail_merge_template = d.pop("mailMergeTemplate", UNSET)
        mail_merge_template: Union[Unset, CodesCodeidGetSourceCodeWithExpandMailMergeTemplate]
        if isinstance(_mail_merge_template, Unset):
            mail_merge_template = UNSET
        else:
            mail_merge_template = CodesCodeidGetSourceCodeWithExpandMailMergeTemplate.from_dict(_mail_merge_template)

        is_source_code_applicable = d.pop("isSourceCodeApplicable", UNSET)

        codes_codeid_get_source_code_with_expand = cls(
            code_id=code_id,
            parent_code_id=parent_code_id,
            name=name,
            description=description,
            code_path=code_path,
            created_by_name=created_by_name,
            date_created=date_created,
            supported_entities=supported_entities,
            code_type=code_type,
            campaign=campaign,
            contact_type=contact_type,
            date_modified=date_modified,
            revenue_stream_id=revenue_stream_id,
            general_ledger_fund=general_ledger_fund,
            cost_center=cost_center,
            revenue_stream=revenue_stream,
            mail_merge_template=mail_merge_template,
            is_source_code_applicable=is_source_code_applicable,
        )

        codes_codeid_get_source_code_with_expand.additional_properties = d
        return codes_codeid_get_source_code_with_expand

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
