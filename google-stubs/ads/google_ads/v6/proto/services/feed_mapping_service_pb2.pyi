"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v6.proto.enums.response_content_type_pb2
import google.ads.google_ads.v6.proto.resources.feed_mapping_pb2
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import google.rpc.status_pb2
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetFeedMappingRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["resource_name", b"resource_name"]
    ) -> None: ...

global___GetFeedMappingRequest = GetFeedMappingRequest

class MutateFeedMappingsRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATIONS_FIELD_NUMBER: builtins.int
    PARTIAL_FAILURE_FIELD_NUMBER: builtins.int
    VALIDATE_ONLY_FIELD_NUMBER: builtins.int
    RESPONSE_CONTENT_TYPE_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    partial_failure: builtins.bool = ...
    validate_only: builtins.bool = ...
    response_content_type: google.ads.google_ads.v6.proto.enums.response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType.V = (
        ...
    )
    @property
    def operations(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___FeedMappingOperation
    ]: ...
    def __init__(
        self,
        *,
        customer_id: typing.Text = ...,
        operations: typing.Optional[
            typing.Iterable[global___FeedMappingOperation]
        ] = ...,
        partial_failure: builtins.bool = ...,
        validate_only: builtins.bool = ...,
        response_content_type: google.ads.google_ads.v6.proto.enums.response_content_type_pb2.ResponseContentTypeEnum.ResponseContentType.V = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "customer_id",
            b"customer_id",
            "operations",
            b"operations",
            "partial_failure",
            b"partial_failure",
            "response_content_type",
            b"response_content_type",
            "validate_only",
            b"validate_only",
        ],
    ) -> None: ...

global___MutateFeedMappingsRequest = MutateFeedMappingsRequest

class FeedMappingOperation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CREATE_FIELD_NUMBER: builtins.int
    REMOVE_FIELD_NUMBER: builtins.int
    remove: typing.Text = ...
    @property
    def create(
        self,
    ) -> google.ads.google_ads.v6.proto.resources.feed_mapping_pb2.FeedMapping: ...
    def __init__(
        self,
        *,
        create: typing.Optional[
            google.ads.google_ads.v6.proto.resources.feed_mapping_pb2.FeedMapping
        ] = ...,
        remove: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "create", b"create", "operation", b"operation", "remove", b"remove"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "create", b"create", "operation", b"operation", "remove", b"remove"
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["operation", b"operation"]
    ) -> typing_extensions.Literal["create", "remove"]: ...

global___FeedMappingOperation = FeedMappingOperation

class MutateFeedMappingsResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    PARTIAL_FAILURE_ERROR_FIELD_NUMBER: builtins.int
    RESULTS_FIELD_NUMBER: builtins.int
    @property
    def partial_failure_error(self) -> google.rpc.status_pb2.Status: ...
    @property
    def results(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___MutateFeedMappingResult
    ]: ...
    def __init__(
        self,
        *,
        partial_failure_error: typing.Optional[google.rpc.status_pb2.Status] = ...,
        results: typing.Optional[
            typing.Iterable[global___MutateFeedMappingResult]
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "partial_failure_error", b"partial_failure_error"
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "partial_failure_error", b"partial_failure_error", "results", b"results"
        ],
    ) -> None: ...

global___MutateFeedMappingsResponse = MutateFeedMappingsResponse

class MutateFeedMappingResult(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESOURCE_NAME_FIELD_NUMBER: builtins.int
    FEED_MAPPING_FIELD_NUMBER: builtins.int
    resource_name: typing.Text = ...
    @property
    def feed_mapping(
        self,
    ) -> google.ads.google_ads.v6.proto.resources.feed_mapping_pb2.FeedMapping: ...
    def __init__(
        self,
        *,
        resource_name: typing.Text = ...,
        feed_mapping: typing.Optional[
            google.ads.google_ads.v6.proto.resources.feed_mapping_pb2.FeedMapping
        ] = ...,
    ) -> None: ...
    def HasField(
        self, field_name: typing_extensions.Literal["feed_mapping", b"feed_mapping"]
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "feed_mapping", b"feed_mapping", "resource_name", b"resource_name"
        ],
    ) -> None: ...

global___MutateFeedMappingResult = MutateFeedMappingResult
