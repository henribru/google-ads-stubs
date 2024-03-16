from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.policy_topic_entry_type import (
    PolicyTopicEntryTypeEnum,
)
from google.ads.googleads.v16.enums.types.policy_topic_evidence_destination_mismatch_url_type import (
    PolicyTopicEvidenceDestinationMismatchUrlTypeEnum,
)
from google.ads.googleads.v16.enums.types.policy_topic_evidence_destination_not_working_device import (
    PolicyTopicEvidenceDestinationNotWorkingDeviceEnum,
)
from google.ads.googleads.v16.enums.types.policy_topic_evidence_destination_not_working_dns_error_type import (
    PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum,
)

_M = TypeVar("_M")

class PolicyTopicConstraint(proto.Message):
    class CountryConstraint(proto.Message):
        country_criterion: str
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            country_criterion: str = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["country_criterion"]
        ) -> bool: ...

    class CountryConstraintList(proto.Message):
        total_targeted_countries: int
        countries: MutableSequence[PolicyTopicConstraint.CountryConstraint]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            total_targeted_countries: int = ...,
            countries: MutableSequence[PolicyTopicConstraint.CountryConstraint] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["total_targeted_countries", "countries"]
        ) -> bool: ...

    class ResellerConstraint(proto.Message):
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: NoReturn
        ) -> bool: ...

    country_constraint_list: PolicyTopicConstraint.CountryConstraintList
    reseller_constraint: PolicyTopicConstraint.ResellerConstraint
    certificate_missing_in_country_list: PolicyTopicConstraint.CountryConstraintList
    certificate_domain_mismatch_in_country_list: (
        PolicyTopicConstraint.CountryConstraintList
    )
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        country_constraint_list: PolicyTopicConstraint.CountryConstraintList = ...,
        reseller_constraint: PolicyTopicConstraint.ResellerConstraint = ...,
        certificate_missing_in_country_list: PolicyTopicConstraint.CountryConstraintList = ...,
        certificate_domain_mismatch_in_country_list: PolicyTopicConstraint.CountryConstraintList = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "country_constraint_list",
            "reseller_constraint",
            "certificate_missing_in_country_list",
            "certificate_domain_mismatch_in_country_list",
        ],
    ) -> bool: ...

class PolicyTopicEntry(proto.Message):
    topic: str
    type_: PolicyTopicEntryTypeEnum.PolicyTopicEntryType
    evidences: MutableSequence[PolicyTopicEvidence]
    constraints: MutableSequence[PolicyTopicConstraint]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        topic: str = ...,
        type_: PolicyTopicEntryTypeEnum.PolicyTopicEntryType = ...,
        evidences: MutableSequence[PolicyTopicEvidence] = ...,
        constraints: MutableSequence[PolicyTopicConstraint] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["topic", "type_", "evidences", "constraints"]
    ) -> bool: ...

class PolicyTopicEvidence(proto.Message):
    class DestinationMismatch(proto.Message):
        url_types: MutableSequence[
            PolicyTopicEvidenceDestinationMismatchUrlTypeEnum.PolicyTopicEvidenceDestinationMismatchUrlType
        ]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            url_types: MutableSequence[
                PolicyTopicEvidenceDestinationMismatchUrlTypeEnum.PolicyTopicEvidenceDestinationMismatchUrlType
            ] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["url_types"]
        ) -> bool: ...

    class DestinationNotWorking(proto.Message):
        expanded_url: str
        device: PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice
        last_checked_date_time: str
        dns_error_type: PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum.PolicyTopicEvidenceDestinationNotWorkingDnsErrorType
        http_error_code: int
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            expanded_url: str = ...,
            device: PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice = ...,
            last_checked_date_time: str = ...,
            dns_error_type: PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum.PolicyTopicEvidenceDestinationNotWorkingDnsErrorType = ...,
            http_error_code: int = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self,
            key: Literal[
                "expanded_url",
                "device",
                "last_checked_date_time",
                "dns_error_type",
                "http_error_code",
            ],
        ) -> bool: ...

    class DestinationTextList(proto.Message):
        destination_texts: MutableSequence[str]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            destination_texts: MutableSequence[str] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["destination_texts"]
        ) -> bool: ...

    class TextList(proto.Message):
        texts: MutableSequence[str]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            texts: MutableSequence[str] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["texts"]
        ) -> bool: ...

    class WebsiteList(proto.Message):
        websites: MutableSequence[str]
        def __init__(
            self: _M,
            mapping: _M | Mapping | google.protobuf.message.Message | None = None,
            *,
            ignore_unknown_fields: bool = False,
            websites: MutableSequence[str] = ...,
        ) -> None: ...
        def __contains__(  # type: ignore[override]
            self, key: Literal["websites"]
        ) -> bool: ...

    website_list: PolicyTopicEvidence.WebsiteList
    text_list: PolicyTopicEvidence.TextList
    language_code: str
    destination_text_list: PolicyTopicEvidence.DestinationTextList
    destination_mismatch: PolicyTopicEvidence.DestinationMismatch
    destination_not_working: PolicyTopicEvidence.DestinationNotWorking
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        website_list: PolicyTopicEvidence.WebsiteList = ...,
        text_list: PolicyTopicEvidence.TextList = ...,
        language_code: str = ...,
        destination_text_list: PolicyTopicEvidence.DestinationTextList = ...,
        destination_mismatch: PolicyTopicEvidence.DestinationMismatch = ...,
        destination_not_working: PolicyTopicEvidence.DestinationNotWorking = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "website_list",
            "text_list",
            "language_code",
            "destination_text_list",
            "destination_mismatch",
            "destination_not_working",
        ],
    ) -> bool: ...

class PolicyValidationParameter(proto.Message):
    ignorable_policy_topics: MutableSequence[str]
    exempt_policy_violation_keys: MutableSequence[PolicyViolationKey]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        ignorable_policy_topics: MutableSequence[str] = ...,
        exempt_policy_violation_keys: MutableSequence[PolicyViolationKey] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["ignorable_policy_topics", "exempt_policy_violation_keys"]
    ) -> bool: ...

class PolicyViolationKey(proto.Message):
    policy_name: str
    violating_text: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        policy_name: str = ...,
        violating_text: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["policy_name", "violating_text"]
    ) -> bool: ...
