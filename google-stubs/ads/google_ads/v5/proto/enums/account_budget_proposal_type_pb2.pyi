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

class AccountBudgetProposalTypeEnum(google___protobuf___message___Message):
    DESCRIPTOR: google___protobuf___descriptor___Descriptor = ...
    AccountBudgetProposalTypeValue = typing___NewType(
        "AccountBudgetProposalTypeValue", builtin___int
    )
    type___AccountBudgetProposalTypeValue = AccountBudgetProposalTypeValue
    AccountBudgetProposalType: _AccountBudgetProposalType
    class _AccountBudgetProposalType(
        google___protobuf___internal___enum_type_wrapper____EnumTypeWrapper[
            AccountBudgetProposalTypeEnum.AccountBudgetProposalTypeValue
        ]
    ):
        DESCRIPTOR: google___protobuf___descriptor___EnumDescriptor = ...
        UNSPECIFIED = typing___cast(
            AccountBudgetProposalTypeEnum.AccountBudgetProposalTypeValue, 0
        )
        UNKNOWN = typing___cast(
            AccountBudgetProposalTypeEnum.AccountBudgetProposalTypeValue, 1
        )
        CREATE = typing___cast(
            AccountBudgetProposalTypeEnum.AccountBudgetProposalTypeValue, 2
        )
        UPDATE = typing___cast(
            AccountBudgetProposalTypeEnum.AccountBudgetProposalTypeValue, 3
        )
        END = typing___cast(
            AccountBudgetProposalTypeEnum.AccountBudgetProposalTypeValue, 4
        )
        REMOVE = typing___cast(
            AccountBudgetProposalTypeEnum.AccountBudgetProposalTypeValue, 5
        )
    UNSPECIFIED = typing___cast(
        AccountBudgetProposalTypeEnum.AccountBudgetProposalTypeValue, 0
    )
    UNKNOWN = typing___cast(
        AccountBudgetProposalTypeEnum.AccountBudgetProposalTypeValue, 1
    )
    CREATE = typing___cast(
        AccountBudgetProposalTypeEnum.AccountBudgetProposalTypeValue, 2
    )
    UPDATE = typing___cast(
        AccountBudgetProposalTypeEnum.AccountBudgetProposalTypeValue, 3
    )
    END = typing___cast(AccountBudgetProposalTypeEnum.AccountBudgetProposalTypeValue, 4)
    REMOVE = typing___cast(
        AccountBudgetProposalTypeEnum.AccountBudgetProposalTypeValue, 5
    )
    type___AccountBudgetProposalType = AccountBudgetProposalType
    def __init__(self,) -> None: ...

type___AccountBudgetProposalTypeEnum = AccountBudgetProposalTypeEnum
