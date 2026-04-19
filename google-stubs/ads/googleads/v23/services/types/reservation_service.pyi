from collections.abc import Mapping
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v23.actions.types.book_campaigns import (
    BookCampaignsOperation,
    BookCampaignsResult,
)
from google.ads.googleads.v23.actions.types.quote_campaigns import (
    QuoteCampaignsOperation,
    QuoteCampaignsResult,
)

_M = TypeVar("_M")

class BookCampaignsRequest(proto.Message):
    customer_id: str
    operation: BookCampaignsOperation
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operation: BookCampaignsOperation = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "operation"]
    ) -> bool: ...

class BookCampaignsResponse(proto.Message):
    result: BookCampaignsResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: BookCampaignsResult = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["result"]
    ) -> bool: ...

class QuoteCampaignsRequest(proto.Message):
    customer_id: str
    operation: QuoteCampaignsOperation
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operation: QuoteCampaignsOperation = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "operation"]
    ) -> bool: ...

class QuoteCampaignsResponse(proto.Message):
    result: QuoteCampaignsResult
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        result: QuoteCampaignsResult = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["result"]
    ) -> bool: ...
