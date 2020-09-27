# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Iterable as typing___Iterable, Optional as typing___Optional

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    Int32Value as google___protobuf___wrappers_pb2___Int32Value,
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v2.proto.enums.policy_topic_entry_type_pb2 import (
    PolicyTopicEntryTypeEnum as google___ads___googleads___v2___enums___policy_topic_entry_type_pb2___PolicyTopicEntryTypeEnum,
)
from google.ads.google_ads.v2.proto.enums.policy_topic_evidence_destination_mismatch_url_type_pb2 import (
    PolicyTopicEvidenceDestinationMismatchUrlTypeEnum as google___ads___googleads___v2___enums___policy_topic_evidence_destination_mismatch_url_type_pb2___PolicyTopicEvidenceDestinationMismatchUrlTypeEnum,
)
from google.ads.google_ads.v2.proto.enums.policy_topic_evidence_destination_not_working_device_pb2 import (
    PolicyTopicEvidenceDestinationNotWorkingDeviceEnum as google___ads___googleads___v2___enums___policy_topic_evidence_destination_not_working_device_pb2___PolicyTopicEvidenceDestinationNotWorkingDeviceEnum,
)
from google.ads.google_ads.v2.proto.enums.policy_topic_evidence_destination_not_working_dns_error_type_pb2 import (
    PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum as google___ads___googleads___v2___enums___policy_topic_evidence_destination_not_working_dns_error_type_pb2___PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class PolicyViolationKey(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def policy_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def violating_text(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        policy_name: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        violating_text: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "policy_name", b"policy_name", "violating_text", b"violating_text"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "policy_name", b"policy_name", "violating_text", b"violating_text"
        ],
    ) -> None: ...

type___PolicyViolationKey = PolicyViolationKey

class PolicyValidationParameter(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def ignorable_policy_topics(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        google___protobuf___wrappers_pb2___StringValue
    ]: ...
    @property
    def exempt_policy_violation_keys(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___PolicyViolationKey
    ]: ...
    def __init__(
        self,
        *,
        ignorable_policy_topics: typing___Optional[
            typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
        ] = None,
        exempt_policy_violation_keys: typing___Optional[
            typing___Iterable[type___PolicyViolationKey]
        ] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "exempt_policy_violation_keys",
            b"exempt_policy_violation_keys",
            "ignorable_policy_topics",
            b"ignorable_policy_topics",
        ],
    ) -> None: ...

type___PolicyValidationParameter = PolicyValidationParameter

class PolicyTopicEntry(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type: google___ads___googleads___v2___enums___policy_topic_entry_type_pb2___PolicyTopicEntryTypeEnum.PolicyTopicEntryTypeValue = ...
    @property
    def topic(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def evidences(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___PolicyTopicEvidence
    ]: ...
    @property
    def constraints(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___PolicyTopicConstraint
    ]: ...
    def __init__(
        self,
        *,
        topic: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        type: typing___Optional[
            google___ads___googleads___v2___enums___policy_topic_entry_type_pb2___PolicyTopicEntryTypeEnum.PolicyTopicEntryTypeValue
        ] = None,
        evidences: typing___Optional[
            typing___Iterable[type___PolicyTopicEvidence]
        ] = None,
        constraints: typing___Optional[
            typing___Iterable[type___PolicyTopicConstraint]
        ] = None,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions___Literal["topic", b"topic"]
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "constraints",
            b"constraints",
            "evidences",
            b"evidences",
            "topic",
            b"topic",
            "type",
            b"type",
        ],
    ) -> None: ...

type___PolicyTopicEntry = PolicyTopicEntry

class PolicyTopicEvidence(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TextList(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def texts(
            self,
        ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
            google___protobuf___wrappers_pb2___StringValue
        ]: ...
        def __init__(
            self,
            *,
            texts: typing___Optional[
                typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
            ] = None,
        ) -> None: ...
        def ClearField(
            self, field_name: typing_extensions___Literal["texts", b"texts"]
        ) -> None: ...
    type___TextList = TextList
    class WebsiteList(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def websites(
            self,
        ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
            google___protobuf___wrappers_pb2___StringValue
        ]: ...
        def __init__(
            self,
            *,
            websites: typing___Optional[
                typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
            ] = None,
        ) -> None: ...
        def ClearField(
            self, field_name: typing_extensions___Literal["websites", b"websites"]
        ) -> None: ...
    type___WebsiteList = WebsiteList
    class DestinationTextList(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def destination_texts(
            self,
        ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
            google___protobuf___wrappers_pb2___StringValue
        ]: ...
        def __init__(
            self,
            *,
            destination_texts: typing___Optional[
                typing___Iterable[google___protobuf___wrappers_pb2___StringValue]
            ] = None,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
                "destination_texts", b"destination_texts"
            ],
        ) -> None: ...
    type___DestinationTextList = DestinationTextList
    class DestinationMismatch(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        url_types: google___protobuf___internal___containers___RepeatedScalarFieldContainer[
            google___ads___googleads___v2___enums___policy_topic_evidence_destination_mismatch_url_type_pb2___PolicyTopicEvidenceDestinationMismatchUrlTypeEnum.PolicyTopicEvidenceDestinationMismatchUrlTypeValue
        ] = ...
        def __init__(
            self,
            *,
            url_types: typing___Optional[
                typing___Iterable[
                    google___ads___googleads___v2___enums___policy_topic_evidence_destination_mismatch_url_type_pb2___PolicyTopicEvidenceDestinationMismatchUrlTypeEnum.PolicyTopicEvidenceDestinationMismatchUrlTypeValue
                ]
            ] = None,
        ) -> None: ...
        def ClearField(
            self, field_name: typing_extensions___Literal["url_types", b"url_types"]
        ) -> None: ...
    type___DestinationMismatch = DestinationMismatch
    class DestinationNotWorking(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        device: google___ads___googleads___v2___enums___policy_topic_evidence_destination_not_working_device_pb2___PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDeviceValue = ...
        dns_error_type: google___ads___googleads___v2___enums___policy_topic_evidence_destination_not_working_dns_error_type_pb2___PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum.PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeValue = ...
        @property
        def expanded_url(self) -> google___protobuf___wrappers_pb2___StringValue: ...
        @property
        def last_checked_date_time(
            self,
        ) -> google___protobuf___wrappers_pb2___StringValue: ...
        @property
        def http_error_code(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
        def __init__(
            self,
            *,
            expanded_url: typing___Optional[
                google___protobuf___wrappers_pb2___StringValue
            ] = None,
            device: typing___Optional[
                google___ads___googleads___v2___enums___policy_topic_evidence_destination_not_working_device_pb2___PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDeviceValue
            ] = None,
            last_checked_date_time: typing___Optional[
                google___protobuf___wrappers_pb2___StringValue
            ] = None,
            dns_error_type: typing___Optional[
                google___ads___googleads___v2___enums___policy_topic_evidence_destination_not_working_dns_error_type_pb2___PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum.PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeValue
            ] = None,
            http_error_code: typing___Optional[
                google___protobuf___wrappers_pb2___Int64Value
            ] = None,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions___Literal[
                "dns_error_type",
                b"dns_error_type",
                "expanded_url",
                b"expanded_url",
                "http_error_code",
                b"http_error_code",
                "last_checked_date_time",
                b"last_checked_date_time",
                "reason",
                b"reason",
            ],
        ) -> builtin___bool: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
                "device",
                b"device",
                "dns_error_type",
                b"dns_error_type",
                "expanded_url",
                b"expanded_url",
                "http_error_code",
                b"http_error_code",
                "last_checked_date_time",
                b"last_checked_date_time",
                "reason",
                b"reason",
            ],
        ) -> None: ...
        def WhichOneof(
            self, oneof_group: typing_extensions___Literal["reason", b"reason"]
        ) -> typing_extensions___Literal["dns_error_type", "http_error_code"]: ...
    type___DestinationNotWorking = DestinationNotWorking
    @property
    def website_list(self) -> type___PolicyTopicEvidence.WebsiteList: ...
    @property
    def text_list(self) -> type___PolicyTopicEvidence.TextList: ...
    @property
    def language_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def destination_text_list(
        self,
    ) -> type___PolicyTopicEvidence.DestinationTextList: ...
    @property
    def destination_mismatch(
        self,
    ) -> type___PolicyTopicEvidence.DestinationMismatch: ...
    @property
    def destination_not_working(
        self,
    ) -> type___PolicyTopicEvidence.DestinationNotWorking: ...
    def __init__(
        self,
        *,
        website_list: typing___Optional[type___PolicyTopicEvidence.WebsiteList] = None,
        text_list: typing___Optional[type___PolicyTopicEvidence.TextList] = None,
        language_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        destination_text_list: typing___Optional[
            type___PolicyTopicEvidence.DestinationTextList
        ] = None,
        destination_mismatch: typing___Optional[
            type___PolicyTopicEvidence.DestinationMismatch
        ] = None,
        destination_not_working: typing___Optional[
            type___PolicyTopicEvidence.DestinationNotWorking
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "destination_mismatch",
            b"destination_mismatch",
            "destination_not_working",
            b"destination_not_working",
            "destination_text_list",
            b"destination_text_list",
            "language_code",
            b"language_code",
            "text_list",
            b"text_list",
            "value",
            b"value",
            "website_list",
            b"website_list",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "destination_mismatch",
            b"destination_mismatch",
            "destination_not_working",
            b"destination_not_working",
            "destination_text_list",
            b"destination_text_list",
            "language_code",
            b"language_code",
            "text_list",
            b"text_list",
            "value",
            b"value",
            "website_list",
            b"website_list",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["value", b"value"]
    ) -> typing_extensions___Literal[
        "website_list",
        "text_list",
        "language_code",
        "destination_text_list",
        "destination_mismatch",
        "destination_not_working",
    ]: ...

type___PolicyTopicEvidence = PolicyTopicEvidence

class PolicyTopicConstraint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class CountryConstraintList(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def total_targeted_countries(
            self,
        ) -> google___protobuf___wrappers_pb2___Int32Value: ...
        @property
        def countries(
            self,
        ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
            type___PolicyTopicConstraint.CountryConstraint
        ]: ...
        def __init__(
            self,
            *,
            total_targeted_countries: typing___Optional[
                google___protobuf___wrappers_pb2___Int32Value
            ] = None,
            countries: typing___Optional[
                typing___Iterable[type___PolicyTopicConstraint.CountryConstraint]
            ] = None,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions___Literal[
                "total_targeted_countries", b"total_targeted_countries"
            ],
        ) -> builtin___bool: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
                "countries",
                b"countries",
                "total_targeted_countries",
                b"total_targeted_countries",
            ],
        ) -> None: ...
    type___CountryConstraintList = CountryConstraintList
    class ResellerConstraint(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        def __init__(self,) -> None: ...
    type___ResellerConstraint = ResellerConstraint
    class CountryConstraint(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        @property
        def country_criterion(
            self,
        ) -> google___protobuf___wrappers_pb2___StringValue: ...
        def __init__(
            self,
            *,
            country_criterion: typing___Optional[
                google___protobuf___wrappers_pb2___StringValue
            ] = None,
        ) -> None: ...
        def HasField(
            self,
            field_name: typing_extensions___Literal[
                "country_criterion", b"country_criterion"
            ],
        ) -> builtin___bool: ...
        def ClearField(
            self,
            field_name: typing_extensions___Literal[
                "country_criterion", b"country_criterion"
            ],
        ) -> None: ...
    type___CountryConstraint = CountryConstraint
    @property
    def country_constraint_list(
        self,
    ) -> type___PolicyTopicConstraint.CountryConstraintList: ...
    @property
    def reseller_constraint(
        self,
    ) -> type___PolicyTopicConstraint.ResellerConstraint: ...
    @property
    def certificate_missing_in_country_list(
        self,
    ) -> type___PolicyTopicConstraint.CountryConstraintList: ...
    @property
    def certificate_domain_mismatch_in_country_list(
        self,
    ) -> type___PolicyTopicConstraint.CountryConstraintList: ...
    def __init__(
        self,
        *,
        country_constraint_list: typing___Optional[
            type___PolicyTopicConstraint.CountryConstraintList
        ] = None,
        reseller_constraint: typing___Optional[
            type___PolicyTopicConstraint.ResellerConstraint
        ] = None,
        certificate_missing_in_country_list: typing___Optional[
            type___PolicyTopicConstraint.CountryConstraintList
        ] = None,
        certificate_domain_mismatch_in_country_list: typing___Optional[
            type___PolicyTopicConstraint.CountryConstraintList
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "certificate_domain_mismatch_in_country_list",
            b"certificate_domain_mismatch_in_country_list",
            "certificate_missing_in_country_list",
            b"certificate_missing_in_country_list",
            "country_constraint_list",
            b"country_constraint_list",
            "reseller_constraint",
            b"reseller_constraint",
            "value",
            b"value",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "certificate_domain_mismatch_in_country_list",
            b"certificate_domain_mismatch_in_country_list",
            "certificate_missing_in_country_list",
            b"certificate_missing_in_country_list",
            "country_constraint_list",
            b"country_constraint_list",
            "reseller_constraint",
            b"reseller_constraint",
            "value",
            b"value",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["value", b"value"]
    ) -> typing_extensions___Literal[
        "country_constraint_list",
        "reseller_constraint",
        "certificate_missing_in_country_list",
        "certificate_domain_mismatch_in_country_list",
    ]: ...

type___PolicyTopicConstraint = PolicyTopicConstraint
