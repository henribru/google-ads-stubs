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


class AccountBudgetProposalStatusEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    class AccountBudgetProposalStatus(int):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        @classmethod
        def Name(cls, number: int) -> str: ...
        @classmethod
        def Value(cls, name: str) -> AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus: ...
        @classmethod
        def keys(cls) -> typing___List[str]: ...
        @classmethod
        def values(cls) -> typing___List[AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus]: ...
        @classmethod
        def items(cls) -> typing___List[typing___Tuple[str, AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus]]: ...
        UNSPECIFIED = typing___cast(AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus, 0)
        UNKNOWN = typing___cast(AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus, 1)
        PENDING = typing___cast(AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus, 2)
        APPROVED_HELD = typing___cast(AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus, 3)
        APPROVED = typing___cast(AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus, 4)
        CANCELLED = typing___cast(AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus, 5)
        REJECTED = typing___cast(AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus, 6)
    UNSPECIFIED = typing___cast(AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus, 0)
    UNKNOWN = typing___cast(AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus, 1)
    PENDING = typing___cast(AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus, 2)
    APPROVED_HELD = typing___cast(AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus, 3)
    APPROVED = typing___cast(AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus, 4)
    CANCELLED = typing___cast(AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus, 5)
    REJECTED = typing___cast(AccountBudgetProposalStatusEnum.AccountBudgetProposalStatus, 6)


    def __init__(self,
        ) -> None: ...
    @classmethod
    def FromString(cls, s: bytes) -> AccountBudgetProposalStatusEnum: ...
    def MergeFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
    def CopyFrom(self, other_msg: google___protobuf___message___Message) -> None: ...
