from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v25.actions.types.generate_shareable_previews import (
    GenerateShareablePreviewsOperation,
    GenerateShareablePreviewsResult,
)

_M = TypeVar("_M")

class GenerateShareablePreviewsRequest(proto.Message):
    customer_id: str
    operation: GenerateShareablePreviewsOperation
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operation: GenerateShareablePreviewsOperation = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "operation"]
    ) -> bool: ...

class GenerateShareablePreviewsResponse(proto.Message):
    result: GenerateShareablePreviewsResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: GenerateShareablePreviewsResult = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["result"]
    ) -> bool: ...
