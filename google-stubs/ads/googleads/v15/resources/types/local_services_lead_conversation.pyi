from collections.abc import Mapping
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.local_services_conversation_type import (
    LocalServicesLeadConversationTypeEnum,
)
from google.ads.googleads.v15.enums.types.local_services_participant_type import (
    LocalServicesParticipantTypeEnum,
)

_M = TypeVar("_M")

class LocalServicesLeadConversation(proto.Message):
    resource_name: str
    id: int
    conversation_channel: LocalServicesLeadConversationTypeEnum.ConversationType
    participant_type: LocalServicesParticipantTypeEnum.ParticipantType
    lead: str
    event_date_time: str
    phone_call_details: PhoneCallDetails
    message_details: MessageDetails
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        conversation_channel: LocalServicesLeadConversationTypeEnum.ConversationType = ...,
        participant_type: LocalServicesParticipantTypeEnum.ParticipantType = ...,
        lead: str = ...,
        event_date_time: str = ...,
        phone_call_details: PhoneCallDetails = ...,
        message_details: MessageDetails = ...
    ) -> None: ...

class MessageDetails(proto.Message):
    text: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        text: str = ...
    ) -> None: ...

class PhoneCallDetails(proto.Message):
    call_duration_millis: int
    call_recording_url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        call_duration_millis: int = ...,
        call_recording_url: str = ...
    ) -> None: ...
