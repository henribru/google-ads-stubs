import proto
from _typeshed import Incomplete
from google.rpc import status_pb2
from typing import MutableSequence

__protobuf__: Incomplete

class GenerateShareablePreviewsRequest(proto.Message):
    customer_id: str
    shareable_previews: MutableSequence['ShareablePreview']

class ShareablePreview(proto.Message):
    asset_group_identifier: AssetGroupIdentifier

class AssetGroupIdentifier(proto.Message):
    asset_group_id: int

class GenerateShareablePreviewsResponse(proto.Message):
    responses: MutableSequence['ShareablePreviewOrError']

class ShareablePreviewOrError(proto.Message):
    asset_group_identifier: AssetGroupIdentifier
    shareable_preview_result: ShareablePreviewResult
    partial_failure_error: status_pb2.Status

class ShareablePreviewResult(proto.Message):
    shareable_preview_url: str
    expiration_date_time: str
