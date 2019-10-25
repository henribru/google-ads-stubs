# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.ads.google_ads.v2.proto.enums.conversion_adjustment_type_pb2 import (
    ConversionAdjustmentTypeEnum as google___ads___googleads___v2___enums___conversion_adjustment_type_pb2___ConversionAdjustmentTypeEnum,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
)

from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from google.protobuf.wrappers_pb2 import (
    DoubleValue as google___protobuf___wrappers_pb2___DoubleValue,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)

from google.rpc.status_pb2 import (
    Status as google___rpc___status_pb2___Status,
)

from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
)

from typing_extensions import (
    Literal as typing_extensions___Literal,
)


class UploadConversionAdjustmentsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id = ... # type: typing___Text
    partial_failure = ... # type: bool
    validate_only = ... # type: bool

    @property
    def conversion_adjustments(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ConversionAdjustment]: ...

    def __init__(self,
        *,
        customer_id : typing___Optional[typing___Text] = None,
        conversion_adjustments : typing___Optional[typing___Iterable[ConversionAdjustment]] = None,
        partial_failure : typing___Optional[bool] = None,
        validate_only : typing___Optional[bool] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UploadConversionAdjustmentsRequest: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def ClearField(self, field_name: typing_extensions___Literal[u"conversion_adjustments",u"customer_id",u"partial_failure",u"validate_only"]) -> None: ...
    else:
        def ClearField(self, field_name: typing_extensions___Literal[u"conversion_adjustments",b"conversion_adjustments",u"customer_id",b"customer_id",u"partial_failure",b"partial_failure",u"validate_only",b"validate_only"]) -> None: ...

class UploadConversionAdjustmentsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def partial_failure_error(self) -> google___rpc___status_pb2___Status: ...

    @property
    def results(self) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[ConversionAdjustmentResult]: ...

    def __init__(self,
        *,
        partial_failure_error : typing___Optional[google___rpc___status_pb2___Status] = None,
        results : typing___Optional[typing___Iterable[ConversionAdjustmentResult]] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> UploadConversionAdjustmentsResponse: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"partial_failure_error"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"partial_failure_error",u"results"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"partial_failure_error",b"partial_failure_error"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"partial_failure_error",b"partial_failure_error",u"results",b"results"]) -> None: ...

class ConversionAdjustment(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    adjustment_type = ... # type: google___ads___googleads___v2___enums___conversion_adjustment_type_pb2___ConversionAdjustmentTypeEnum.ConversionAdjustmentType

    @property
    def conversion_action(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def adjustment_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def restatement_value(self) -> RestatementValue: ...

    @property
    def gclid_date_time_pair(self) -> GclidDateTimePair: ...

    @property
    def order_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        conversion_action : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        adjustment_date_time : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        adjustment_type : typing___Optional[google___ads___googleads___v2___enums___conversion_adjustment_type_pb2___ConversionAdjustmentTypeEnum.ConversionAdjustmentType] = None,
        restatement_value : typing___Optional[RestatementValue] = None,
        gclid_date_time_pair : typing___Optional[GclidDateTimePair] = None,
        order_id : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ConversionAdjustment: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"adjustment_date_time",u"conversion_action",u"conversion_identifier",u"gclid_date_time_pair",u"order_id",u"restatement_value"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"adjustment_date_time",u"adjustment_type",u"conversion_action",u"conversion_identifier",u"gclid_date_time_pair",u"order_id",u"restatement_value"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"adjustment_date_time",b"adjustment_date_time",u"conversion_action",b"conversion_action",u"conversion_identifier",b"conversion_identifier",u"gclid_date_time_pair",b"gclid_date_time_pair",u"order_id",b"order_id",u"restatement_value",b"restatement_value"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"adjustment_date_time",b"adjustment_date_time",u"adjustment_type",b"adjustment_type",u"conversion_action",b"conversion_action",u"conversion_identifier",b"conversion_identifier",u"gclid_date_time_pair",b"gclid_date_time_pair",u"order_id",b"order_id",u"restatement_value",b"restatement_value"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"conversion_identifier",b"conversion_identifier"]) -> typing_extensions___Literal["gclid_date_time_pair","order_id"]: ...

class RestatementValue(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def adjusted_value(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...

    @property
    def currency_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        adjusted_value : typing___Optional[google___protobuf___wrappers_pb2___DoubleValue] = None,
        currency_code : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> RestatementValue: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"adjusted_value",u"currency_code"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"adjusted_value",u"currency_code"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"adjusted_value",b"adjusted_value",u"currency_code",b"currency_code"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"adjusted_value",b"adjusted_value",u"currency_code",b"currency_code"]) -> None: ...

class GclidDateTimePair(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...

    @property
    def gclid(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def conversion_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        gclid : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        conversion_date_time : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> GclidDateTimePair: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"conversion_date_time",u"gclid"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"conversion_date_time",u"gclid"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"conversion_date_time",b"conversion_date_time",u"gclid",b"gclid"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"conversion_date_time",b"conversion_date_time",u"gclid",b"gclid"]) -> None: ...

class ConversionAdjustmentResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    adjustment_type = ... # type: google___ads___googleads___v2___enums___conversion_adjustment_type_pb2___ConversionAdjustmentTypeEnum.ConversionAdjustmentType

    @property
    def conversion_action(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def adjustment_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    @property
    def gclid_date_time_pair(self) -> GclidDateTimePair: ...

    @property
    def order_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...

    def __init__(self,
        *,
        conversion_action : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        adjustment_date_time : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        adjustment_type : typing___Optional[google___ads___googleads___v2___enums___conversion_adjustment_type_pb2___ConversionAdjustmentTypeEnum.ConversionAdjustmentType] = None,
        gclid_date_time_pair : typing___Optional[GclidDateTimePair] = None,
        order_id : typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> ConversionAdjustmentResult: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    if sys.version_info >= (3,):
        def HasField(self, field_name: typing_extensions___Literal[u"adjustment_date_time",u"conversion_action",u"conversion_identifier",u"gclid_date_time_pair",u"order_id"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"adjustment_date_time",u"adjustment_type",u"conversion_action",u"conversion_identifier",u"gclid_date_time_pair",u"order_id"]) -> None: ...
    else:
        def HasField(self, field_name: typing_extensions___Literal[u"adjustment_date_time",b"adjustment_date_time",u"conversion_action",b"conversion_action",u"conversion_identifier",b"conversion_identifier",u"gclid_date_time_pair",b"gclid_date_time_pair",u"order_id",b"order_id"]) -> bool: ...
        def ClearField(self, field_name: typing_extensions___Literal[u"adjustment_date_time",b"adjustment_date_time",u"adjustment_type",b"adjustment_type",u"conversion_action",b"conversion_action",u"conversion_identifier",b"conversion_identifier",u"gclid_date_time_pair",b"gclid_date_time_pair",u"order_id",b"order_id"]) -> None: ...
    def WhichOneof(self, oneof_group: typing_extensions___Literal[u"conversion_identifier",b"conversion_identifier"]) -> typing_extensions___Literal["gclid_date_time_pair","order_id"]: ...
