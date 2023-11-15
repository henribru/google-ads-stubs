from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

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
