"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.ads.google_ads.v5.proto.resources.customer_manager_link_pb2
import google.protobuf.descriptor
import google.protobuf.field_mask_pb2
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class GetCustomerManagerLinkRequest(google.protobuf.message.Message):
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

global___GetCustomerManagerLinkRequest = GetCustomerManagerLinkRequest

class MutateCustomerManagerLinkRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    OPERATIONS_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    @property
    def operations(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___CustomerManagerLinkOperation
    ]: ...
    def __init__(
        self,
        *,
        customer_id: typing.Text = ...,
        operations: typing.Optional[
            typing.Iterable[global___CustomerManagerLinkOperation]
        ] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "customer_id", b"customer_id", "operations", b"operations"
        ],
    ) -> None: ...

global___MutateCustomerManagerLinkRequest = MutateCustomerManagerLinkRequest

class MoveManagerLinkRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    CUSTOMER_ID_FIELD_NUMBER: builtins.int
    PREVIOUS_CUSTOMER_MANAGER_LINK_FIELD_NUMBER: builtins.int
    NEW_MANAGER_FIELD_NUMBER: builtins.int
    customer_id: typing.Text = ...
    previous_customer_manager_link: typing.Text = ...
    new_manager: typing.Text = ...
    def __init__(
        self,
        *,
        customer_id: typing.Text = ...,
        previous_customer_manager_link: typing.Text = ...,
        new_manager: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "customer_id",
            b"customer_id",
            "new_manager",
            b"new_manager",
            "previous_customer_manager_link",
            b"previous_customer_manager_link",
        ],
    ) -> None: ...

global___MoveManagerLinkRequest = MoveManagerLinkRequest

class CustomerManagerLinkOperation(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    UPDATE_MASK_FIELD_NUMBER: builtins.int
    UPDATE_FIELD_NUMBER: builtins.int
    @property
    def update_mask(self) -> google.protobuf.field_mask_pb2.FieldMask: ...
    @property
    def update(
        self,
    ) -> google.ads.google_ads.v5.proto.resources.customer_manager_link_pb2.CustomerManagerLink: ...
    def __init__(
        self,
        *,
        update_mask: typing.Optional[google.protobuf.field_mask_pb2.FieldMask] = ...,
        update: typing.Optional[
            google.ads.google_ads.v5.proto.resources.customer_manager_link_pb2.CustomerManagerLink
        ] = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "operation",
            b"operation",
            "update",
            b"update",
            "update_mask",
            b"update_mask",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "operation",
            b"operation",
            "update",
            b"update",
            "update_mask",
            b"update_mask",
        ],
    ) -> None: ...
    def WhichOneof(
        self, oneof_group: typing_extensions.Literal["operation", b"operation"]
    ) -> typing_extensions.Literal["update"]: ...

global___CustomerManagerLinkOperation = CustomerManagerLinkOperation

class MutateCustomerManagerLinkResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    RESULTS_FIELD_NUMBER: builtins.int
    @property
    def results(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___MutateCustomerManagerLinkResult
    ]: ...
    def __init__(
        self,
        *,
        results: typing.Optional[
            typing.Iterable[global___MutateCustomerManagerLinkResult]
        ] = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["results", b"results"]
    ) -> None: ...

global___MutateCustomerManagerLinkResponse = MutateCustomerManagerLinkResponse

class MoveManagerLinkResponse(google.protobuf.message.Message):
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

global___MoveManagerLinkResponse = MoveManagerLinkResponse

class MutateCustomerManagerLinkResult(google.protobuf.message.Message):
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

global___MutateCustomerManagerLinkResult = MutateCustomerManagerLinkResult
