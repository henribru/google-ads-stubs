# @generated by mypy-protobuf.  Do not edit manually!
import sys
from typing import NewType as typing___NewType, cast as typing___cast

from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
    FileDescriptor as google___protobuf___descriptor___FileDescriptor,
)
from google.protobuf.internal.enum_type_wrapper import (
    _EnumTypeWrapper as google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper,
)
from google.protobuf.message import Message as google___protobuf___message___Message

builtin___int = int

DESCRIPTOR: google___protobuf___descriptor___FileDescriptor = ...

class CustomerManagerLinkErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    CustomerManagerLinkErrorValue = typing___NewType(
        "CustomerManagerLinkErrorValue", builtin___int
    )
    type___CustomerManagerLinkErrorValue = CustomerManagerLinkErrorValue
    CustomerManagerLinkError: _CustomerManagerLinkError
    class _CustomerManagerLinkError(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 0
        )
        UNKNOWN = typing___cast(
            CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 1
        )
        NO_PENDING_INVITE = typing___cast(
            CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 2
        )
        SAME_CLIENT_MORE_THAN_ONCE_PER_CALL = typing___cast(
            CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 3
        )
        MANAGER_HAS_MAX_NUMBER_OF_LINKED_ACCOUNTS = typing___cast(
            CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 4
        )
        CANNOT_UNLINK_ACCOUNT_WITHOUT_ACTIVE_USER = typing___cast(
            CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 5
        )
        CANNOT_REMOVE_LAST_CLIENT_ACCOUNT_OWNER = typing___cast(
            CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 6
        )
        CANNOT_CHANGE_ROLE_BY_NON_ACCOUNT_OWNER = typing___cast(
            CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 7
        )
        CANNOT_CHANGE_ROLE_FOR_NON_ACTIVE_LINK_ACCOUNT = typing___cast(
            CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 8
        )
        DUPLICATE_CHILD_FOUND = typing___cast(
            CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 9
        )
        TEST_ACCOUNT_LINKS_TOO_MANY_CHILD_ACCOUNTS = typing___cast(
            CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 10
        )
    UNSPECIFIED = typing___cast(
        CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 0
    )
    UNKNOWN = typing___cast(
        CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 1
    )
    NO_PENDING_INVITE = typing___cast(
        CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 2
    )
    SAME_CLIENT_MORE_THAN_ONCE_PER_CALL = typing___cast(
        CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 3
    )
    MANAGER_HAS_MAX_NUMBER_OF_LINKED_ACCOUNTS = typing___cast(
        CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 4
    )
    CANNOT_UNLINK_ACCOUNT_WITHOUT_ACTIVE_USER = typing___cast(
        CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 5
    )
    CANNOT_REMOVE_LAST_CLIENT_ACCOUNT_OWNER = typing___cast(
        CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 6
    )
    CANNOT_CHANGE_ROLE_BY_NON_ACCOUNT_OWNER = typing___cast(
        CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 7
    )
    CANNOT_CHANGE_ROLE_FOR_NON_ACTIVE_LINK_ACCOUNT = typing___cast(
        CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 8
    )
    DUPLICATE_CHILD_FOUND = typing___cast(
        CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 9
    )
    TEST_ACCOUNT_LINKS_TOO_MANY_CHILD_ACCOUNTS = typing___cast(
        CustomerManagerLinkErrorEnum.CustomerManagerLinkErrorValue, 10
    )
    type___CustomerManagerLinkError = CustomerManagerLinkError
    def __init__(self,) -> None: ...

type___CustomerManagerLinkErrorEnum = CustomerManagerLinkErrorEnum
