# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import Iterable as typing___Iterable, Optional as typing___Optional

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v5.proto.enums.keyword_plan_competition_level_pb2 import (
    KeywordPlanCompetitionLevelEnum as google___ads___googleads___v5___enums___keyword_plan_competition_level_pb2___KeywordPlanCompetitionLevelEnum,
)
from google.ads.google_ads.v5.proto.enums.month_of_year_pb2 import (
    MonthOfYearEnum as google___ads___googleads___v5___enums___month_of_year_pb2___MonthOfYearEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class KeywordPlanHistoricalMetrics(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    competition: google___ads___googleads___v5___enums___keyword_plan_competition_level_pb2___KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevelValue = ...
    @property
    def avg_monthly_searches(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def monthly_search_volumes(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___MonthlySearchVolume
    ]: ...
    @property
    def competition_index(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def low_top_of_page_bid_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def high_top_of_page_bid_micros(
        self,
    ) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        avg_monthly_searches: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        monthly_search_volumes: typing___Optional[
            typing___Iterable[type___MonthlySearchVolume]
        ] = None,
        competition: typing___Optional[
            google___ads___googleads___v5___enums___keyword_plan_competition_level_pb2___KeywordPlanCompetitionLevelEnum.KeywordPlanCompetitionLevelValue
        ] = None,
        competition_index: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        low_top_of_page_bid_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
        high_top_of_page_bid_micros: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "avg_monthly_searches",
            b"avg_monthly_searches",
            "competition_index",
            b"competition_index",
            "high_top_of_page_bid_micros",
            b"high_top_of_page_bid_micros",
            "low_top_of_page_bid_micros",
            b"low_top_of_page_bid_micros",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "avg_monthly_searches",
            b"avg_monthly_searches",
            "competition",
            b"competition",
            "competition_index",
            b"competition_index",
            "high_top_of_page_bid_micros",
            b"high_top_of_page_bid_micros",
            "low_top_of_page_bid_micros",
            b"low_top_of_page_bid_micros",
            "monthly_search_volumes",
            b"monthly_search_volumes",
        ],
    ) -> None: ...

type___KeywordPlanHistoricalMetrics = KeywordPlanHistoricalMetrics

class MonthlySearchVolume(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    month: google___ads___googleads___v5___enums___month_of_year_pb2___MonthOfYearEnum.MonthOfYearValue = ...
    @property
    def year(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    @property
    def monthly_searches(self) -> google___protobuf___wrappers_pb2___Int64Value: ...
    def __init__(
        self,
        *,
        year: typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        month: typing___Optional[
            google___ads___googleads___v5___enums___month_of_year_pb2___MonthOfYearEnum.MonthOfYearValue
        ] = None,
        monthly_searches: typing___Optional[
            google___protobuf___wrappers_pb2___Int64Value
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "monthly_searches", b"monthly_searches", "year", b"year"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "month", b"month", "monthly_searches", b"monthly_searches", "year", b"year"
        ],
    ) -> None: ...

type___MonthlySearchVolume = MonthlySearchVolume
