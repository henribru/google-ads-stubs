import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import local_services
from google.ads.googleads.v19.enums.types import local_services_business_registration_check_rejection_reason, local_services_business_registration_type, local_services_insurance_rejection_reason, local_services_license_rejection_reason, local_services_verification_artifact_status, local_services_verification_artifact_type

__protobuf__: Incomplete

class LocalServicesVerificationArtifact(proto.Message):
    resource_name: str
    id: int
    creation_date_time: str
    status: local_services_verification_artifact_status.LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus
    artifact_type: local_services_verification_artifact_type.LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType
    background_check_verification_artifact: BackgroundCheckVerificationArtifact
    insurance_verification_artifact: InsuranceVerificationArtifact
    license_verification_artifact: LicenseVerificationArtifact
    business_registration_check_verification_artifact: BusinessRegistrationCheckVerificationArtifact

class BackgroundCheckVerificationArtifact(proto.Message):
    case_url: str
    final_adjudication_date_time: str

class InsuranceVerificationArtifact(proto.Message):
    amount_micros: int
    rejection_reason: local_services_insurance_rejection_reason.LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    insurance_document_readonly: local_services.LocalServicesDocumentReadOnly
    expiration_date_time: str

class LicenseVerificationArtifact(proto.Message):
    license_type: str
    license_number: str
    licensee_first_name: str
    licensee_last_name: str
    rejection_reason: local_services_license_rejection_reason.LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason
    license_document_readonly: local_services.LocalServicesDocumentReadOnly
    expiration_date_time: str

class BusinessRegistrationCheckVerificationArtifact(proto.Message):
    registration_type: local_services_business_registration_type.LocalServicesBusinessRegistrationTypeEnum.LocalServicesBusinessRegistrationType
    check_id: str
    rejection_reason: local_services_business_registration_check_rejection_reason.LocalServicesBusinessRegistrationCheckRejectionReasonEnum.LocalServicesBusinessRegistrationCheckRejectionReason
    registration_number: BusinessRegistrationNumber
    registration_document: BusinessRegistrationDocument

class BusinessRegistrationNumber(proto.Message):
    number: str

class BusinessRegistrationDocument(proto.Message):
    document_readonly: local_services.LocalServicesDocumentReadOnly
