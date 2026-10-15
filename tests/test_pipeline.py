import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from src.simulate_program_data import simulate
from src.program_evaluation import difference_in_differences, validate_effect_recovery


def test_cohort_has_1200_participants():
    df, _ = simulate()
    assert len(df) == 1200


def test_did_recovers_true_effect_within_tolerance():
    df, true_effect = simulate()
    result = difference_in_differences(df)
    recovery = validate_effect_recovery(result, true_effect)
    assert recovery["pct_error"] < 20.0


def test_effect_is_statistically_significant():
    df, true_effect = simulate()
    result = difference_in_differences(df)
    assert result["p_value"] < 0.05


def test_treatment_group_improves_more_than_control():
    df, _ = simulate()
    result = difference_in_differences(df)
    assert result["treatment_mean_change"] > result["control_mean_change"]


def test_groups_are_roughly_balanced():
    df, _ = simulate()
    counts = df["group"].value_counts()
    assert abs(counts["treatment"] - counts["control"]) < 100
