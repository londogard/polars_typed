from __future__ import annotations

from dataclasses import dataclass

import polars as pl

from typed_polars import utils
from typed_polars.checks.check import Check, ValidationResult


@dataclass
class Column:
    type_: pl.DataType
    nullable: bool = False

    checks: list[Check] | Check | None = None

    def check(self, df: pl.DataFrame, column: str) -> ValidationResult:
        checks = utils.as_list(self.checks)
        results = []

        # TODO: type check

        for check in checks:
            results.append(check.validate_frame_column(df, column))

        pass


@dataclass
class CastColumn(Column):
    type_: pl.DataType
    nullable: bool = False

    allow_drop_null_on_cast: bool = False

    checks: list[Check] | Check | None = None
