from typing import Any, Optional, Tuple, Dict, List, NamedTuple

import grpc  # type: ignore

class _ClientCallDetails(NamedTuple(
                '_ClientCallDetails',
                [('method', str), ('timeout', float), ('metadata', List[Tuple[str, Any]]), ('credentials', Optional[grpc.CallCredentials])]),
    grpc.ClientCallDetails):
    pass


class InterceptorMixin:
    @classmethod
    def get_request_id_from_metadata(self, trailing_metadata: Tuple[Tuple[str, Any], ...]) -> Optional[str]: ...
    @classmethod
    def parse_metadata_to_json(self, metadata: Tuple[Tuple[str, Any], ...]) -> str: ...
    @classmethod
    def format_json_object(self, obj: Dict[str, Any]) -> str: ...
    @classmethod
    def get_trailing_metadata_from_interceptor_exception(self, exception: grpc.Call) -> Tuple[Tuple[str, Any], ...]: ...
    @classmethod
    def get_client_call_details_instance(cls, method: str, timeout: float, metadata: List[Tuple[str, Any]], credentials: Optional[grpc.CallCredentials] = ...) -> _ClientCallDetails: ...
