# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import (
    Iterable as typing___Iterable,
    Optional as typing___Optional,
    Text as typing___Text,
    overload as typing___overload,
)

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.containers import (
    RepeatedCompositeFieldContainer as google___protobuf___internal___containers___RepeatedCompositeFieldContainer,
)
from google.protobuf.message import Message as google___protobuf___message___Message
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
    gclid: typing___Text = ...
    conversion_action: typing___Text = ...
    conversion_date_time: typing___Text = ...
    conversion_value: builtin___float = ...
    currency_code: typing___Text = ...
    order_id: typing___Text = ...
    @property
    def external_attribution_data(self) -> type___ExternalAttributionData: ...
    def __init__(
        self,
        *,
        gclid: typing___Optional[typing___Text] = None,
        conversion_action: typing___Optional[typing___Text] = None,
        conversion_date_time: typing___Optional[typing___Text] = None,
        conversion_value: typing___Optional[builtin___float] = None,
        currency_code: typing___Optional[typing___Text] = None,
        order_id: typing___Optional[typing___Text] = None,
        external_attribution_data: typing___Optional[
            type___ExternalAttributionData
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_conversion_action",
            b"_conversion_action",
            "_conversion_date_time",
            b"_conversion_date_time",
            "_conversion_value",
            b"_conversion_value",
            "_currency_code",
            b"_currency_code",
            "_gclid",
            b"_gclid",
            "_order_id",
            b"_order_id",
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
            "_conversion_action",
            b"_conversion_action",
            "_conversion_date_time",
            b"_conversion_date_time",
            "_conversion_value",
            b"_conversion_value",
            "_currency_code",
            b"_currency_code",
            "_gclid",
            b"_gclid",
            "_order_id",
            b"_order_id",
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
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_conversion_action", b"_conversion_action"
        ],
    ) -> typing_extensions___Literal["conversion_action"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_conversion_date_time", b"_conversion_date_time"
        ],
    ) -> typing_extensions___Literal["conversion_date_time"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_conversion_value", b"_conversion_value"
        ],
    ) -> typing_extensions___Literal["conversion_value"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_currency_code", b"_currency_code"],
    ) -> typing_extensions___Literal["currency_code"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_gclid", b"_gclid"]
    ) -> typing_extensions___Literal["gclid"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_order_id", b"_order_id"]
    ) -> typing_extensions___Literal["order_id"]: ...

type___ClickConversion = ClickConversion

class CallConversion(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    caller_id: typing___Text = ...
    call_start_date_time: typing___Text = ...
    conversion_action: typing___Text = ...
    conversion_date_time: typing___Text = ...
    conversion_value: builtin___float = ...
    currency_code: typing___Text = ...
    def __init__(
        self,
        *,
        caller_id: typing___Optional[typing___Text] = None,
        call_start_date_time: typing___Optional[typing___Text] = None,
        conversion_action: typing___Optional[typing___Text] = None,
        conversion_date_time: typing___Optional[typing___Text] = None,
        conversion_value: typing___Optional[builtin___float] = None,
        currency_code: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_call_start_date_time",
            b"_call_start_date_time",
            "_caller_id",
            b"_caller_id",
            "_conversion_action",
            b"_conversion_action",
            "_conversion_date_time",
            b"_conversion_date_time",
            "_conversion_value",
            b"_conversion_value",
            "_currency_code",
            b"_currency_code",
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
            "_call_start_date_time",
            b"_call_start_date_time",
            "_caller_id",
            b"_caller_id",
            "_conversion_action",
            b"_conversion_action",
            "_conversion_date_time",
            b"_conversion_date_time",
            "_conversion_value",
            b"_conversion_value",
            "_currency_code",
            b"_currency_code",
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
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_call_start_date_time", b"_call_start_date_time"
        ],
    ) -> typing_extensions___Literal["call_start_date_time"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_caller_id", b"_caller_id"]
    ) -> typing_extensions___Literal["caller_id"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_conversion_action", b"_conversion_action"
        ],
    ) -> typing_extensions___Literal["conversion_action"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_conversion_date_time", b"_conversion_date_time"
        ],
    ) -> typing_extensions___Literal["conversion_date_time"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_conversion_value", b"_conversion_value"
        ],
    ) -> typing_extensions___Literal["conversion_value"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal["_currency_code", b"_currency_code"],
    ) -> typing_extensions___Literal["currency_code"]: ...

type___CallConversion = CallConversion

class ExternalAttributionData(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    external_attribution_credit: builtin___float = ...
    external_attribution_model: typing___Text = ...
    def __init__(
        self,
        *,
        external_attribution_credit: typing___Optional[builtin___float] = None,
        external_attribution_model: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_external_attribution_credit",
            b"_external_attribution_credit",
            "_external_attribution_model",
            b"_external_attribution_model",
            "external_attribution_credit",
            b"external_attribution_credit",
            "external_attribution_model",
            b"external_attribution_model",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "_external_attribution_credit",
            b"_external_attribution_credit",
            "_external_attribution_model",
            b"_external_attribution_model",
            "external_attribution_credit",
            b"external_attribution_credit",
            "external_attribution_model",
            b"external_attribution_model",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_external_attribution_credit", b"_external_attribution_credit"
        ],
    ) -> typing_extensions___Literal["external_attribution_credit"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_external_attribution_model", b"_external_attribution_model"
        ],
    ) -> typing_extensions___Literal["external_attribution_model"]: ...

type___ExternalAttributionData = ExternalAttributionData

class ClickConversionResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    gclid: typing___Text = ...
    conversion_action: typing___Text = ...
    conversion_date_time: typing___Text = ...
    def __init__(
        self,
        *,
        gclid: typing___Optional[typing___Text] = None,
        conversion_action: typing___Optional[typing___Text] = None,
        conversion_date_time: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_conversion_action",
            b"_conversion_action",
            "_conversion_date_time",
            b"_conversion_date_time",
            "_gclid",
            b"_gclid",
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
            "_conversion_action",
            b"_conversion_action",
            "_conversion_date_time",
            b"_conversion_date_time",
            "_gclid",
            b"_gclid",
            "conversion_action",
            b"conversion_action",
            "conversion_date_time",
            b"conversion_date_time",
            "gclid",
            b"gclid",
        ],
    ) -> None: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_conversion_action", b"_conversion_action"
        ],
    ) -> typing_extensions___Literal["conversion_action"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_conversion_date_time", b"_conversion_date_time"
        ],
    ) -> typing_extensions___Literal["conversion_date_time"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_gclid", b"_gclid"]
    ) -> typing_extensions___Literal["gclid"]: ...

type___ClickConversionResult = ClickConversionResult

class CallConversionResult(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    caller_id: typing___Text = ...
    call_start_date_time: typing___Text = ...
    conversion_action: typing___Text = ...
    conversion_date_time: typing___Text = ...
    def __init__(
        self,
        *,
        caller_id: typing___Optional[typing___Text] = None,
        call_start_date_time: typing___Optional[typing___Text] = None,
        conversion_action: typing___Optional[typing___Text] = None,
        conversion_date_time: typing___Optional[typing___Text] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "_call_start_date_time",
            b"_call_start_date_time",
            "_caller_id",
            b"_caller_id",
            "_conversion_action",
            b"_conversion_action",
            "_conversion_date_time",
            b"_conversion_date_time",
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
            "_call_start_date_time",
            b"_call_start_date_time",
            "_caller_id",
            b"_caller_id",
            "_conversion_action",
            b"_conversion_action",
            "_conversion_date_time",
            b"_conversion_date_time",
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
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_call_start_date_time", b"_call_start_date_time"
        ],
    ) -> typing_extensions___Literal["call_start_date_time"]: ...
    @typing___overload
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["_caller_id", b"_caller_id"]
    ) -> typing_extensions___Literal["caller_id"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_conversion_action", b"_conversion_action"
        ],
    ) -> typing_extensions___Literal["conversion_action"]: ...
    @typing___overload
    def WhichOneof(
        self,
        oneof_group: typing_extensions___Literal[
            "_conversion_date_time", b"_conversion_date_time"
        ],
    ) -> typing_extensions___Literal["conversion_date_time"]: ...

type___CallConversionResult = CallConversionResult
