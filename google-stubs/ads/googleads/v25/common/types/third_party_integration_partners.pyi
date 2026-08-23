from collections.abc import Mapping, MutableSequence
from typing import Any, NoReturn, TypeVar

import google.protobuf.message
import proto
from typing_extensions import Literal

from google.ads.googleads.v25.enums.types.third_party_brand_lift_integration_partner import (
    ThirdPartyBrandLiftIntegrationPartnerEnum,
)
from google.ads.googleads.v25.enums.types.third_party_brand_safety_integration_partner import (
    ThirdPartyBrandSafetyIntegrationPartnerEnum,
)
from google.ads.googleads.v25.enums.types.third_party_conversion_attribution_integration_partner import (
    ThirdPartyConversionAttributionIntegrationPartnerEnum,
)
from google.ads.googleads.v25.enums.types.third_party_reach_integration_partner import (
    ThirdPartyReachIntegrationPartnerEnum,
)
from google.ads.googleads.v25.enums.types.third_party_viewability_integration_partner import (
    ThirdPartyViewabilityIntegrationPartnerEnum,
)

_M = TypeVar("_M")

class CampaignThirdPartyBrandLiftIntegrationPartner(proto.Message):
    brand_lift_integration_partner: (
        ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner
    )
    brand_lift_integration_partner_data: ThirdPartyIntegrationPartnerData
    share_cost: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        brand_lift_integration_partner: ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner = ...,
        brand_lift_integration_partner_data: ThirdPartyIntegrationPartnerData = ...,
        share_cost: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "brand_lift_integration_partner",
            "brand_lift_integration_partner_data",
            "share_cost",
        ],
    ) -> bool: ...

class CampaignThirdPartyBrandSafetyIntegrationPartner(proto.Message):
    brand_safety_integration_partner: ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner
    brand_safety_integration_partner_data: ThirdPartyIntegrationPartnerData
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        brand_safety_integration_partner: ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner = ...,
        brand_safety_integration_partner_data: ThirdPartyIntegrationPartnerData = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "brand_safety_integration_partner", "brand_safety_integration_partner_data"
        ],
    ) -> bool: ...

class CampaignThirdPartyConversionAttributionIntegrationPartner(proto.Message):
    conversion_attribution_integration_partner: ThirdPartyConversionAttributionIntegrationPartnerEnum.ThirdPartyConversionAttributionIntegrationPartner
    conversion_attribution_integration_partner_data: ThirdPartyIntegrationPartnerData
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        conversion_attribution_integration_partner: ThirdPartyConversionAttributionIntegrationPartnerEnum.ThirdPartyConversionAttributionIntegrationPartner = ...,
        conversion_attribution_integration_partner_data: ThirdPartyIntegrationPartnerData = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "conversion_attribution_integration_partner",
            "conversion_attribution_integration_partner_data",
        ],
    ) -> bool: ...

class CampaignThirdPartyIntegrationPartners(proto.Message):
    viewability_integration_partners: MutableSequence[
        CampaignThirdPartyViewabilityIntegrationPartner
    ]
    brand_lift_integration_partners: MutableSequence[
        CampaignThirdPartyBrandLiftIntegrationPartner
    ]
    brand_safety_integration_partners: MutableSequence[
        CampaignThirdPartyBrandSafetyIntegrationPartner
    ]
    reach_integration_partners: MutableSequence[
        CampaignThirdPartyReachIntegrationPartner
    ]
    conversion_attribution_integration_partners: MutableSequence[
        CampaignThirdPartyConversionAttributionIntegrationPartner
    ]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        viewability_integration_partners: MutableSequence[
            CampaignThirdPartyViewabilityIntegrationPartner
        ] = ...,
        brand_lift_integration_partners: MutableSequence[
            CampaignThirdPartyBrandLiftIntegrationPartner
        ] = ...,
        brand_safety_integration_partners: MutableSequence[
            CampaignThirdPartyBrandSafetyIntegrationPartner
        ] = ...,
        reach_integration_partners: MutableSequence[
            CampaignThirdPartyReachIntegrationPartner
        ] = ...,
        conversion_attribution_integration_partners: MutableSequence[
            CampaignThirdPartyConversionAttributionIntegrationPartner
        ] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "viewability_integration_partners",
            "brand_lift_integration_partners",
            "brand_safety_integration_partners",
            "reach_integration_partners",
            "conversion_attribution_integration_partners",
        ],
    ) -> bool: ...

class CampaignThirdPartyReachIntegrationPartner(proto.Message):
    reach_integration_partner: (
        ThirdPartyReachIntegrationPartnerEnum.ThirdPartyReachIntegrationPartner
    )
    reach_integration_partner_data: ThirdPartyIntegrationPartnerData
    share_cost: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        reach_integration_partner: ThirdPartyReachIntegrationPartnerEnum.ThirdPartyReachIntegrationPartner = ...,
        reach_integration_partner_data: ThirdPartyIntegrationPartnerData = ...,
        share_cost: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "reach_integration_partner", "reach_integration_partner_data", "share_cost"
        ],
    ) -> bool: ...

class CampaignThirdPartyViewabilityIntegrationPartner(proto.Message):
    viewability_integration_partner: ThirdPartyViewabilityIntegrationPartnerEnum.ThirdPartyViewabilityIntegrationPartner
    viewability_integration_partner_data: ThirdPartyIntegrationPartnerData
    share_cost: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        viewability_integration_partner: ThirdPartyViewabilityIntegrationPartnerEnum.ThirdPartyViewabilityIntegrationPartner = ...,
        viewability_integration_partner_data: ThirdPartyIntegrationPartnerData = ...,
        share_cost: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "viewability_integration_partner",
            "viewability_integration_partner_data",
            "share_cost",
        ],
    ) -> bool: ...

class CustomerThirdPartyBrandLiftIntegrationPartner(proto.Message):
    brand_lift_integration_partner: (
        ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner
    )
    allow_share_cost: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        brand_lift_integration_partner: ThirdPartyBrandLiftIntegrationPartnerEnum.ThirdPartyBrandLiftIntegrationPartner = ...,
        allow_share_cost: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["brand_lift_integration_partner", "allow_share_cost"]
    ) -> bool: ...

class CustomerThirdPartyBrandSafetyIntegrationPartner(proto.Message):
    brand_safety_integration_partner: ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        brand_safety_integration_partner: ThirdPartyBrandSafetyIntegrationPartnerEnum.ThirdPartyBrandSafetyIntegrationPartner = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["brand_safety_integration_partner"]
    ) -> bool: ...

class CustomerThirdPartyConversionAttributionIntegrationPartner(proto.Message):
    conversion_attribution_integration_partner: ThirdPartyConversionAttributionIntegrationPartnerEnum.ThirdPartyConversionAttributionIntegrationPartner
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        conversion_attribution_integration_partner: ThirdPartyConversionAttributionIntegrationPartnerEnum.ThirdPartyConversionAttributionIntegrationPartner = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["conversion_attribution_integration_partner"]
    ) -> bool: ...

class CustomerThirdPartyIntegrationPartners(proto.Message):
    viewability_integration_partners: MutableSequence[
        CustomerThirdPartyViewabilityIntegrationPartner
    ]
    brand_lift_integration_partners: MutableSequence[
        CustomerThirdPartyBrandLiftIntegrationPartner
    ]
    brand_safety_integration_partners: MutableSequence[
        CustomerThirdPartyBrandSafetyIntegrationPartner
    ]
    reach_integration_partners: MutableSequence[
        CustomerThirdPartyReachIntegrationPartner
    ]
    conversion_attribution_integration_partners: MutableSequence[
        CustomerThirdPartyConversionAttributionIntegrationPartner
    ]
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        viewability_integration_partners: MutableSequence[
            CustomerThirdPartyViewabilityIntegrationPartner
        ] = ...,
        brand_lift_integration_partners: MutableSequence[
            CustomerThirdPartyBrandLiftIntegrationPartner
        ] = ...,
        brand_safety_integration_partners: MutableSequence[
            CustomerThirdPartyBrandSafetyIntegrationPartner
        ] = ...,
        reach_integration_partners: MutableSequence[
            CustomerThirdPartyReachIntegrationPartner
        ] = ...,
        conversion_attribution_integration_partners: MutableSequence[
            CustomerThirdPartyConversionAttributionIntegrationPartner
        ] = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self,
        key: Literal[
            "viewability_integration_partners",
            "brand_lift_integration_partners",
            "brand_safety_integration_partners",
            "reach_integration_partners",
            "conversion_attribution_integration_partners",
        ],
    ) -> bool: ...

class CustomerThirdPartyReachIntegrationPartner(proto.Message):
    reach_integration_partner: (
        ThirdPartyReachIntegrationPartnerEnum.ThirdPartyReachIntegrationPartner
    )
    allow_share_cost: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        reach_integration_partner: ThirdPartyReachIntegrationPartnerEnum.ThirdPartyReachIntegrationPartner = ...,
        allow_share_cost: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["reach_integration_partner", "allow_share_cost"]
    ) -> bool: ...

class CustomerThirdPartyViewabilityIntegrationPartner(proto.Message):
    viewability_integration_partner: ThirdPartyViewabilityIntegrationPartnerEnum.ThirdPartyViewabilityIntegrationPartner
    allow_share_cost: bool
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        viewability_integration_partner: ThirdPartyViewabilityIntegrationPartnerEnum.ThirdPartyViewabilityIntegrationPartner = ...,
        allow_share_cost: bool = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["viewability_integration_partner", "allow_share_cost"]
    ) -> bool: ...

class ThirdPartyIntegrationPartnerData(proto.Message):
    client_id: str
    third_party_placement_id: str
    def __init__(
        self: _M,
        mapping: _M | Mapping | google.protobuf.message.Message | None = None,
        *,
        ignore_unknown_fields: bool = False,
        client_id: str = ...,
        third_party_placement_id: str = ...,
    ) -> None: ...
    def __contains__(  # type: ignore[override]
        self, key: Literal["client_id", "third_party_placement_id"]
    ) -> bool: ...
