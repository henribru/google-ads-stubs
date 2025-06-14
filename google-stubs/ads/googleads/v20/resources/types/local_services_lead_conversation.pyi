import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import local_services_conversation_type, local_services_participant_type
from typing import MutableSequence

__protobuf__: Incomplete

class LocalServicesLeadConversation(proto.Message):
    resource_name: str
    id: int
    conversation_channel: local_services_conversation_type.LocalServicesLeadConversationTypeEnum.ConversationType
    participant_type: local_services_participant_type.LocalServicesParticipantTypeEnum.ParticipantType
    lead: str
    event_date_time: str
    phone_call_details: PhoneCallDetails
    message_details: MessageDetails

class PhoneCallDetails(proto.Message):
    call_duration_millis: int
    call_recording_url: str

class MessageDetails(proto.Message):
    text: str
    attachment_urls: MutableSequence[str]
