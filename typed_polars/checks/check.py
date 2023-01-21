from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass

import polars as pl


# https://pandera.readthedocs.io/en/stable/
# https://aeturrell.github.io/coding-for-economists/data-advanced.html
# https://pandera.readthedocs.io/en/stable/data_format_conversion.html


@dataclass
class ValidationResult:
    msg: str
    passed: bool

    @staticmethod
    def combine_all(results: list[ValidationResult]) -> ValidationResult:
        return ValidationResult(
            msg="\n".join([m.msg for m in results if m is not None]),
            passed=all([m.passed for m in results if m is not None]),
        )


class Check(ABC):
    @abstractmethod
    def validate_column(self, series: pl.Series) -> ValidationResult:
        pass

    def validate_frame_column(self, df: pl.DataFrame, column: str) -> ValidationResult:
        return self.validate_column(df[column])
