from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from google.protobuf.field_mask_pb2 import FieldMask
from google.rpc.status_pb2 import Status
from typing_extensions import Literal

from google.ads.googleads.v23.enums.types.response_content_type import (
    ResponseContentTypeEnum,
)
from google.ads.googleads.v23.resources.types.campaign import Campaign

_M = TypeVar("_M")

class BrandCampaignAssets(proto.Message):
    business_name_asset: str
    logo_asset: MutableSequence[str]
    landscape_logo_asset: MutableSequence[str]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        business_name_asset: str = ...,
        logo_asset: MutableSequence[str] = ...,
        landscape_logo_asset: MutableSequence[str] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["business_name_asset", "logo_asset", "landscape_logo_asset"]
    ) -> bool: ...

class CampaignOperation(proto.Message):
    update_mask: FieldMask
    create: Campaign
    update: Campaign
    remove: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        update_mask: FieldMask = ...,
        create: Campaign = ...,
        update: Campaign = ...,
        remove: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["update_mask", "create", "update", "remove"]
    ) -> bool: ...

class EnableOperation(proto.Message):
    campaign: str
    auto_populate_brand_assets: bool
    brand_assets: BrandCampaignAssets
    final_uri_domain: str
    main_color: str
    accent_color: str
    font_family: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        campaign: str = ...,
        auto_populate_brand_assets: bool = ...,
        brand_assets: BrandCampaignAssets = ...,
        final_uri_domain: str = ...,
        main_color: str = ...,
        accent_color: str = ...,
        font_family: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "campaign",
            "auto_populate_brand_assets",
            "brand_assets",
            "final_uri_domain",
            "main_color",
            "accent_color",
            "font_family",
        ],
    ) -> bool: ...

class EnablePMaxBrandGuidelinesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[EnableOperation]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[EnableOperation] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["customer_id", "operations"]
    ) -> bool: ...

class EnablePMaxBrandGuidelinesResponse(proto.Message):
    results: MutableSequence[EnablementResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        results: MutableSequence[EnablementResult] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["results"]
    ) -> bool: ...

class EnablementResult(proto.Message):
    campaign: str
    enablement_error: Status
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        campaign: str = ...,
        enablement_error: Status = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["campaign", "enablement_error"]
    ) -> bool: ...

class MutateCampaignResult(proto.Message):
    resource_name: str
    campaign: Campaign
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        resource_name: str = ...,
        campaign: Campaign = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["resource_name", "campaign"]
    ) -> bool: ...

class MutateCampaignsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence[CampaignOperation]
    partial_failure: bool
    validate_only: bool
    response_content_type: ResponseContentTypeEnum.ResponseContentType
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        customer_id: str = ...,
        operations: MutableSequence[CampaignOperation] = ...,
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

class MutateCampaignsResponse(proto.Message):
    partial_failure_error: Status
    results: MutableSequence[MutateCampaignResult]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        partial_failure_error: Status = ...,
        results: MutableSequence[MutateCampaignResult] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["partial_failure_error", "results"]
    ) -> bool: ...
