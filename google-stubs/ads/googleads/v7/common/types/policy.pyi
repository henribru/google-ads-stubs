from typing import Any

import proto

from google.ads.googleads.v7.enums.types import (
    policy_topic_entry_type as policy_topic_entry_type,
    policy_topic_evidence_destination_mismatch_url_type as policy_topic_evidence_destination_mismatch_url_type,
    policy_topic_evidence_destination_not_working_device as policy_topic_evidence_destination_not_working_device,
    policy_topic_evidence_destination_not_working_dns_error_type as policy_topic_evidence_destination_not_working_dns_error_type,
)

__protobuf__: Any

class PolicyViolationKey(proto.Message):
    policy_name: Any
    violating_text: Any

class PolicyValidationParameter(proto.Message):
    ignorable_policy_topics: Any
    exempt_policy_violation_keys: Any

class PolicyTopicEntry(proto.Message):
    topic: Any
    type_: Any
    evidences: Any
    constraints: Any

class PolicyTopicEvidence(proto.Message):
    class TextList(proto.Message):
        texts: Any
    class WebsiteList(proto.Message):
        websites: Any
    class DestinationTextList(proto.Message):
        destination_texts: Any
    class DestinationMismatch(proto.Message):
        url_types: Any
    class DestinationNotWorking(proto.Message):
        expanded_url: Any
        device: Any
        last_checked_date_time: Any
        dns_error_type: Any
        http_error_code: Any
    website_list: Any
    text_list: Any
    language_code: Any
    destination_text_list: Any
    destination_mismatch: Any
    destination_not_working: Any

class PolicyTopicConstraint(proto.Message):
    class CountryConstraintList(proto.Message):
        total_targeted_countries: Any
        countries: Any
    class ResellerConstraint(proto.Message): ...
    class CountryConstraint(proto.Message):
        country_criterion: Any
    country_constraint_list: Any
    reseller_constraint: Any
    certificate_missing_in_country_list: Any
    certificate_domain_mismatch_in_country_list: Any
