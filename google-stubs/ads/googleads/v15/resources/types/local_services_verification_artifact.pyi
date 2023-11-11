from typing import Any

import proto

from google.ads.googleads.v15.common.types.local_services import (
    LocalServicesDocumentReadOnly,
)
from google.ads.googleads.v15.enums.types.local_services_insurance_rejection_reason import (
    LocalServicesInsuranceRejectionReasonEnum,
)
from google.ads.googleads.v15.enums.types.local_services_license_rejection_reason import (
    LocalServicesLicenseRejectionReasonEnum,
)
from google.ads.googleads.v15.enums.types.local_services_verification_artifact_status import (
    LocalServicesVerificationArtifactStatusEnum,
)
from google.ads.googleads.v15.enums.types.local_services_verification_artifact_type import (
    LocalServicesVerificationArtifactTypeEnum,
)

class BackgroundCheckVerificationArtifact(proto.Message):
    case_url: str
    final_adjudication_date_time: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        case_url: str = ...,
        final_adjudication_date_time: str = ...
    ) -> None: ...

class InsuranceVerificationArtifact(proto.Message):
    amount_micros: int
    rejection_reason: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    insurance_document_readonly: LocalServicesDocumentReadOnly
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        amount_micros: int = ...,
        rejection_reason: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason = ...,
        insurance_document_readonly: LocalServicesDocumentReadOnly = ...
    ) -> None: ...

class LicenseVerificationArtifact(proto.Message):
    license_type: str
    license_number: str
    licensee_first_name: str
    licensee_last_name: str
    rejection_reason: LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason
    license_document_readonly: LocalServicesDocumentReadOnly
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        license_type: str = ...,
        license_number: str = ...,
        licensee_first_name: str = ...,
        licensee_last_name: str = ...,
        rejection_reason: LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason = ...,
        license_document_readonly: LocalServicesDocumentReadOnly = ...
    ) -> None: ...

class LocalServicesVerificationArtifact(proto.Message):
    resource_name: str
    id: int
    creation_date_time: str
    status: LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus
    artifact_type: LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType
    background_check_verification_artifact: BackgroundCheckVerificationArtifact
    insurance_verification_artifact: InsuranceVerificationArtifact
    license_verification_artifact: LicenseVerificationArtifact
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        resource_name: str = ...,
        id: int = ...,
        creation_date_time: str = ...,
        status: LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus = ...,
        artifact_type: LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType = ...,
        background_check_verification_artifact: BackgroundCheckVerificationArtifact = ...,
        insurance_verification_artifact: InsuranceVerificationArtifact = ...,
        license_verification_artifact: LicenseVerificationArtifact = ...
    ) -> None: ...
