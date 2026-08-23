from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v25.enums.types.local_services_lead_credit_state import (
    LocalServicesCreditStateEnum,
)
from google.ads.googleads.v25.enums.types.local_services_lead_status import (
    LocalServicesLeadStatusEnum,
)
from google.ads.googleads.v25.enums.types.local_services_lead_type import (
    LocalServicesLeadTypeEnum,
)

_M = TypeVar("_M")

class ContactDetails(proto.Message):
    phone_number: str
    consumer_name: str
    phone_number_extension: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        phone_number: str = ...,
        consumer_name: str = ...,
        phone_number_extension: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["phone_number", "consumer_name", "phone_number_extension"]
    ) -> bool: ...

class CreditDetails(proto.Message):
    credit_state: LocalServicesCreditStateEnum.CreditState
    credit_state_last_update_date_time: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        credit_state: LocalServicesCreditStateEnum.CreditState = ...,
        credit_state_last_update_date_time: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["credit_state", "credit_state_last_update_date_time"]
    ) -> bool: ...

class LocalServicesLead(proto.Message):
    resource_name: str
    id: int
    category_id: str
    service_id: str
    contact_details: ContactDetails
    lead_type: LocalServicesLeadTypeEnum.LeadType
    lead_status: LocalServicesLeadStatusEnum.LeadStatus
    creation_date_time: str
    locale: str
    note: Note
    lead_charged: bool
    credit_details: CreditDetails
    lead_feedback_submitted: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        category_id: str = ...,
        service_id: str = ...,
        contact_details: ContactDetails = ...,
        lead_type: LocalServicesLeadTypeEnum.LeadType = ...,
        lead_status: LocalServicesLeadStatusEnum.LeadStatus = ...,
        creation_date_time: str = ...,
        locale: str = ...,
        note: Note = ...,
        lead_charged: bool = ...,
        credit_details: CreditDetails = ...,
        lead_feedback_submitted: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "category_id",
            "service_id",
            "contact_details",
            "lead_type",
            "lead_status",
            "creation_date_time",
            "locale",
            "note",
            "lead_charged",
            "credit_details",
            "lead_feedback_submitted",
        ],
    ) -> bool: ...

class Note(proto.Message):
    edit_date_time: str
    description: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        edit_date_time: str = ...,
        description: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["edit_date_time", "description"]
    ) -> bool: ...
