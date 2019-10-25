# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v1.proto.common.dates_pb2 import (
    DateRange as google___ads___googleads___v1___common___dates_pb2___DateRange,
)

from google.ads.google_ads.v1.proto.enums.keyword_plan_forecast_interval_pb2 import (
    KeywordPlanForecastIntervalEnum as google___ads___googleads___v1___enums___keyword_plan_forecast_interval_pb2___KeywordPlanForecastIntervalEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    Int64Value as google___protobuf___wrappers_pb2___Int64Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from typing import (
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class KeywordPlan(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    resource_name = ... # type: typing___Text

    @property
    def id(self) -> google___protobuf___wrappers_pb2___Int64Value: ...

    @property
    def name(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def forecast_period(self) -> KeywordPlanForecastPeriod: ...

    def __init__(self,
        *,
        resource_name : typing___Optional[typing___Text] = None,
        id : typing___Optional[google___protobuf___wrappers_pb2___Int64Value] = None,
        name : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        forecast_period : typing___Optional[KeywordPlanForecastPeriod] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> KeywordPlan: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"forecast_period",u"id",u"name"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"forecast_period",u"id",u"name",u"resource_name"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"forecast_period",b"forecast_period",u"id",b"id",u"name",b"name"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"forecast_period",b"forecast_period",u"id",b"id",u"name",b"name",u"resource_name",b"resource_name"]) -> None: ...

class KeywordPlanForecastPeriod(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    date_interval = ... # type: google___ads___googleads___v1___enums___keyword_plan_forecast_interval_pb2___KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval

    @property
    def date_range(self) -> google___ads___googleads___v1___common___dates_pb2___DateRange: ...

    def __init__(self,
        *,
        date_interval : typing___Optional[google___ads___googleads___v1___enums___keyword_plan_forecast_interval_pb2___KeywordPlanForecastIntervalEnum.KeywordPlanForecastInterval] = None,
        date_range : typing___Optional[google___ads___googleads___v1___common___dates_pb2___DateRange] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> KeywordPlanForecastPeriod: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"date_interval",u"date_range",u"interval"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"date_interval",u"date_range",u"interval"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"date_interval",b"date_interval",u"date_range",b"date_range",u"interval",b"interval"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"date_interval",b"date_interval",u"date_range",b"date_range",u"interval",b"interval"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"interval",b"interval"]) -> typing_extensions___Literal["date_interval","date_range"]: ...
