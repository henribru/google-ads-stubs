from typing import Any

import proto

from google.ads.googleads.v11.enums.types.gender_type import GenderTypeEnum
from google.ads.googleads.v11.enums.types.income_range_type import IncomeRangeTypeEnum
from google.ads.googleads.v11.enums.types.parental_status_type import (
    ParentalStatusTypeEnum,
)

class AgeDimension(proto.Message):
    age_ranges: list[AgeSegment]
    include_undetermined: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        age_ranges: list[AgeSegment] = ...,
        include_undetermined: bool = ...
    ) -> None: ...

class AgeSegment(proto.Message):
    min_age: int
    max_age: int
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        min_age: int = ...,
        max_age: int = ...
    ) -> None: ...

class AudienceDimension(proto.Message):
    age: AgeDimension
    gender: GenderDimension
    household_income: HouseholdIncomeDimension
    parental_status: ParentalStatusDimension
    audience_segments: AudienceSegmentDimension
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        age: AgeDimension = ...,
        gender: GenderDimension = ...,
        household_income: HouseholdIncomeDimension = ...,
        parental_status: ParentalStatusDimension = ...,
        audience_segments: AudienceSegmentDimension = ...
    ) -> None: ...

class AudienceExclusionDimension(proto.Message):
    exclusions: list[ExclusionSegment]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        exclusions: list[ExclusionSegment] = ...
    ) -> None: ...

class AudienceSegment(proto.Message):
    user_list: UserListSegment
    user_interest: UserInterestSegment
    life_event: LifeEventSegment
    detailed_demographic: DetailedDemographicSegment
    custom_audience: CustomAudienceSegment
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        user_list: UserListSegment = ...,
        user_interest: UserInterestSegment = ...,
        life_event: LifeEventSegment = ...,
        detailed_demographic: DetailedDemographicSegment = ...,
        custom_audience: CustomAudienceSegment = ...
    ) -> None: ...

class AudienceSegmentDimension(proto.Message):
    segments: list[AudienceSegment]
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        segments: list[AudienceSegment] = ...
    ) -> None: ...

class CustomAudienceSegment(proto.Message):
    custom_audience: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        custom_audience: str = ...
    ) -> None: ...

class DetailedDemographicSegment(proto.Message):
    detailed_demographic: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        detailed_demographic: str = ...
    ) -> None: ...

class ExclusionSegment(proto.Message):
    user_list: UserListSegment
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        user_list: UserListSegment = ...
    ) -> None: ...

class GenderDimension(proto.Message):
    genders: list[GenderTypeEnum.GenderType]
    include_undetermined: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        genders: list[GenderTypeEnum.GenderType] = ...,
        include_undetermined: bool = ...
    ) -> None: ...

class HouseholdIncomeDimension(proto.Message):
    income_ranges: list[IncomeRangeTypeEnum.IncomeRangeType]
    include_undetermined: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        income_ranges: list[IncomeRangeTypeEnum.IncomeRangeType] = ...,
        include_undetermined: bool = ...
    ) -> None: ...

class LifeEventSegment(proto.Message):
    life_event: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        life_event: str = ...
    ) -> None: ...

class ParentalStatusDimension(proto.Message):
    parental_statuses: list[ParentalStatusTypeEnum.ParentalStatusType]
    include_undetermined: bool
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        parental_statuses: list[ParentalStatusTypeEnum.ParentalStatusType] = ...,
        include_undetermined: bool = ...
    ) -> None: ...

class UserInterestSegment(proto.Message):
    user_interest_category: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        user_interest_category: str = ...
    ) -> None: ...

class UserListSegment(proto.Message):
    user_list: str
    def __init__(
        self,
        mapping: Any | None = ...,
        *,
        ignore_unknown_fields: bool = ...,
        user_list: str = ...
    ) -> None: ...
