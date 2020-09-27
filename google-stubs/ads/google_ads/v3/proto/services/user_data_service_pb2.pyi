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
    Int32Value as google___protobuf___wrappers_pb2___Int32Value,
    StringValue as google___protobuf___wrappers_pb2___StringValue,
)
from typing_extensions import Literal as typing_extensions___Literal

from google.ads.google_ads.v3.proto.common.offline_user_data_pb2 import (
    CustomerMatchUserListMetadata as google___ads___googleads___v3___common___offline_user_data_pb2___CustomerMatchUserListMetadata,
    UserData as google___ads___googleads___v3___common___offline_user_data_pb2___UserData,
)

builtin___bool = bool
builtin___bytes = bytes
builtin___float = float
builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class UploadUserDataRequest(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    customer_id: typing___Text = ...
    @property
    def operations(
        self,
    ) -> google___protobuf___internal___containers___RepeatedCompositeFieldContainer[
        type___UserDataOperation
    ]: ...
    @property
    def customer_match_user_list_metadata(
        self,
    ) -> google___ads___googleads___v3___common___offline_user_data_pb2___CustomerMatchUserListMetadata: ...
    def __init__(
        self,
        *,
        customer_id: typing___Optional[typing___Text] = None,
        operations: typing___Optional[
            typing___Iterable[type___UserDataOperation]
        ] = None,
        customer_match_user_list_metadata: typing___Optional[
            google___ads___googleads___v3___common___offline_user_data_pb2___CustomerMatchUserListMetadata
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "customer_match_user_list_metadata",
            b"customer_match_user_list_metadata",
            "metadata",
            b"metadata",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "customer_id",
            b"customer_id",
            "customer_match_user_list_metadata",
            b"customer_match_user_list_metadata",
            "metadata",
            b"metadata",
            "operations",
            b"operations",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["metadata", b"metadata"]
    ) -> typing_extensions___Literal["customer_match_user_list_metadata"]: ...

type___UploadUserDataRequest = UploadUserDataRequest

class UserDataOperation(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def create(
        self,
    ) -> google___ads___googleads___v3___common___offline_user_data_pb2___UserData: ...
    def __init__(
        self,
        *,
        create: typing___Optional[
            google___ads___googleads___v3___common___offline_user_data_pb2___UserData
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "create", b"create", "operation", b"operation"
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "create", b"create", "operation", b"operation"
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions___Literal["operation", b"operation"]
    ) -> typing_extensions___Literal["create"]: ...

type___UserDataOperation = UserDataOperation

class UploadUserDataResponse(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    @property
    def upload_date_time(self) -> google___protobuf___wrappers_pb2___StringValue: ...
    @property
    def received_operations_count(
        self,
    ) -> google___protobuf___wrappers_pb2___Int32Value: ...
    def __init__(
        self,
        *,
        upload_date_time: typing___Optional[
            google___protobuf___wrappers_pb2___StringValue
        ] = None,
        received_operations_count: typing___Optional[
            google___protobuf___wrappers_pb2___Int32Value
        ] = None,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions___Literal[
            "received_operations_count",
            b"received_operations_count",
            "upload_date_time",
            b"upload_date_time",
        ],
    ) -> builtin___bool: ...
    def ClearField(
        self,
        field_name: typing_extensions___Literal[
            "received_operations_count",
            b"received_operations_count",
            "upload_date_time",
            b"upload_date_time",
        ],
    ) -> None: ...

type___UploadUserDataResponse = UploadUserDataResponse
