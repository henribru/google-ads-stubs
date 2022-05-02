from typing import Union

import grpc

from google.ads.googleads.v9 import GoogleAdsFailure as GoogleAdsFailureV9
from google.ads.googleads.v10 import GoogleAdsFailure as GoogleAdsFailureV10

GoogleAdsFailure = Union[GoogleAdsFailureV9, GoogleAdsFailureV10]

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
