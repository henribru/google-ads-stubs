import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import local_services_lead_credit_issuance_decision, local_services_lead_survey_answer, local_services_lead_survey_dissatisfied_reason, local_services_lead_survey_satisfied_reason
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

class SurveySatisfied(proto.Message):
    survey_satisfied_reason: local_services_lead_survey_satisfied_reason.LocalServicesLeadSurveySatisfiedReasonEnum.SurveySatisfiedReason
    other_reason_comment: str

class SurveyDissatisfied(proto.Message):
    survey_dissatisfied_reason: local_services_lead_survey_dissatisfied_reason.LocalServicesLeadSurveyDissatisfiedReasonEnum.SurveyDissatisfiedReason
    other_reason_comment: str

class ProvideLeadFeedbackRequest(proto.Message):
    resource_name: str
    survey_answer: local_services_lead_survey_answer.LocalServicesLeadSurveyAnswerEnum.SurveyAnswer
    survey_satisfied: SurveySatisfied
    survey_dissatisfied: SurveyDissatisfied

class ProvideLeadFeedbackResponse(proto.Message):
    credit_issuance_decision: local_services_lead_credit_issuance_decision.LocalServicesLeadCreditIssuanceDecisionEnum.CreditIssuanceDecision
