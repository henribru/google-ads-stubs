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

class AccessInvitationErrorEnum(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class _AccessInvitationError(
        google.protobuf.internal.enum_type_wrapper._EnumTypeWrapper[
            AccessInvitationError.V
        ],
        builtins.type,
    ):
        DESCRIPTOR: google.protobuf.descriptor.EnumDescriptor = ...
        UNSPECIFIED = AccessInvitationErrorEnum.AccessInvitationError.V(0)
        UNKNOWN = AccessInvitationErrorEnum.AccessInvitationError.V(1)
        INVALID_EMAIL_ADDRESS = AccessInvitationErrorEnum.AccessInvitationError.V(2)
        EMAIL_ADDRESS_ALREADY_HAS_ACCESS = (
            AccessInvitationErrorEnum.AccessInvitationError.V(3)
        )
    class AccessInvitationError(metaclass=_AccessInvitationError):
        V = typing.NewType("V", builtins.int)
    UNSPECIFIED = AccessInvitationErrorEnum.AccessInvitationError.V(0)
    UNKNOWN = AccessInvitationErrorEnum.AccessInvitationError.V(1)
    INVALID_EMAIL_ADDRESS = AccessInvitationErrorEnum.AccessInvitationError.V(2)
    EMAIL_ADDRESS_ALREADY_HAS_ACCESS = (
        AccessInvitationErrorEnum.AccessInvitationError.V(3)
    )
    def __init__(
        self,
    ) -> None: ...

global___AccessInvitationErrorEnum = AccessInvitationErrorEnum
