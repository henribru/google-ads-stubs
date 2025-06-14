import proto
from _typeshed import Incomplete
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class AppendLeadConversationRequest(proto.Message):
    customer_id: str
    conversations: MutableSequence['Conversation']

class AppendLeadConversationResponse(proto.Message):
    responses: MutableSequence['ConversationOrError']

class Conversation(proto.Message):
    local_services_lead: str
    text: str

class ConversationOrError(proto.Message):
    local_services_lead_conversation: str
    partial_failure_error: status_pb2.Status
