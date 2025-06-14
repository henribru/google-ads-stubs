import proto
from _typeshed import Incomplete
from google.ads.googleads.v20.common.types import text_label as gagc_text_label
from google.ads.googleads.v20.enums.types import label_status

__protobuf__: Incomplete

class Label(proto.Message):
    resource_name: str
    id: int
    name: str
    status: label_status.LabelStatusEnum.LabelStatus
    text_label: gagc_text_label.TextLabel
