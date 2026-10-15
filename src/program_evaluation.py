"""Real difference-in-differences program evaluation: estimates the
treatment effect as the gain in the treatment group minus the gain in
the control group, with a two-sample t-test for significance."""
from __future__ import annotations

import pandas as pd
from scipy import stats


def difference_in_differences(df: pd.DataFrame) -> dict:
    df = df.copy()
    df["change"] = df["post_score"] - df["baseline_score"]

    treat_change = df.loc[df["group"] == "treatment", "change"]
    control_change = df.loc[df["group"] == "control", "change"]

    did_estimate = treat_change.mean() - control_change.mean()
    t_stat, p_value = stats.ttest_ind(treat_change, control_change)

    return {
        "treatment_mean_change": round(float(treat_change.mean()), 3),
        "control_mean_change": round(float(control_change.mean()), 3),
        "did_estimate": round(float(did_estimate), 3),
        "p_value": float(p_value),
        "n_treatment": int(len(treat_change)), "n_control": int(len(control_change)),
    }


def validate_effect_recovery(result: dict, true_effect: float) -> dict:
    estimate = result["did_estimate"]
    abs_error = abs(estimate - true_effect)
    pct_error = round(100 * abs_error / true_effect, 2)
    return {"true_effect": true_effect, "estimated_effect": estimate,
            "absolute_error": round(abs_error, 3), "pct_error": pct_error,
            "effect_detected_significant": result["p_value"] < 0.05}
