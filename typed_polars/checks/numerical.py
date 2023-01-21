from datetime import date, datetime
from typing import Callable

import polars as pl

def ge(than: float | int | date | datetime) -> Callable[[str], pl.Expr]:
    return lambda x: pl.col(x) > than



# @dataclass
# class MustBeGreater(ColumnValidator):
#     than: float | int | date | datetime
#     inclusive: bool
#
#     def validate_frame_column(self, df: pl.DataFrame, column: str):
#         col = pl.col(column)
#
#         series = df[[column]].filter(col >= self.than if self.inclusive else col > self.than)
#
#         return ValidationResult(
#             f"Number elements outside bounds {self}: {len(df) - len(series)}",
#             len(series) == len(df)
#         )