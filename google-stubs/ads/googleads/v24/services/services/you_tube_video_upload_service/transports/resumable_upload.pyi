import datetime
from dataclasses import dataclass
from typing import BinaryIO, Callable, Sequence

import google.api_core.retry
import requests
from _typeshed import Incomplete

from .resumable_upload_error_adapter import (
    raise_formatted_for_status as raise_formatted_for_status,
)

@dataclass(frozen=True)
class ResumableUploadStatus:
    upload_url: str
    total_bytes: int | None
    bytes_uploaded: int
    finished: bool

class ResumableUpload:
    initial_url: Incomplete
    stream: Incomplete
    size: Incomplete
    content_type: Incomplete
    chunk_size: Incomplete
    deadline: Incomplete
    extra_headers: Incomplete
    on_progress: Incomplete
    session_url: Incomplete
    bytes_uploaded: int
    finished: bool
    chunk_granularity: Incomplete
    def __init__(
        self,
        upload_url: str,
        stream: BinaryIO,
        size: int | None = None,
        content_type: str | None = None,
        chunk_size: int | None = None,
        deadline: datetime.datetime | None = None,
        headers: Sequence[tuple[str, str | bytes]] | None = None,
        on_progress: Callable[[ResumableUploadStatus], None] | None = None,
    ) -> None: ...
    def initiate(
        self,
        transport: requests.Session,
        request_body: str = "",
        request_retry: google.api_core.retry.Retry | None = None,
    ): ...
    def transmit_next_chunk(self, transport: requests.Session) -> requests.Response: ...

def make_resumable_upload(
    transport: requests.Session,
    request_body: str,
    stream: BinaryIO,
    upload_url: str,
    size: int | None = None,
    content_type: str | None = None,
    chunk_size: int | None = None,
    request_retry: google.api_core.retry.Retry | None = None,
    deadline: datetime.datetime | None = None,
    headers: Sequence[tuple[str, str | bytes]] | None = None,
    on_progress: Callable[[ResumableUploadStatus], None] | None = None,
) -> requests.Response: ...
