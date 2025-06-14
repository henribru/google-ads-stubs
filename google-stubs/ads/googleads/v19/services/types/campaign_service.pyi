import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.enums.types import response_content_type as gage_response_content_type
from google.ads.googleads.v19.resources.types import campaign as gagr_campaign
from google.protobuf import field_mask_pb2
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCampaignsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CampaignOperation']
    partial_failure: bool
    validate_only: bool
    response_content_type: gage_response_content_type.ResponseContentTypeEnum.ResponseContentType

class CampaignOperation(proto.Message):
    update_mask: field_mask_pb2.FieldMask
    create: gagr_campaign.Campaign
    update: gagr_campaign.Campaign
    remove: str

class MutateCampaignsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateCampaignResult']

class MutateCampaignResult(proto.Message):
    resource_name: str
    campaign: gagr_campaign.Campaign

class EnablePMaxBrandGuidelinesRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['EnableOperation']

class EnableOperation(proto.Message):
    campaign: str
    auto_populate_brand_assets: bool
    brand_assets: BrandCampaignAssets
    final_uri_domain: str
    main_color: str
    accent_color: str
    font_family: str

class BrandCampaignAssets(proto.Message):
    business_name_asset: str
    logo_asset: MutableSequence[str]
    landscape_logo_asset: MutableSequence[str]

class EnablePMaxBrandGuidelinesResponse(proto.Message):
    results: MutableSequence['EnablementResult']

class EnablementResult(proto.Message):
    campaign: str
    enablement_error: status_pb2.Status
