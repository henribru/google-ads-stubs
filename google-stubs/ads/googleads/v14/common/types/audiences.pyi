from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v14.enums.types.gender_type import GenderTypeEnum
from google.ads.googleads.v14.enums.types.income_range_type import IncomeRangeTypeEnum
from google.ads.googleads.v14.enums.types.parental_status_type import (
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
        include_undetermined: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["age_ranges", "include_undetermined"]
    ) -> bool: ...

class AgeSegment(proto.Message):
    min_age: int
    max_age: int
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        min_age: int = ...,
        max_age: int = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["min_age", "max_age"]
    ) -> bool: ...

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
        audience_segments: AudienceSegmentDimension = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "age", "gender", "household_income", "parental_status", "audience_segments"
        ],
    ) -> bool: ...

class AudienceExclusionDimension(proto.Message):
    exclusions: MutableSequence[ExclusionSegment]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        exclusions: MutableSequence[ExclusionSegment] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["exclusions"]
    ) -> bool: ...

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
        custom_audience: CustomAudienceSegment = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "user_list",
            "user_interest",
            "life_event",
            "detailed_demographic",
            "custom_audience",
        ],
    ) -> bool: ...

class AudienceSegmentDimension(proto.Message):
    segments: MutableSequence[AudienceSegment]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        segments: MutableSequence[AudienceSegment] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["segments"]
    ) -> bool: ...

class CustomAudienceSegment(proto.Message):
    custom_audience: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        custom_audience: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["custom_audience"]
    ) -> bool: ...

class DetailedDemographicSegment(proto.Message):
    detailed_demographic: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        detailed_demographic: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["detailed_demographic"]
    ) -> bool: ...

class ExclusionSegment(proto.Message):
    user_list: UserListSegment
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_list: UserListSegment = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["user_list"]
    ) -> bool: ...

class GenderDimension(proto.Message):
    genders: MutableSequence[GenderTypeEnum.GenderType]
    include_undetermined: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        genders: MutableSequence[GenderTypeEnum.GenderType] = ...,
        include_undetermined: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["genders", "include_undetermined"]
    ) -> bool: ...

class HouseholdIncomeDimension(proto.Message):
    income_ranges: MutableSequence[IncomeRangeTypeEnum.IncomeRangeType]
    include_undetermined: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        income_ranges: MutableSequence[IncomeRangeTypeEnum.IncomeRangeType] = ...,
        include_undetermined: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["income_ranges", "include_undetermined"]
    ) -> bool: ...

class LifeEventSegment(proto.Message):
    life_event: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        life_event: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["life_event"]
    ) -> bool: ...

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
        include_undetermined: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["parental_statuses", "include_undetermined"]
    ) -> bool: ...

class UserInterestSegment(proto.Message):
    user_interest_category: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_interest_category: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["user_interest_category"]
    ) -> bool: ...

class UserListSegment(proto.Message):
    user_list: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        user_list: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["user_list"]
    ) -> bool: ...
