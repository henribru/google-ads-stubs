"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.enum_type_wrapper
import google.protobuf.message
import typing

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class BillingSetupStatusEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _BillingSetupStatus(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            BillingSetupStatus.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = BillingSetupStatusEnum.BillingSetupStatus.V(0)
        UNKNOWN = BillingSetupStatusEnum.BillingSetupStatus.V(1)
        PENDING = BillingSetupStatusEnum.BillingSetupStatus.V(2)
        APPROVED_HELD = BillingSetupStatusEnum.BillingSetupStatus.V(3)
        APPROVED = BillingSetupStatusEnum.BillingSetupStatus.V(4)
        CANCELLED = BillingSetupStatusEnum.BillingSetupStatus.V(5)
    class BillingSetupStatus(metaclass=_BillingSetupStatus):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = BillingSetupStatusEnum.BillingSetupStatus.V(0)
    UNKNOWN = BillingSetupStatusEnum.BillingSetupStatus.V(1)
    PENDING = BillingSetupStatusEnum.BillingSetupStatus.V(2)
    APPROVED_HELD = BillingSetupStatusEnum.BillingSetupStatus.V(3)
    APPROVED = BillingSetupStatusEnum.BillingSetupStatus.V(4)
    CANCELLED = BillingSetupStatusEnum.BillingSetupStatus.V(5)
    def __init__(
        self,
    ) -> None: ...

global___BillingSetupStatusEnum = BillingSetupStatusEnum
