from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.local_services_conversation_type import (
    LocalServicesLeadConversationTypeEnum,
)
from google.ads.googleads.v16.enums.types.local_services_participant_type import (
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
        message_details: MessageDetails = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "conversation_channel",
            "participant_type",
            "lead",
            "event_date_time",
            "phone_call_details",
            "message_details",
        ],
    ) -> bool: ...

class MessageDetails(proto.Message):
    text: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        text: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["text"]
    ) -> bool: ...

class PhoneCallDetails(proto.Message):
    call_duration_millis: int
    call_recording_url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        call_duration_millis: int = ...,
        call_recording_url: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["call_duration_millis", "call_recording_url"]
    ) -> bool: ...
