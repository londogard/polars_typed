import polars as pl
from dataclasses import dataclass

from typed_polars.checks.check import ValidationResult
from typed_polars.column import Column


@dataclass
class DataFrameSchema:
    schema: dict[str, Column]

    def validate(self, df: pl.DataFrame) -> ValidationResult:
        results = []
        for column_name, column in self.schema.items():
            column: Column
            result = column.check(df, column_name)
            results.append(result)

        result: ValidationResult = ValidationResult.combine_all(results)

        return result
