from google.ads.googleads.v22.enums.types.local_services_lead_survey_satisfied_reason import LocalServicesLeadSurveySatisfiedReasonEnum
from google.ads.googleads.v22.enums.types.local_services_lead_survey_dissatisfied_reason import LocalServicesLeadSurveyDissatisfiedReasonEnum
from google.ads.googleads.v22.enums.types.local_services_lead_credit_issuance_decision import LocalServicesLeadCreditIssuanceDecisionEnum
from google.ads.googleads.v22.enums.types.local_services_lead_survey_answer import LocalServicesLeadSurveyAnswerEnum
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
class ProvideLeadFeedbackRequest(proto.Message):
    resource_name: str
    survey_answer: LocalServicesLeadSurveyAnswerEnum.SurveyAnswer
    survey_satisfied: SurveySatisfied
    survey_dissatisfied: SurveyDissatisfied
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, resource_name: str = ..., survey_answer: LocalServicesLeadSurveyAnswerEnum.SurveyAnswer = ..., survey_satisfied: SurveySatisfied = ..., survey_dissatisfied: SurveyDissatisfied = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["resource_name", "survey_answer", "survey_satisfied", "survey_dissatisfied"]) -> bool: ...
class ProvideLeadFeedbackResponse(proto.Message):
    credit_issuance_decision: LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, credit_issuance_decision: LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["credit_issuance_decision"]) -> bool: ...
class SurveyDissatisfied(proto.Message):
    survey_dissatisfied_reason: LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason
    other_reason_comment: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, survey_dissatisfied_reason: LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason = ..., other_reason_comment: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["survey_dissatisfied_reason", "other_reason_comment"]) -> bool: ...
class SurveySatisfied(proto.Message):
    survey_satisfied_reason: LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason
    other_reason_comment: str
    def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = None, *, ignore_unknown_fields: bool = False, survey_satisfied_reason: LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason = ..., other_reason_comment: str = ...) -> None: ...
    def __contains__(  # type: ignore[override]
    self, key: Literal["survey_satisfied_reason", "other_reason_comment"]) -> bool: ...
