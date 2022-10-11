import proto
from _typeshed import Incomplete

from google.ads.googleads.v11.enums.types import (
    policy_topic_entry_type as policy_topic_entry_type,
    policy_topic_evidence_destination_mismatch_url_type as policy_topic_evidence_destination_mismatch_url_type,
    policy_topic_evidence_destination_not_working_device as policy_topic_evidence_destination_not_working_device,
    policy_topic_evidence_destination_not_working_dns_error_type as policy_topic_evidence_destination_not_working_dns_error_type,
)

__protobuf__: Incomplete

class PolicyViolationKey(proto.Message):
    policy_name: Incomplete
    violating_text: Incomplete

class PolicyValidationParameter(proto.Message):
    ignorable_policy_topics: Incomplete
    exempt_policy_violation_keys: Incomplete

class PolicyTopicEntry(proto.Message):
    topic: Incomplete
    type_: Incomplete
    evidences: Incomplete
    constraints: Incomplete

class PolicyTopicEvidence(proto.Message):
    class TextList(proto.Message):
        texts: Incomplete

    class WebsiteList(proto.Message):
        websites: Incomplete

    class DestinationTextList(proto.Message):
        destination_texts: Incomplete

    class DestinationMismatch(proto.Message):
        url_types: Incomplete

    class DestinationNotWorking(proto.Message):
        expanded_url: Incomplete
        device: Incomplete
        last_checked_date_time: Incomplete
        dns_error_type: Incomplete
        http_error_code: Incomplete
    website_list: Incomplete
    text_list: Incomplete
    language_code: Incomplete
    destination_text_list: Incomplete
    destination_mismatch: Incomplete
    destination_not_working: Incomplete

class PolicyTopicConstraint(proto.Message):
    class CountryConstraintList(proto.Message):
        total_targeted_countries: Incomplete
        countries: Incomplete

    class ResellerConstraint(proto.Message): ...

    class CountryConstraint(proto.Message):
        country_criterion: Incomplete
    country_constraint_list: Incomplete
    reseller_constraint: Incomplete
    certificate_missing_in_country_list: Incomplete
    certificate_domain_mismatch_in_country_list: Incomplete
