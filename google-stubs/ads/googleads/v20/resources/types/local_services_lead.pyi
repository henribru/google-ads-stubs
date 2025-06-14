import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import local_services_lead_credit_state, local_services_lead_status, local_services_lead_type

__protobuf__: Incomplete

class LocalServicesLead(proto.Message):
    resource_name: str
    id: int
    category_id: str
    service_id: str
    contact_details: ContactDetails
    lead_type: local_services_lead_type.LocalServicesLeadTypeEnum.LeadType
    lead_status: local_services_lead_status.LocalServicesLeadStatusEnum.LeadStatus
    creation_date_time: str
    locale: str
    note: Note
    lead_charged: bool
    credit_details: CreditDetails
    lead_feedback_submitted: bool

class ContactDetails(proto.Message):
    phone_number: str
    email: str
    consumer_name: str

class Note(proto.Message):
    edit_date_time: str
    description: str

class CreditDetails(proto.Message):
    credit_state: local_services_lead_credit_state.LocalServicesCreditStateEnum.CreditState
    credit_state_last_update_date_time: str
