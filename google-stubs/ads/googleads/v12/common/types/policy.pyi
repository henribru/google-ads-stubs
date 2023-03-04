from collections.abc import MutableSequence
from typing import Any

import proto

from google.ads.googleads.v12.enums.types.policy_topic_entry_type import (
    PolicyTopicEntryTypeEnum,
)
from google.ads.googleads.v12.enums.types.policy_topic_evidence_destination_mismatch_url_type import (
    PolicyTopicEvidenceDestinationMismatchUrlTypeEnum,
)
from google.ads.googleads.v12.enums.types.policy_topic_evidence_destination_not_working_device import (
    PolicyTopicEvidenceDestinationNotWorkingDeviceEnum,
)
from google.ads.googleads.v12.enums.types.policy_topic_evidence_destination_not_working_dns_error_type import (
    PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum,
)

class PolicyTopicConstraint(proto.Message):
    class CountryConstraint(proto.Message):
        country_criterion: str
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            country_criterion: str = ...,
        ) -> None: ...

    class CountryConstraintList(proto.Message):
        total_targeted_countries: int
        countries: MutableSequence[PolicyTopicConstraint.CountryConstraint]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            total_targeted_countries: int = ...,
            countries: MutableSequence[PolicyTopicConstraint.CountryConstraint] = ...,
        ) -> None: ...

    class ResellerConstraint(proto.Message):
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
        ) -> None: ...
        ...
    country_constraint_list: PolicyTopicConstraint.CountryConstraintList
    reseller_constraint: PolicyTopicConstraint.ResellerConstraint
    certificate_missing_in_country_list: PolicyTopicConstraint.CountryConstraintList
    certificate_domain_mismatch_in_country_list: PolicyTopicConstraint.CountryConstraintList
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        country_constraint_list: PolicyTopicConstraint.CountryConstraintList = ...,
        reseller_constraint: PolicyTopicConstraint.ResellerConstraint = ...,
        certificate_missing_in_country_list: PolicyTopicConstraint.CountryConstraintList = ...,
        certificate_domain_mismatch_in_country_list: PolicyTopicConstraint.CountryConstraintList = ...,
    ) -> None: ...

class PolicyTopicEntry(proto.Message):
    topic: str
    type_: PolicyTopicEntryTypeEnum.PolicyTopicEntryType
    evidences: MutableSequence[PolicyTopicEvidence]
    constraints: MutableSequence[PolicyTopicConstraint]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        topic: str = ...,
        type_: PolicyTopicEntryTypeEnum.PolicyTopicEntryType = ...,
        evidences: MutableSequence[PolicyTopicEvidence] = ...,
        constraints: MutableSequence[PolicyTopicConstraint] = ...,
    ) -> None: ...

class PolicyTopicEvidence(proto.Message):
    class DestinationMismatch(proto.Message):
        url_types: MutableSequence[
            PolicyTopicEvidenceDestinationMismatchUrlTypeEnum.PolicyTopicEvidenceDestinationMismatchUrlType
        ]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            url_types: MutableSequence[
                PolicyTopicEvidenceDestinationMismatchUrlTypeEnum.PolicyTopicEvidenceDestinationMismatchUrlType
            ] = ...,
        ) -> None: ...

    class DestinationNotWorking(proto.Message):
        expanded_url: str
        device: PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice
        last_checked_date_time: str
        dns_error_type: PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum.PolicyTopicEvidenceDestinationNotWorkingDnsErrorType
        http_error_code: int
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            expanded_url: str = ...,
            device: PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice = ...,
            last_checked_date_time: str = ...,
            dns_error_type: PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum.PolicyTopicEvidenceDestinationNotWorkingDnsErrorType = ...,
            http_error_code: int = ...,
        ) -> None: ...

    class DestinationTextList(proto.Message):
        destination_texts: MutableSequence[str]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            destination_texts: MutableSequence[str] = ...,
        ) -> None: ...

    class TextList(proto.Message):
        texts: MutableSequence[str]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            texts: MutableSequence[str] = ...,
        ) -> None: ...

    class WebsiteList(proto.Message):
        websites: MutableSequence[str]
        def __init__(
            self,
            mapping: Any | None = ...,
            *,
            ignore_unknown_fields: bool = ...,
            websites: MutableSequence[str] = ...,
        ) -> None: ...
    website_list: PolicyTopicEvidence.WebsiteList
    text_list: PolicyTopicEvidence.TextList
    language_code: str
    destination_text_list: PolicyTopicEvidence.DestinationTextList
    destination_mismatch: PolicyTopicEvidence.DestinationMismatch
    destination_not_working: PolicyTopicEvidence.DestinationNotWorking
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        website_list: PolicyTopicEvidence.WebsiteList = ...,
        text_list: PolicyTopicEvidence.TextList = ...,
        language_code: str = ...,
        destination_text_list: PolicyTopicEvidence.DestinationTextList = ...,
        destination_mismatch: PolicyTopicEvidence.DestinationMismatch = ...,
        destination_not_working: PolicyTopicEvidence.DestinationNotWorking = ...,
    ) -> None: ...

class PolicyValidationParameter(proto.Message):
    ignorable_policy_topics: MutableSequence[str]
    exempt_policy_violation_keys: MutableSequence[PolicyViolationKey]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        ignorable_policy_topics: MutableSequence[str] = ...,
        exempt_policy_violation_keys: MutableSequence[PolicyViolationKey] = ...,
    ) -> None: ...

class PolicyViolationKey(proto.Message):
    policy_name: str
    violating_text: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        policy_name: str = ...,
        violating_text: str = ...,
    ) -> None: ...
