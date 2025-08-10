import grpc

from google.ads.googleads.v19.errors import GoogleAdsFailure as GoogleAdsFailureV19
from google.ads.googleads.v20.errors import GoogleAdsFailure as GoogleAdsFailureV20
from google.ads.googleads.v21.errors import GoogleAdsFailure as GoogleAdsFailureV21

GoogleAdsFailure = GoogleAdsFailureV19 | GoogleAdsFailureV20 | GoogleAdsFailureV21

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
