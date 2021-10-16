from typing import Any

import proto

from google.ads.googleads.v8.common.types import criteria as criteria
from google.ads.googleads.v8.enums.types import criterion_type as criterion_type

__protobuf__: Any

class CustomerNegativeCriterion(proto.Message):
    resource_name: Any
    id: Any
    type_: Any
    content_label: Any
    mobile_application: Any
    mobile_app_category: Any
    placement: Any
    youtube_video: Any
    youtube_channel: Any
