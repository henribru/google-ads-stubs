import proto
from _typeshed import Incomplete
from google.rpc import status_pb2 as status_pb2

from google.ads.googleads.v11.resources.types import campaign_label as campaign_label

__protobuf__: Incomplete

class MutateCampaignLabelsRequest(proto.Message):
    customer_id: Incomplete
    operations: Incomplete
    partial_failure: Incomplete
    validate_only: Incomplete

class CampaignLabelOperation(proto.Message):
    create: Incomplete
    remove: Incomplete

class MutateCampaignLabelsResponse(proto.Message):
    partial_failure_error: Incomplete
    results: Incomplete

class MutateCampaignLabelResult(proto.Message):
    resource_name: Incomplete
