#!/usr/bin/env bash

import importlib
import inspect
from contextlib import contextmanager
from pathlib import Path

import proto


class Writer:
    def __init__(self, file):
        self.file = file
        self.lines = []
        self._indent_level = 0

    @contextmanager
    def indent(self):
        self._indent_level += 1
        yield
        self._indent_level -= 1

    def write(self, s: str = "", end="\n", indent=True, prepend=False):
        if not isinstance(s, str):
            s = str(s)
        if indent:
            s = " " * self._indent_level * 4 + s
        if prepend:
            self.lines.insert(0, s + end)
        else:
            self.lines.append(s + end)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, exc_tb):
        if exc_type is None:
            self.file.writelines(self.lines)


def print_message(cls_name, cls, writer, imports):
    writer.write(f"class {cls_name}(proto.Message):")
    with writer.indent():
        for inner_cls_name, inner_cls in inspect.getmembers(
            cls,
            lambda value: inspect.isclass(value) and issubclass(value, proto.Message),
        ):
            if inner_cls_name != "__base__":
                print_message(inner_cls_name, inner_cls, writer, imports)

        for inner_enum_name, inner_enum in inspect.getmembers(
            cls, lambda value: inspect.isclass(value) and issubclass(value, proto.Enum)
        ):
            writer.write(f"class {inner_enum_name}(proto.Enum):")
            with writer.indent():
                for member_name, member in inner_enum.__members__.items():
                    writer.write(f"{member_name} = {member.value}")

        fields = {}
        for field_name, field in cls.meta.fields.items():
            if field.proto_type in [proto.DOUBLE, proto.FLOAT]:
                type = "float"
            elif field.proto_type in [
                proto.INT64,
                proto.UINT64,
                proto.INT32,
                proto.FIXED64,
                proto.FIXED32,
                proto.UINT32,
                proto.SFIXED32,
                proto.SFIXED64,
                proto.SINT32,
                proto.SINT64,
            ]:
                type = "int"
            elif field.proto_type == proto.BOOL:
                type = "bool"
            elif field.proto_type == proto.STRING:
                type = "str"
            elif field.proto_type == proto.BYTES:
                type = "bytes"
            elif field.proto_type == proto.MESSAGE:
                if isinstance(field.message, str):
                    type = field.message
                else:
                    type = field.message.__qualname__
                    if field.message.__module__ != cls.__module__:
                        imports.append(
                            f"from {field.message.__module__} import {field.message.__qualname__.split('.')[0]}"
                        )
            elif field.proto_type == proto.ENUM:
                if isinstance(field.message, str):
                    type = field.enum
                else:
                    type = field.enum.__qualname__
                    if field.enum.__module__ != cls.__module__:
                        imports.append(
                            f"from {field.enum.__module__} import {field.enum.__qualname__.split('.')[0]}"
                        )
            else:
                raise Exception(field.proto_type)
            if field.repeated:
                type = f"MutableSequence[{type}]"
                imports.append("from collections.abc import MutableSequence")
            fields[field_name] = type
            writer.write(f"{field_name}: {type}")

        writer.write(
            f"def __init__(self: _M, mapping: _M | Mapping | google.protobuf.message.Message | None = ..., *, ignore_unknown_fields: bool = ..., {', '.join(f'{field_name}: {type} = ...' for field_name, type in fields.items())}) -> None: ..."
        )
        quoted_fields = [f'"{field}"' for field in fields]
        writer.write(f"def __contains__(  # type: ignore[override]")
        if quoted_fields:
            writer.write(
                f"self, key: Literal[{', '.join(quoted_fields)}]) -> bool: ..."
            )
        else:
            writer.write(f"self, key: NoReturn) -> bool: ...")


for path in Path("./google-ads-python/google/ads/googleads/").glob("**/types/*.py"):
    if path.stem == "__init__":
        continue
    module = importlib.import_module(".".join([*path.parent.parts[1:], path.stem]))
    with open(
        Path("google-stubs", *path.parent.parts[2:], f"{path.stem}.pyi"), "w"
    ) as file, Writer(file) as writer:
        writer.write("import proto")
        writer.write("import google.protobuf.message")
        writer.write("from typing import Any, TypeVar, NoReturn")
        writer.write("from typing_extensions import Literal")
        writer.write("from collections.abc import Mapping")
        writer.write('_M = TypeVar("_M")')
        imports = []
        for cls_name, cls in inspect.getmembers(
            module,
            lambda value: inspect.isclass(value) and issubclass(value, proto.Message),
        ):
            print_message(cls_name, cls, writer, imports)
        for import_ in imports:
            writer.write(import_, prepend=True)
