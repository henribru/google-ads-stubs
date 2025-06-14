import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.resources.types import campaign_label
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class MutateCampaignLabelsRequest(proto.Message):
    customer_id: str
    operations: MutableSequence['CampaignLabelOperation']
    partial_failure: bool
    validate_only: bool

class CampaignLabelOperation(proto.Message):
    create: campaign_label.CampaignLabel
    remove: str

class MutateCampaignLabelsResponse(proto.Message):
    partial_failure_error: status_pb2.Status
    results: MutableSequence['MutateCampaignLabelResult']

class MutateCampaignLabelResult(proto.Message):
    resource_name: str
