from typing import Any

import proto

class LocalServicesLicenseRejectionReasonEnum(proto.Message):
    class LocalServicesLicenseRejectionReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BUSINESS_NAME_MISMATCH = 2
        UNAUTHORIZED = 3
        EXPIRED = 4
        POOR_QUALITY = 5
        UNVERIFIABLE = 6
        WRONG_DOCUMENT_OR_ID = 7
        OTHER = 8
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
