from typing import Any

import proto

class LocalServicesInsuranceRejectionReasonEnum(proto.Message):
    class LocalServicesInsuranceRejectionReason(proto.Enum):
        UNSPECIFIED = 0
        UNKNOWN = 1
        BUSINESS_NAME_MISMATCH = 2
        INSURANCE_AMOUNT_INSUFFICIENT = 3
        EXPIRED = 4
        NO_SIGNATURE = 5
        NO_POLICY_NUMBER = 6
        NO_COMMERCIAL_GENERAL_LIABILITY = 7
        EDITABLE_FORMAT = 8
        CATEGORY_MISMATCH = 9
        MISSING_EXPIRATION_DATE = 10
        POOR_QUALITY = 11
        POTENTIALLY_EDITED = 12
        WRONG_DOCUMENT_TYPE = 13
        NON_FINAL = 14
        OTHER = 15
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
    ) -> None: ...
