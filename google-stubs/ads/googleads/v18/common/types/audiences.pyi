import proto
from _typeshed import Incomplete
from google.ads.googleads.v18.enums.types import gender_type, income_range_type, parental_status_type
from typing import MutableSequence

__protobuf__: Incomplete

class AudienceDimension(proto.Message):
    age: AgeDimension
    gender: GenderDimension
    household_income: HouseholdIncomeDimension
    parental_status: ParentalStatusDimension
    audience_segments: AudienceSegmentDimension

class AudienceExclusionDimension(proto.Message):
    exclusions: MutableSequence['ExclusionSegment']

class ExclusionSegment(proto.Message):
    user_list: UserListSegment

class AgeDimension(proto.Message):
    age_ranges: MutableSequence['AgeSegment']
    include_undetermined: bool

class AgeSegment(proto.Message):
    min_age: int
    max_age: int

class GenderDimension(proto.Message):
    genders: MutableSequence[gender_type.GenderTypeEnum.GenderType]
    include_undetermined: bool

class HouseholdIncomeDimension(proto.Message):
    income_ranges: MutableSequence[income_range_type.IncomeRangeTypeEnum.IncomeRangeType]
    include_undetermined: bool

class ParentalStatusDimension(proto.Message):
    parental_statuses: MutableSequence[parental_status_type.ParentalStatusTypeEnum.ParentalStatusType]
    include_undetermined: bool

class AudienceSegmentDimension(proto.Message):
    segments: MutableSequence['AudienceSegment']

class AudienceSegment(proto.Message):
    user_list: UserListSegment
    user_interest: UserInterestSegment
    life_event: LifeEventSegment
    detailed_demographic: DetailedDemographicSegment
    custom_audience: CustomAudienceSegment

class UserListSegment(proto.Message):
    user_list: str

class UserInterestSegment(proto.Message):
    user_interest_category: str

class LifeEventSegment(proto.Message):
    life_event: str

class DetailedDemographicSegment(proto.Message):
    detailed_demographic: str

class CustomAudienceSegment(proto.Message):
    custom_audience: str
