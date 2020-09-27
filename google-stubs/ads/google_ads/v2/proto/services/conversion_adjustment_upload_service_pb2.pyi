# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
from google.protobuf.wrappers_pb2 import (
    DoubleValue as google___protobuf___wrappers_pb2___DoubleValue,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from google.rpc.status_pb2 import Status as google___rpc___status_pb2___Status
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v2.proto.enums.conversion_adjustment_type_pb2 import (
    ConversionAdjustmentTypeEnum as google___ads___googleads___v2___enums___conversion_adjustment_type_pb2___ConversionAdjustmentTypeEnum,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class UploadConversionAdjustmentsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    partial_failure: builtin___bool = ...
    validate_only: builtin___bool = ...
    @property
    def conversion_adjustments(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___ConversionAdjustment
    ]: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        conversion_adjustments: typing___Optional[
            typing___Iterable[type___ConversionAdjustment]
        ] = None,
        partial_failure: typing___Optional[builtin___bool] = None,
        validate_only: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "conversion_adjustments",
            b"conversion_adjustments",
            "customer_id",
            b"customer_id",
            "partial_failure",
            b"partial_failure",
            "validate_only",
            b"validate_only",
        ],
    ) -> None: ...

type___UploadConversionAdjustmentsRequest = UploadConversionAdjustmentsRequest

class UploadConversionAdjustmentsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def partial_failure_error(self) -> google___rpc___status_pb2___Status: ...
    @property
    def results(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___ConversionAdjustmentResult
    ]: ...
    def __init__(
        self,
        *,
        partial_failure_error: typing___Optional[
            google___rpc___status_pb2___Status
        ] = None,
        results: typing___Optional[
            typing___Iterable[type___ConversionAdjustmentResult]
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "partial_failure_error", b"partial_failure_error"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "partial_failure_error", b"partial_failure_error", "results", b"results"
        ],
    ) -> None: ...

type___UploadConversionAdjustmentsResponse = UploadConversionAdjustmentsResponse

class ConversionAdjustment(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    adjustment_type: google___ads___googleads___v2___enums___conversion_adjustment_type_pb2___ConversionAdjustmentTypeEnum.ConversionAdjustmentTypeValue = ...
    @property
    def conversion_action(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def adjustment_date_time(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def restatement_value(self) -> type___RestatementValue: ...
    @property
    def gclid_date_time_pair(self) -> type___GclidDateTimePair: ...
    @property
    def order_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        conversion_action: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        adjustment_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        adjustment_type: typing___Optional[
            google___ads___googleads___v2___enums___conversion_adjustment_type_pb2___ConversionAdjustmentTypeEnum.ConversionAdjustmentTypeValue
        ] = None,
        restatement_value: typing___Optional[type___RestatementValue] = None,
        gclid_date_time_pair: typing___Optional[type___GclidDateTimePair] = None,
        order_id: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "adjustment_date_time",
            b"adjustment_date_time",
            "conversion_action",
            b"conversion_action",
            "conversion_identifier",
            b"conversion_identifier",
            "gclid_date_time_pair",
            b"gclid_date_time_pair",
            "order_id",
            b"order_id",
            "restatement_value",
            b"restatement_value",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "adjustment_date_time",
            b"adjustment_date_time",
            "adjustment_type",
            b"adjustment_type",
            "conversion_action",
            b"conversion_action",
            "conversion_identifier",
            b"conversion_identifier",
            "gclid_date_time_pair",
            b"gclid_date_time_pair",
            "order_id",
            b"order_id",
            "restatement_value",
            b"restatement_value",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "conversion_identifier", b"conversion_identifier"
        ],
    ) -> typing_extensions___Literal["gclid_date_time_pair", "order_id"]: ...

type___ConversionAdjustment = ConversionAdjustment

class RestatementValue(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def adjusted_value(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def currency_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        adjusted_value: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        currency_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "adjusted_value", b"adjusted_value", "currency_code", b"currency_code"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "adjusted_value", b"adjusted_value", "currency_code", b"currency_code"
        ],
    ) -> None: ...

type___RestatementValue = RestatementValue

class GclidDateTimePair(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def gclid(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def conversion_date_time(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        gclid: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        conversion_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "conversion_date_time", b"conversion_date_time", "gclid", b"gclid"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "conversion_date_time", b"conversion_date_time", "gclid", b"gclid"
        ],
    ) -> None: ...

type___GclidDateTimePair = GclidDateTimePair

class ConversionAdjustmentResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    adjustment_type: google___ads___googleads___v2___enums___conversion_adjustment_type_pb2___ConversionAdjustmentTypeEnum.ConversionAdjustmentTypeValue = ...
    @property
    def conversion_action(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def adjustment_date_time(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def gclid_date_time_pair(self) -> type___GclidDateTimePair: ...
    @property
    def order_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        conversion_action: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        adjustment_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        adjustment_type: typing___Optional[
            google___ads___googleads___v2___enums___conversion_adjustment_type_pb2___ConversionAdjustmentTypeEnum.ConversionAdjustmentTypeValue
        ] = None,
        gclid_date_time_pair: typing___Optional[type___GclidDateTimePair] = None,
        order_id: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "adjustment_date_time",
            b"adjustment_date_time",
            "conversion_action",
            b"conversion_action",
            "conversion_identifier",
            b"conversion_identifier",
            "gclid_date_time_pair",
            b"gclid_date_time_pair",
            "order_id",
            b"order_id",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "adjustment_date_time",
            b"adjustment_date_time",
            "adjustment_type",
            b"adjustment_type",
            "conversion_action",
            b"conversion_action",
            "conversion_identifier",
            b"conversion_identifier",
            "gclid_date_time_pair",
            b"gclid_date_time_pair",
            "order_id",
            b"order_id",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "conversion_identifier", b"conversion_identifier"
        ],
    ) -> typing_extensions___Literal["gclid_date_time_pair", "order_id"]: ...

type___ConversionAdjustmentResult = ConversionAdjustmentResult
