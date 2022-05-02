import proto
from _typeshed import Incomplete

from google.ads.googleads.v10.enums.types import (
    gender_type as gender_type,
    income_range_type as income_range_type,
    parental_status_type as parental_status_type,
)

__protobuf__: Incomplete

class AudienceDimension(proto.Message):
    age: Incomplete
    gender: Incomplete
    household_income: Incomplete
    parental_status: Incomplete
    audience_segments: Incomplete

class AudienceExclusionDimension(proto.Message):
    exclusions: Incomplete

class ExclusionSegment(proto.Message):
    user_list: Incomplete

class AgeDimension(proto.Message):
    age_ranges: Incomplete
    include_undetermined: Incomplete

class AgeSegment(proto.Message):
    min_age: Incomplete
    max_age: Incomplete

class GenderDimension(proto.Message):
    genders: Incomplete
    include_undetermined: Incomplete

class HouseholdIncomeDimension(proto.Message):
    income_ranges: Incomplete
    include_undetermined: Incomplete

class ParentalStatusDimension(proto.Message):
    parental_statuses: Incomplete
    include_undetermined: Incomplete

class AudienceSegmentDimension(proto.Message):
    segments: Incomplete

class AudienceSegment(proto.Message):
    user_list: Incomplete
    user_interest: Incomplete
    life_event: Incomplete
    detailed_demographic: Incomplete
    custom_audience: Incomplete

class UserListSegment(proto.Message):
    user_list: Incomplete

class UserInterestSegment(proto.Message):
    user_interest_category: Incomplete

class LifeEventSegment(proto.Message):
    life_event: Incomplete

class DetailedDemographicSegment(proto.Message):
    detailed_demographic: Incomplete

class CustomAudienceSegment(proto.Message):
    custom_audience: Incomplete
