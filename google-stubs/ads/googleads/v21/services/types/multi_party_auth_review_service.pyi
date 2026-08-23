from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v21.enums.types.multi_party_auth_review_status import (
    MultiPartyAuthReviewStatusEnum,
)

_M = TypeVar("_M")

class ResolveMultiPartyAuthReviewOperation(proto.Message):
    multi_party_auth_review: str
    new_status: MultiPartyAuthReviewStatusEnum.MultiPartyAuthReviewStatus
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        multi_party_auth_review: str = ...,
        new_status: MultiPartyAuthReviewStatusEnum.MultiPartyAuthReviewStatus = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["multi_party_auth_review", "new_status"]
    ) -> bool: ...

class ResolveMultiPartyAuthReviewRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[ResolveMultiPartyAuthReviewOperation]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[ResolveMultiPartyAuthReviewOperation] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "operations"]
    ) -> bool: ...

class ResolveMultiPartyAuthReviewResponse(proto.Message):
    result_or_error: MutableSequence[ResolveMultiPartyAuthReviewResultOrError]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result_or_error: MutableSequence[
            ResolveMultiPartyAuthReviewResultOrError
        ] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["result_or_error"]
    ) -> bool: ...

class ResolveMultiPartyAuthReviewResult(proto.Message):
    multi_party_auth_review: str
    customer_user_access_invitation: str
    customer_user_access: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        multi_party_auth_review: str = ...,
        customer_user_access_invitation: str = ...,
        customer_user_access: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "multi_party_auth_review",
            "customer_user_access_invitation",
            "customer_user_access",
        ],
    ) -> bool: ...

class ResolveMultiPartyAuthReviewResultOrError(proto.Message):
    result: ResolveMultiPartyAuthReviewResult
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: ResolveMultiPartyAuthReviewResult = ...,
        partial_failure_error: Status = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["result", "partial_failure_error"]
    ) -> bool: ...
