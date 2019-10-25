# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import (
    Message as google___protobuf___message___Message,
)

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    cast as typing___cast,
)


class CustomerManagerLinkErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class CustomerManagerLinkError(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> CustomerManagerLinkErrorEnum.CustomerManagerLinkError: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[CustomerManagerLinkErrorEnum.CustomerManagerLinkError]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, CustomerManagerLinkErrorEnum.CustomerManagerLinkError]]: ...
        UNSPECIFIED = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 0)
        UNKNOWN = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 1)
        NO_PENDING_INVITE = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 2)
        SAME_CLIENT_MORE_THAN_ONCE_PER_CALL = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 3)
        MANAGER_HAS_MAX_NUMBER_OF_LINKED_ACCOUNTS = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 4)
        CANNOT_UNLINK_ACCOUNT_WITHOUT_ACTIVE_USER = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 5)
        CANNOT_REMOVE_LAST_CLIENT_ACCOUNT_OWNER = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 6)
        CANNOT_CHANGE_ROLE_BY_NON_ACCOUNT_OWNER = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 7)
        CANNOT_CHANGE_ROLE_FOR_NON_ACTIVE_LINK_ACCOUNT = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 8)
        DUPLICATE_CHILD_FOUND = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 9)
    UNSPECIFIED = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 0)
    UNKNOWN = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 1)
    NO_PENDING_INVITE = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 2)
    SAME_CLIENT_MORE_THAN_ONCE_PER_CALL = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 3)
    MANAGER_HAS_MAX_NUMBER_OF_LINKED_ACCOUNTS = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 4)
    CANNOT_UNLINK_ACCOUNT_WITHOUT_ACTIVE_USER = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 5)
    CANNOT_REMOVE_LAST_CLIENT_ACCOUNT_OWNER = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 6)
    CANNOT_CHANGE_ROLE_BY_NON_ACCOUNT_OWNER = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 7)
    CANNOT_CHANGE_ROLE_FOR_NON_ACTIVE_LINK_ACCOUNT = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 8)
    DUPLICATE_CHILD_FOUND = typing___cast(CustomerManagerLinkErrorEnum.CustomerManagerLinkError, 9)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> CustomerManagerLinkErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
