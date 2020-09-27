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

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class UploadClickConversionsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    partial_failure: builtin___bool = ...
    validate_only: builtin___bool = ...
    @property
    def conversions(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___ClickConversion
    ]: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        conversions: typing___Optional[
            typing___Iterable[type___ClickConversion]
        ] = None,
        partial_failure: typing___Optional[builtin___bool] = None,
        validate_only: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "conversions",
            b"conversions",
            "customer_id",
            b"customer_id",
            "partial_failure",
            b"partial_failure",
            "validate_only",
            b"validate_only",
        ],
    ) -> None: ...

type___UploadClickConversionsRequest = UploadClickConversionsRequest

class UploadClickConversionsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def partial_failure_error(self) -> google___rpc___status_pb2___Status: ...
    @property
    def results(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___ClickConversionResult
    ]: ...
    def __init__(
        self,
        *,
        partial_failure_error: typing___Optional[
            google___rpc___status_pb2___Status
        ] = None,
        results: typing___Optional[
            typing___Iterable[type___ClickConversionResult]
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

type___UploadClickConversionsResponse = UploadClickConversionsResponse

class UploadCallConversionsRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    partial_failure: builtin___bool = ...
    validate_only: builtin___bool = ...
    @property
    def conversions(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___CallConversion
    ]: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        conversions: typing___Optional[typing___Iterable[type___CallConversion]] = None,
        partial_failure: typing___Optional[builtin___bool] = None,
        validate_only: typing___Optional[builtin___bool] = None,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "conversions",
            b"conversions",
            "customer_id",
            b"customer_id",
            "partial_failure",
            b"partial_failure",
            "validate_only",
            b"validate_only",
        ],
    ) -> None: ...

type___UploadCallConversionsRequest = UploadCallConversionsRequest

class UploadCallConversionsResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def partial_failure_error(self) -> google___rpc___status_pb2___Status: ...
    @property
    def results(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___CallConversionResult
    ]: ...
    def __init__(
        self,
        *,
        partial_failure_error: typing___Optional[
            google___rpc___status_pb2___Status
        ] = None,
        results: typing___Optional[
            typing___Iterable[type___CallConversionResult]
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

type___UploadCallConversionsResponse = UploadCallConversionsResponse

class ClickConversion(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def gclid(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def conversion_action(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def conversion_date_time(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def conversion_value(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def currency_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def order_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def external_attribution_data(self) -> type___ExternalAttributionData: ...
    def __init__(
        self,
        *,
        gclid: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        conversion_action: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        conversion_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        conversion_value: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        currency_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        order_id: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        external_attribution_data: typing___Optional[
            type___ExternalAttributionData
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "conversion_action",
            b"conversion_action",
            "conversion_date_time",
            b"conversion_date_time",
            "conversion_value",
            b"conversion_value",
            "currency_code",
            b"currency_code",
            "external_attribution_data",
            b"external_attribution_data",
            "gclid",
            b"gclid",
            "order_id",
            b"order_id",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "conversion_action",
            b"conversion_action",
            "conversion_date_time",
            b"conversion_date_time",
            "conversion_value",
            b"conversion_value",
            "currency_code",
            b"currency_code",
            "external_attribution_data",
            b"external_attribution_data",
            "gclid",
            b"gclid",
            "order_id",
            b"order_id",
        ],
    ) -> None: ...

type___ClickConversion = ClickConversion

class CallConversion(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def caller_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def call_start_date_time(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def conversion_action(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def conversion_date_time(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def conversion_value(self) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def currency_code(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        caller_id: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        call_start_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        conversion_action: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        conversion_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        conversion_value: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        currency_code: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "call_start_date_time",
            b"call_start_date_time",
            "caller_id",
            b"caller_id",
            "conversion_action",
            b"conversion_action",
            "conversion_date_time",
            b"conversion_date_time",
            "conversion_value",
            b"conversion_value",
            "currency_code",
            b"currency_code",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "call_start_date_time",
            b"call_start_date_time",
            "caller_id",
            b"caller_id",
            "conversion_action",
            b"conversion_action",
            "conversion_date_time",
            b"conversion_date_time",
            "conversion_value",
            b"conversion_value",
            "currency_code",
            b"currency_code",
        ],
    ) -> None: ...

type___CallConversion = CallConversion

class ExternalAttributionData(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def external_attribution_credit(
        self,
    ) -> google___protobuf___wrappers_pb2___DoubleValue: ...
    @property
    def external_attribution_model(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        external_attribution_credit: typing___Optional[
            google___protobuf___wrappers_pb2___DoubleValue
        ] = None,
        external_attribution_model: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "external_attribution_credit",
            b"external_attribution_credit",
            "external_attribution_model",
            b"external_attribution_model",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "external_attribution_credit",
            b"external_attribution_credit",
            "external_attribution_model",
            b"external_attribution_model",
        ],
    ) -> None: ...

type___ExternalAttributionData = ExternalAttributionData

class ClickConversionResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def gclid(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def conversion_action(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def conversion_date_time(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        gclid: typing___Optional[google___protobuf___wrappers_pb2___StringValue] = None,
        conversion_action: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        conversion_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "conversion_action",
            b"conversion_action",
            "conversion_date_time",
            b"conversion_date_time",
            "gclid",
            b"gclid",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "conversion_action",
            b"conversion_action",
            "conversion_date_time",
            b"conversion_date_time",
            "gclid",
            b"gclid",
        ],
    ) -> None: ...

type___ClickConversionResult = ClickConversionResult

class CallConversionResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def caller_id(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def call_start_date_time(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def conversion_action(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def conversion_date_time(
        self,
    ) -> google___protobuf___wrappers_pb2___StringValue: ...
    def __init__(
        self,
        *,
        caller_id: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        call_start_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        conversion_action: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        conversion_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "call_start_date_time",
            b"call_start_date_time",
            "caller_id",
            b"caller_id",
            "conversion_action",
            b"conversion_action",
            "conversion_date_time",
            b"conversion_date_time",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "call_start_date_time",
            b"call_start_date_time",
            "caller_id",
            b"caller_id",
            "conversion_action",
            b"conversion_action",
            "conversion_date_time",
            b"conversion_date_time",
        ],
    ) -> None: ...

type___CallConversionResult = CallConversionResult