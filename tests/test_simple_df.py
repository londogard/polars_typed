import polars as pl
import typed_polars as pt


def test_only_types():
    df = pl.DataFrame({"name": ["Hampus", "Dennis", "Noah"], "age": [28, 26, 20]})

    schema = pt.DataFrameSchema(
        {"name": pt.Column(pl.Utf8), "age": pt.Column(pl.Int64)}
    )

    result = schema.validate(df)

    assert result.passed

    df = pl.DataFrame({"age": ["Hampus", "Dennis", "Noah"], "name": [28, 26, 20]})
    result = schema.validate(df)

    assert not result.passed
