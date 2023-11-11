from typing import Any

import proto

from google.ads.googleads.v15.enums.types.local_services_conversation_type import (
    LocalServicesLeadConversationTypeEnum,
)
from google.ads.googleads.v15.enums.types.local_services_participant_type import (
    LocalServicesParticipantTypeEnum,
)

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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
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
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        text: str = ...
    ) -> None: ...

class PhoneCallDetails(proto.Message):
    call_duration_millis: int
    call_recording_url: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        call_duration_millis: int = ...,
        call_recording_url: str = ...
    ) -> None: ...
