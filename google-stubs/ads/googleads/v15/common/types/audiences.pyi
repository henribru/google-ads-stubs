from collections.abc import Mapping, MutableSequence
from typing import Any, TypeVar

import google.protobuf.message
import proto

from google.ads.googleads.v15.enums.types.gender_type import GenderTypeEnum
from google.ads.googleads.v15.enums.types.income_range_type import IncomeRangeTypeEnum
from google.ads.googleads.v15.enums.types.parental_status_type import (
    ParentalStatusTypeEnum,
)

_M = TypeVar("_M")

class AgeDimension(proto.Message):
    age_ranges: MutableSequence[AgeSegment]
    include_undetermined: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        age_ranges: MutableSequence[AgeSegment] = ...,
        include_undetermined: bool = ...
    ) -> None: ...

class AgeSegment(proto.Message):
    min_age: int
    max_age: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
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
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        age: AgeDimension = ...,
        gender: GenderDimension = ...,
        household_income: HouseholdIncomeDimension = ...,
        parental_status: ParentalStatusDimension = ...,
        audience_segments: AudienceSegmentDimension = ...
    ) -> None: ...

class AudienceExclusionDimension(proto.Message):
    exclusions: MutableSequence[ExclusionSegment]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        exclusions: MutableSequence[ExclusionSegment] = ...
    ) -> None: ...

class AudienceSegment(proto.Message):
    user_list: UserListSegment
    user_interest: UserInterestSegment
    life_event: LifeEventSegment
    detailed_demographic: DetailedDemographicSegment
    custom_audience: CustomAudienceSegment
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_list: UserListSegment = ...,
        user_interest: UserInterestSegment = ...,
        life_event: LifeEventSegment = ...,
        detailed_demographic: DetailedDemographicSegment = ...,
        custom_audience: CustomAudienceSegment = ...
    ) -> None: ...

class AudienceSegmentDimension(proto.Message):
    segments: MutableSequence[AudienceSegment]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        segments: MutableSequence[AudienceSegment] = ...
    ) -> None: ...

class CustomAudienceSegment(proto.Message):
    custom_audience: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        custom_audience: str = ...
    ) -> None: ...

class DetailedDemographicSegment(proto.Message):
    detailed_demographic: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        detailed_demographic: str = ...
    ) -> None: ...

class ExclusionSegment(proto.Message):
    user_list: UserListSegment
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_list: UserListSegment = ...
    ) -> None: ...

class GenderDimension(proto.Message):
    genders: MutableSequence[GenderTypeEnum.GenderType]
    include_undetermined: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        genders: MutableSequence[GenderTypeEnum.GenderType] = ...,
        include_undetermined: bool = ...
    ) -> None: ...

class HouseholdIncomeDimension(proto.Message):
    income_ranges: MutableSequence[IncomeRangeTypeEnum.IncomeRangeType]
    include_undetermined: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        income_ranges: MutableSequence[IncomeRangeTypeEnum.IncomeRangeType] = ...,
        include_undetermined: bool = ...
    ) -> None: ...

class LifeEventSegment(proto.Message):
    life_event: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        life_event: str = ...
    ) -> None: ...

class ParentalStatusDimension(proto.Message):
    parental_statuses: MutableSequence[ParentalStatusTypeEnum.ParentalStatusType]
    include_undetermined: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        parental_statuses: MutableSequence[
            ParentalStatusTypeEnum.ParentalStatusType
        ] = ...,
        include_undetermined: bool = ...
    ) -> None: ...

class UserInterestSegment(proto.Message):
    user_interest_category: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_interest_category: str = ...
    ) -> None: ...

class UserListSegment(proto.Message):
    user_list: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_list: str = ...
    ) -> None: ...
