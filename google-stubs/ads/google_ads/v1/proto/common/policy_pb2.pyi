# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.enums.policy_topic_entry_type_pb2 import (
    PolicyTopicEntryTypeEnum as google___ads___googleads___v1___enums___policy_topic_entry_type_pb2___PolicyTopicEntryTypeEnum,
)

from google.ads.google_ads.v1.proto.enums.policy_topic_evidence_destination_mismatch_url_type_pb2 import (
    PolicyTopicEvidenceDestinationMismatchUrlTypeEnum as google___ads___googleads___v1___enums___policy_topic_evidence_destination_mismatch_url_type_pb2___PolicyTopicEvidenceDestinationMismatchUrlTypeEnum,
)

from google.ads.google_ads.v1.proto.enums.policy_topic_evidence_destination_not_working_device_pb2 import (
    PolicyTopicEvidenceDestinationNotWorkingDeviceEnum as google___ads___googleads___v1___enums___policy_topic_evidence_destination_not_working_device_pb2___PolicyTopicEvidenceDestinationNotWorkingDeviceEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
    RepeatedScalarFieldContainer as google___protobuf___internal___containers___RepeatedScalarFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    Int32Value as google___protobuf___wrappers_pb2___Int32Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class PolicyViolationKey(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def policy_name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def violating_text(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        policy_name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        violating_text : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PolicyViolationKey: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"policy_name",u"violating_text"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"policy_name",u"violating_text"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"policy_name",b"policy_name",u"violating_text",b"violating_text"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"policy_name",b"policy_name",u"violating_text",b"violating_text"]) -> None: ...

class PolicyValidationParameter(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def ignorable_policy_topics(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

    @property
    def exempt_policy_violation_keys(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[PolicyViolationKey]: ...

    def __init__(self,
        *,
        ignorable_policy_topics : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
        exempt_policy_violation_keys : typing___Optional[typing___Iterable[PolicyViolationKey]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PolicyValidationParameter: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"exempt_policy_violation_keys",u"ignorable_policy_topics"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"exempt_policy_violation_keys",b"exempt_policy_violation_keys",u"ignorable_policy_topics",b"ignorable_policy_topics"]) -> None: ...

class PolicyTopicEntry(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    type = ... # type: google___ads___googleads___v1___enums___policy_topic_entry_type_pb2___PolicyTopicEntryTypeEnum.PolicyTopicEntryType

    @property
    def topic(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def evidences(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[PolicyTopicEvidence]: ...

    @property
    def constraints(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[PolicyTopicConstraint]: ...

    def __init__(self,
        *,
        topic : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        type : typing___Optional[google___ads___googleads___v1___enums___policy_topic_entry_type_pb2___PolicyTopicEntryTypeEnum.PolicyTopicEntryType] = None,
        evidences : typing___Optional[typing___Iterable[PolicyTopicEvidence]] = None,
        constraints : typing___Optional[typing___Iterable[PolicyTopicConstraint]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PolicyTopicEntry: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"topic"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"constraints",u"evidences",u"topic",u"type"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"topic",b"topic"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"constraints",b"constraints",u"evidences",b"evidences",u"topic",b"topic",u"type",b"type"]) -> None: ...

class PolicyTopicEvidence(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class TextList(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def texts(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

        def __init__(self,
            *,
            texts : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> PolicyTopicEvidence.TextList: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"texts"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"texts",b"texts"]) -> None: ...

    class WebsiteList(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def websites(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

        def __init__(self,
            *,
            websites : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> PolicyTopicEvidence.WebsiteList: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"websites"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"websites",b"websites"]) -> None: ...

    class DestinationTextList(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def destination_texts(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[google___protobuf___wrappers_pb2___StringValue]: ...

        def __init__(self,
            *,
            destination_texts : typing___Optional[typing___Iterable[google___protobuf___wrappers_pb2___StringValue]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> PolicyTopicEvidence.DestinationTextList: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"destination_texts"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"destination_texts",b"destination_texts"]) -> None: ...

    class DestinationMismatch(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        url_types = ... # type: google___protobuf___internal___containers___RepeatedScalarFieldContainer[google___ads___googleads___v1___enums___policy_topic_evidence_destination_mismatch_url_type_pb2___PolicyTopicEvidenceDestinationMismatchUrlTypeEnum.PolicyTopicEvidenceDestinationMismatchUrlType]

        def __init__(self,
            *,
            url_types : typing___Optional[typing___Iterable[google___ads___googleads___v1___enums___policy_topic_evidence_destination_mismatch_url_type_pb2___PolicyTopicEvidenceDestinationMismatchUrlTypeEnum.PolicyTopicEvidenceDestinationMismatchUrlType]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> PolicyTopicEvidence.DestinationMismatch: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def ClearField(self, field_name: typing_extensions___Literal[u"url_types"]) -> None: ...
        else:
            def ClearField(self, field_name: typing_extensions___Literal[u"url_types",b"url_types"]) -> None: ...

    class DestinationNotWorking(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
        device = ... # type: google___ads___googleads___v1___enums___policy_topic_evidence_destination_not_working_device_pb2___PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice

        @property
        def expanded_url(self) -> google___protobuf___wrappers_pb2___StringValue: ...

        @property
        def last_checked_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...

        def __init__(self,
            *,
            expanded_url : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
            device : typing___Optional[google___ads___googleads___v1___enums___policy_topic_evidence_destination_not_working_device_pb2___PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice] = None,
            last_checked_date_time : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> PolicyTopicEvidence.DestinationNotWorking: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"expanded_url",u"last_checked_date_time"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"device",u"expanded_url",u"last_checked_date_time"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"expanded_url",b"expanded_url",u"last_checked_date_time",b"last_checked_date_time"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"device",b"device",u"expanded_url",b"expanded_url",u"last_checked_date_time",b"last_checked_date_time"]) -> None: ...


    @property
    def http_code(self) -> google___protobuf___wrappers_pb2___Int32Value: ...

    @property
    def website_list(self) -> PolicyTopicEvidence.WebsiteList: ...

    @property
    def text_list(self) -> PolicyTopicEvidence.TextList: ...

    @property
    def language_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def destination_text_list(self) -> PolicyTopicEvidence.DestinationTextList: ...

    @property
    def destination_mismatch(self) -> PolicyTopicEvidence.DestinationMismatch: ...

    @property
    def destination_not_working(self) -> PolicyTopicEvidence.DestinationNotWorking: ...

    def __init__(self,
        *,
        http_code : typing___Optional[google___protobuf___wrappers_pb2___Int32Value] = None,
        website_list : typing___Optional[PolicyTopicEvidence.WebsiteList] = None,
        text_list : typing___Optional[PolicyTopicEvidence.TextList] = None,
        language_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        destination_text_list : typing___Optional[PolicyTopicEvidence.DestinationTextList] = None,
        destination_mismatch : typing___Optional[PolicyTopicEvidence.DestinationMismatch] = None,
        destination_not_working : typing___Optional[PolicyTopicEvidence.DestinationNotWorking] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PolicyTopicEvidence: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"destination_mismatch",u"destination_not_working",u"destination_text_list",u"http_code",u"language_code",u"text_list",u"value",u"website_list"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"destination_mismatch",u"destination_not_working",u"destination_text_list",u"http_code",u"language_code",u"text_list",u"value",u"website_list"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"destination_mismatch",b"destination_mismatch",u"destination_not_working",b"destination_not_working",u"destination_text_list",b"destination_text_list",u"http_code",b"http_code",u"language_code",b"language_code",u"text_list",b"text_list",u"value",b"value",u"website_list",b"website_list"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"destination_mismatch",b"destination_mismatch",u"destination_not_working",b"destination_not_working",u"destination_text_list",b"destination_text_list",u"http_code",b"http_code",u"language_code",b"language_code",u"text_list",b"text_list",u"value",b"value",u"website_list",b"website_list"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"value",b"value"]) -> typing_extensions___Literal["http_code","website_list","text_list","language_code","destination_text_list","destination_mismatch","destination_not_working"]: ...

class PolicyTopicConstraint(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class CountryConstraintList(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def total_targeted_countries(self) -> google___protobuf___wrappers_pb2___Int32Value: ...

        @property
        def countries(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[PolicyTopicConstraint.CountryConstraint]: ...

        def __init__(self,
            *,
            total_targeted_countries : typing___Optional[google___protobuf___wrappers_pb2___Int32Value] = None,
            countries : typing___Optional[typing___Iterable[PolicyTopicConstraint.CountryConstraint]] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> PolicyTopicConstraint.CountryConstraintList: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"total_targeted_countries"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"countries",u"total_targeted_countries"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"total_targeted_countries",b"total_targeted_countries"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"countries",b"countries",u"total_targeted_countries",b"total_targeted_countries"]) -> None: ...

    class ResellerConstraint(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        def __init__(self,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> PolicyTopicConstraint.ResellerConstraint: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

    class CountryConstraint(google___protobuf___message___Message):
        DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

        @property
        def country_criterion(self) -> google___protobuf___wrappers_pb2___StringValue: ...

        def __init__(self,
            *,
            country_criterion : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
            ) -> None: ...
        @classmethod
        def FromString(cls, s: bytes) -> PolicyTopicConstraint.CountryConstraint: ...
        def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
        if sys.version_info >= (3,):
            def HasField(self, field_name: typing_extensions___Literal[u"country_criterion"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"country_criterion"]) -> None: ...
        else:
            def HasField(self, field_name: typing_extensions___Literal[u"country_criterion",b"country_criterion"]) -> bool: ...
            def ClearField(self, field_name: typing_extensions___Literal[u"country_criterion",b"country_criterion"]) -> None: ...


    @property
    def country_constraint_list(self) -> PolicyTopicConstraint.CountryConstraintList: ...

    @property
    def reseller_constraint(self) -> PolicyTopicConstraint.ResellerConstraint: ...

    @property
    def certificate_missing_in_country_list(self) -> PolicyTopicConstraint.CountryConstraintList: ...

    @property
    def certificate_domain_mismatch_in_country_list(self) -> PolicyTopicConstraint.CountryConstraintList: ...

    def __init__(self,
        *,
        country_constraint_list : typing___Optional[PolicyTopicConstraint.CountryConstraintList] = None,
        reseller_constraint : typing___Optional[PolicyTopicConstraint.ResellerConstraint] = None,
        certificate_missing_in_country_list : typing___Optional[PolicyTopicConstraint.CountryConstraintList] = None,
        certificate_domain_mismatch_in_country_list : typing___Optional[PolicyTopicConstraint.CountryConstraintList] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> PolicyTopicConstraint: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"certificate_domain_mismatch_in_country_list",u"certificate_missing_in_country_list",u"country_constraint_list",u"reseller_constraint",u"value"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"certificate_domain_mismatch_in_country_list",u"certificate_missing_in_country_list",u"country_constraint_list",u"reseller_constraint",u"value"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"certificate_domain_mismatch_in_country_list",b"certificate_domain_mismatch_in_country_list",u"certificate_missing_in_country_list",b"certificate_missing_in_country_list",u"country_constraint_list",b"country_constraint_list",u"reseller_constraint",b"reseller_constraint",u"value",b"value"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"certificate_domain_mismatch_in_country_list",b"certificate_domain_mismatch_in_country_list",u"certificate_missing_in_country_list",b"certificate_missing_in_country_list",u"country_constraint_list",b"country_constraint_list",u"reseller_constraint",b"reseller_constraint",u"value",b"value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"value",b"value"]) -> typing_extensions___Literal["country_constraint_list","reseller_constraint","certificate_missing_in_country_list","certificate_domain_mismatch_in_country_list"]: ...
