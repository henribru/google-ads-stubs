from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v16.enums.types.identity_verification_program import (
    IdentityVerificationProgramEnum,
)
from google.ads.googleads.v16.enums.types.identity_verification_program_status import (
    IdentityVerificationProgramStatusEnum,
)

_M = TypeVar("_M")

class GetIdentityVerificationRequest(proto.Message):
    customer_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id"]
    ) -> bool: ...

class GetIdentityVerificationResponse(proto.Message):
    identity_verification: MutableSequence[IdentityVerification]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        identity_verification: MutableSequence[IdentityVerification] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["identity_verification"]
    ) -> bool: ...

class IdentityVerification(proto.Message):
    verification_program: IdentityVerificationProgramEnum.IdentityVerificationProgram
    identity_verification_requirement: IdentityVerificationRequirement
    verification_progress: IdentityVerificationProgress
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        verification_program: IdentityVerificationProgramEnum.IdentityVerificationProgram = ...,
        identity_verification_requirement: IdentityVerificationRequirement = ...,
        verification_progress: IdentityVerificationProgress = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "verification_program",
            "identity_verification_requirement",
            "verification_progress",
        ],
    ) -> bool: ...

class IdentityVerificationProgress(proto.Message):
    program_status: (
        IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus
    )
    invitation_link_expiration_time: str
    action_url: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        program_status: IdentityVerificationProgramStatusEnum.IdentityVerificationProgramStatus = ...,
        invitation_link_expiration_time: str = ...,
        action_url: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal["program_status", "invitation_link_expiration_time", "action_url"],
    ) -> bool: ...

class IdentityVerificationRequirement(proto.Message):
    verification_start_deadline_time: str
    verification_completion_deadline_time: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        verification_start_deadline_time: str = ...,
        verification_completion_deadline_time: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "verification_start_deadline_time", "verification_completion_deadline_time"
        ],
    ) -> bool: ...

class StartIdentityVerificationRequest(proto.Message):
    customer_id: str
    verification_program: IdentityVerificationProgramEnum.IdentityVerificationProgram
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        verification_program: IdentityVerificationProgramEnum.IdentityVerificationProgram = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "verification_program"]
    ) -> bool: ...
