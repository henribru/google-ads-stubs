from typing import Union

import grpc  # type: ignore

from google.ads.google_ads.v3.proto.errors.errors_pb2 import (
    GoogleAdsFailure as GoogleAdsFailureV3,
)
from google.ads.google_ads.v4.proto.errors.errors_pb2 import (
    GoogleAdsFailure as GoogleAdsFailureV4,
)
from google.ads.google_ads.v5.proto.errors.errors_pb2 import (
    GoogleAdsFailure as GoogleAdsFailureV5,
)
from google.ads.google_ads.v6.proto.errors.errors_pb2 import (
    GoogleAdsFailure as GoogleAdsFailureV6,
)

GoogleAdsFailure = Union[
    GoogleAdsFailureV3, GoogleAdsFailureV4, GoogleAdsFailureV5, GoogleAdsFailureV6
]

class GoogleAdsException(Exception):
    error: grpc.RpcError = ...
    call: grpc.Call = ...
    failure: GoogleAdsFailure = ...
    request_id: str = ...
    def __init__(
        self,
        error: grpc.RpcError,
        call: grpc.Call,
        failure: GoogleAdsFailure,
        request_id: str,
    ) -> None: ...
