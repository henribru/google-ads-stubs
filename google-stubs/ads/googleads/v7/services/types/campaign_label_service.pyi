from typing import Any

import proto

from google.ads.googleads.v7.resources.types import campaign_label as campaign_label

__protobuf__: Any

class GetCampaignLabelRequest(proto.Message):
    resource_name: Any

class MutateCampaignLabelsRequest(proto.Message):
    customer_id: Any
    operations: Any
    partial_failure: Any
    validate_only: Any

class CampaignLabelOperation(proto.Message):
    create: Any
    remove: Any

class MutateCampaignLabelsResponse(proto.Message):
    partial_failure_error: Any
    results: Any

class MutateCampaignLabelResult(proto.Message):
    resource_name: Any
