from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

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

_M = TypeVar("_M")

class BackgroundCheckVerificationArtifact(proto.Message):
    case_url: str
    final_adjudication_date_time: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        case_url: str = ...,
        final_adjudication_date_time: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["case_url", "final_adjudication_date_time"]
    ) -> bool: ...

class InsuranceVerificationArtifact(proto.Message):
    amount_micros: int
    rejection_reason: (
        LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason
    )
    insurance_document_readonly: LocalServicesDocumentReadOnly
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        amount_micros: int = ...,
        rejection_reason: LocalServicesInsuranceRejectionReasonEnum.LocalServicesInsuranceRejectionReason = ...,
        insurance_document_readonly: LocalServicesDocumentReadOnly = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "amount_micros", "rejection_reason", "insurance_document_readonly"
        ],
    ) -> bool: ...

class LicenseVerificationArtifact(proto.Message):
    license_type: str
    license_number: str
    licensee_first_name: str
    licensee_last_name: str
    rejection_reason: (
        LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason
    )
    license_document_readonly: LocalServicesDocumentReadOnly
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        license_type: str = ...,
        license_number: str = ...,
        licensee_first_name: str = ...,
        licensee_last_name: str = ...,
        rejection_reason: LocalServicesLicenseRejectionReasonEnum.LocalServicesLicenseRejectionReason = ...,
        license_document_readonly: LocalServicesDocumentReadOnly = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "license_type",
            "license_number",
            "licensee_first_name",
            "licensee_last_name",
            "rejection_reason",
            "license_document_readonly",
        ],
    ) -> bool: ...

class LocalServicesVerificationArtifact(proto.Message):
    resource_name: str
    id: int
    creation_date_time: str
    status: LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus
    artifact_type: (
        LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType
    )
    background_check_verification_artifact: BackgroundCheckVerificationArtifact
    insurance_verification_artifact: InsuranceVerificationArtifact
    license_verification_artifact: LicenseVerificationArtifact
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        id: int = ...,
        creation_date_time: str = ...,
        status: LocalServicesVerificationArtifactStatusEnum.LocalServicesVerificationArtifactStatus = ...,
        artifact_type: LocalServicesVerificationArtifactTypeEnum.LocalServicesVerificationArtifactType = ...,
        background_check_verification_artifact: BackgroundCheckVerificationArtifact = ...,
        insurance_verification_artifact: InsuranceVerificationArtifact = ...,
        license_verification_artifact: LicenseVerificationArtifact = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "resource_name",
            "id",
            "creation_date_time",
            "status",
            "artifact_type",
            "background_check_verification_artifact",
            "insurance_verification_artifact",
            "license_verification_artifact",
        ],
    ) -> bool: ...
