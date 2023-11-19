from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v15.enums.types.local_services_lead_status import (
    LocalServicesLeadStatusEnum,
)
from google.ads.googleads.v15.enums.types.local_services_lead_type import (
    LocalServicesLeadTypeEnum,
)

_M = TypeVar("_M")

class ContactDetails(proto.Message):
    phone_number: str
    email: str
    consumer_name: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        phone_number: str = ...,
        email: str = ...,
        consumer_name: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["phone_number", "email", "consumer_name"]) -> bool: ...  # type: ignore[override]

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
        lead_charged: bool = ...
    ) -> None: ...
    def __contains__(self, key: Literal["resource_name", "id", "category_id", "service_id", "contact_details", "lead_type", "lead_status", "creation_date_time", "locale", "note", "lead_charged"]) -> bool: ...  # type: ignore[override]

class Note(proto.Message):
    edit_date_time: str
    description: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        edit_date_time: str = ...,
        description: str = ...
    ) -> None: ...
    def __contains__(self, key: Literal["edit_date_time", "description"]) -> bool: ...  # type: ignore[override]
