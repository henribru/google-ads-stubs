from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v15.common.types.policy import PolicyViolationKey
from google.ads.googleads.v15.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v15.resources.types.asset_group_signal import AssetGroupSignal

_M = TypeVar("_M")

class AssetGroupSignalOperation(proto.Message):
    exempt_policy_violation_keys: MutableSequence[PolicyViolationKey]
    create: AssetGroupSignal
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        exempt_policy_violation_keys: MutableSequence[PolicyViolationKey] = ...,
        create: AssetGroupSignal = ...,
        remove: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["exempt_policy_violation_keys", "create", "remove"]
    ) -> bool: ...

class MutateAssetGroupSignalResult(proto.Message):
    resource_name: str
    asset_group_signal: AssetGroupSignal
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        asset_group_signal: AssetGroupSignal = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "asset_group_signal"]
    ) -> bool: ...

class MutateAssetGroupSignalsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[AssetGroupSignalOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[AssetGroupSignalOperation] = ...,
        partial_failure: bool = ...,
        validate_only: bool = ...,
        response_content_type: ResponseContentTypeEnum.ResponseContentType = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "customer_id",
            "operations",
            "partial_failure",
            "validate_only",
            "response_content_type",
        ],
    ) -> bool: ...

class MutateAssetGroupSignalsResponse(proto.Message):
    results: MutableSequence[MutateAssetGroupSignalResult]
    partial_failure_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[MutateAssetGroupSignalResult] = ...,
        partial_failure_error: Status = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["results", "partial_failure_error"]
    ) -> bool: ...
