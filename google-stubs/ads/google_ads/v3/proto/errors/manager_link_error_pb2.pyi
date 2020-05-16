# @generated by generate_proto_mypy_stubs.py.  Do not edit!
import sys
from google.protobuf.descriptor import (
    Descriptor as google___protobuf___descriptor___Descriptor,
    EnumDescriptor as google___protobuf___descriptor___EnumDescriptor,
)

from google.protobuf.message import Message as google___protobuf___message___Message

from typing import (
    List as typing___List,
    Tuple as typing___Tuple,
    Union as typing___Union,
    cast as typing___cast,
)

builtin___bytes = bytes
builtin___int = int
builtin___str = str
if sys.version_info < (3,):
    builtin___buffer = buffer
    builtin___unicode = unicode

class ManagerLinkErrorEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class ManagerLinkError(builtin___int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: builtin___int) -> builtin___str: ...
        @classmethod
        def Value(
            cls, name: builtin___str
        ) -> "ManagerLinkErrorEnum.ManagerLinkError": ...
        @classmethod
        def keys(cls) -> typing___List[builtin___str]: ...
        @classmethod
        def values(cls) -> typing___List["ManagerLinkErrorEnum.ManagerLinkError"]: ...
        @classmethod
        def items(
            cls,
        ) -> typing___List[
            typing___Tuple[builtin___str, "ManagerLinkErrorEnum.ManagerLinkError"]
        ]: ...
        UNSPECIFIED = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 0)
        UNKNOWN = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 1)
        ACCOUNTS_NOT_COMPATIBLE_FOR_LINKING = typing___cast(
            "ManagerLinkErrorEnum.ManagerLinkError", 2
        )
        TOO_MANY_MANAGERS = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 3)
        TOO_MANY_INVITES = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 4)
        ALREADY_INVITED_BY_THIS_MANAGER = typing___cast(
            "ManagerLinkErrorEnum.ManagerLinkError", 5
        )
        ALREADY_MANAGED_BY_THIS_MANAGER = typing___cast(
            "ManagerLinkErrorEnum.ManagerLinkError", 6
        )
        ALREADY_MANAGED_IN_HIERARCHY = typing___cast(
            "ManagerLinkErrorEnum.ManagerLinkError", 7
        )
        DUPLICATE_CHILD_FOUND = typing___cast(
            "ManagerLinkErrorEnum.ManagerLinkError", 8
        )
        CLIENT_HAS_NO_ADMIN_USER = typing___cast(
            "ManagerLinkErrorEnum.ManagerLinkError", 9
        )
        MAX_DEPTH_EXCEEDED = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 10)
        CYCLE_NOT_ALLOWED = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 11)
        TOO_MANY_ACCOUNTS = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 12)
        TOO_MANY_ACCOUNTS_AT_MANAGER = typing___cast(
            "ManagerLinkErrorEnum.ManagerLinkError", 13
        )
        NON_OWNER_USER_CANNOT_MODIFY_LINK = typing___cast(
            "ManagerLinkErrorEnum.ManagerLinkError", 14
        )
        SUSPENDED_ACCOUNT_CANNOT_ADD_CLIENTS = typing___cast(
            "ManagerLinkErrorEnum.ManagerLinkError", 15
        )
        CLIENT_OUTSIDE_TREE = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 16)
        INVALID_STATUS_CHANGE = typing___cast(
            "ManagerLinkErrorEnum.ManagerLinkError", 17
        )
        INVALID_CHANGE = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 18)
    UNSPECIFIED = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 0)
    UNKNOWN = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 1)
    ACCOUNTS_NOT_COMPATIBLE_FOR_LINKING = typing___cast(
        "ManagerLinkErrorEnum.ManagerLinkError", 2
    )
    TOO_MANY_MANAGERS = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 3)
    TOO_MANY_INVITES = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 4)
    ALREADY_INVITED_BY_THIS_MANAGER = typing___cast(
        "ManagerLinkErrorEnum.ManagerLinkError", 5
    )
    ALREADY_MANAGED_BY_THIS_MANAGER = typing___cast(
        "ManagerLinkErrorEnum.ManagerLinkError", 6
    )
    ALREADY_MANAGED_IN_HIERARCHY = typing___cast(
        "ManagerLinkErrorEnum.ManagerLinkError", 7
    )
    DUPLICATE_CHILD_FOUND = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 8)
    CLIENT_HAS_NO_ADMIN_USER = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 9)
    MAX_DEPTH_EXCEEDED = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 10)
    CYCLE_NOT_ALLOWED = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 11)
    TOO_MANY_ACCOUNTS = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 12)
    TOO_MANY_ACCOUNTS_AT_MANAGER = typing___cast(
        "ManagerLinkErrorEnum.ManagerLinkError", 13
    )
    NON_OWNER_USER_CANNOT_MODIFY_LINK = typing___cast(
        "ManagerLinkErrorEnum.ManagerLinkError", 14
    )
    SUSPENDED_ACCOUNT_CANNOT_ADD_CLIENTS = typing___cast(
        "ManagerLinkErrorEnum.ManagerLinkError", 15
    )
    CLIENT_OUTSIDE_TREE = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 16)
    INVALID_STATUS_CHANGE = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 17)
    INVALID_CHANGE = typing___cast("ManagerLinkErrorEnum.ManagerLinkError", 18)
    global___ManagerLinkError = ManagerLinkError
    def __init__(self,) -> None: ...
    if sys.version_info >= (3,):
        @classmethod
        def FromString(cls, s: builtin___bytes) -> ManagerLinkErrorEnum: ...
    else:
        @classmethod
        def FromString(
            cls, s: typing___Union[builtin___bytes, builtin___buffer, builtin___unicode]
        ) -> ManagerLinkErrorEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...

global___ManagerLinkErrorEnum = ManagerLinkErrorEnum
