from google.rpc.status_pb2 import Status
from collections.abc import MutableSequence
from collections.abc import MutableSequence
import proto
import google.protobuf.message
from typing import Any, TypeVar, NoReturn
from typing_extensions import Literal
from collections.abc import Mapping
_M = TypeVar("_M")
class AppendLeadConversationRequest(proto.Message):
    customer_id: str
    conversations: MutableSequence[Conversation]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, customer_id: str = ..., conversations: MutableSequence[Conversation] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["customer_id", "conversations"]) -> bool: ...
class AppendLeadConversationResponse(proto.Message):
    responses: MutableSequence[ConversationOrError]
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, responses: MutableSequence[ConversationOrError] = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["responses"]) -> bool: ...
class Conversation(proto.Message):
    local_services_lead: str
    text: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, local_services_lead: str = ..., text: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["local_services_lead", "text"]) -> bool: ...
class ConversationOrError(proto.Message):
    local_services_lead_conversation: str
    partial_failure_error: Status
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, local_services_lead_conversation: str = ..., partial_failure_error: Status = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["local_services_lead_conversation", "partial_failure_error"]) -> bool: ...
