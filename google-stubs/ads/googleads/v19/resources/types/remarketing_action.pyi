import proto
from _typeshed import Incomplete
from google.ads.googleads.v19.common.types import tag_snippet
from typing import MutableSequence

__protobuf__: Incomplete

class RemarketingAction(proto.Message):
    resource_name: str
    id: int
    name: str
    tag_snippets: MutableSequence[tag_snippet.TagSnippet]
