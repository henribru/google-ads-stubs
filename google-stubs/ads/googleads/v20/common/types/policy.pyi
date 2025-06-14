import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.enums.types import policy_topic_entry_type, policy_topic_evidence_destination_mismatch_url_type, policy_topic_evidence_destination_not_working_device, policy_topic_evidence_destination_not_working_dns_error_type
from typing import MutableSequence

__protobuf__: Incomplete

class PolicyViolationKey(proto.Message):
    policy_name: str
    violating_text: str

class PolicyValidationParameter(proto.Message):
    ignorable_policy_topics: MutableSequence[str]
    exempt_policy_violation_keys: MutableSequence['PolicyViolationKey']

class PolicyTopicEntry(proto.Message):
    topic: str
    type_: policy_topic_entry_type.PolicyTopicEntryTypeEnum.PolicyTopicEntryType
    evidences: MutableSequence['PolicyTopicEvidence']
    constraints: MutableSequence['PolicyTopicConstraint']

class PolicyTopicEvidence(proto.Message):
    class TextList(proto.Message):
        texts: MutableSequence[str]
    class WebsiteList(proto.Message):
        websites: MutableSequence[str]
    class DestinationTextList(proto.Message):
        destination_texts: MutableSequence[str]
    class DestinationMismatch(proto.Message):
        url_types: MutableSequence[policy_topic_evidence_destination_mismatch_url_type.PolicyTopicEvidenceDestinationMismatchUrlTypeEnum.PolicyTopicEvidenceDestinationMismatchUrlType]
    class DestinationNotWorking(proto.Message):
        expanded_url: str
        device: policy_topic_evidence_destination_not_working_device.PolicyTopicEvidenceDestinationNotWorkingDeviceEnum.PolicyTopicEvidenceDestinationNotWorkingDevice
        last_checked_date_time: str
        dns_error_type: policy_topic_evidence_destination_not_working_dns_error_type.PolicyTopicEvidenceDestinationNotWorkingDnsErrorTypeEnum.PolicyTopicEvidenceDestinationNotWorkingDnsErrorType
        http_error_code: int
    website_list: WebsiteList
    text_list: TextList
    language_code: str
    destination_text_list: DestinationTextList
    destination_mismatch: DestinationMismatch
    destination_not_working: DestinationNotWorking

class PolicyTopicConstraint(proto.Message):
    class CountryConstraintList(proto.Message):
        total_targeted_countries: int
        countries: MutableSequence['PolicyTopicConstraint.CountryConstraint']
    class ResellerConstraint(proto.Message): ...
    class CountryConstraint(proto.Message):
        country_criterion: str
    country_constraint_list: CountryConstraintList
    reseller_constraint: ResellerConstraint
    certificate_missing_in_country_list: CountryConstraintList
    certificate_domain_mismatch_in_country_list: CountryConstraintList
