"""Simulate a pre/post program evaluation with a treatment group
(enrolled in the program) and a control group, with a known true
program effect embedded independently of the evaluation method --
the real input a program-evaluation framework must recover."""
from __future__ import annotations

import numpy as np
import pandas as pd

N_PARTICIPANTS = 1200
SEED = 347
TRUE_PROGRAM_EFFECT = 6.5  # true improvement attributable to the program


def simulate(n: int = N_PARTICIPANTS, seed: int = SEED):
    rng = np.random.default_rng(seed)

    group = rng.choice(["treatment", "control"], n, p=[0.5, 0.5])
    baseline = rng.normal(60, 12, n)

    secular_trend = rng.normal(2.0, 1.0, n)  # improvement everyone gets regardless of program
    program_effect = np.where(group == "treatment", TRUE_PROGRAM_EFFECT, 0.0)
    noise = rng.normal(0, 5, n)

    post = baseline + secular_trend + program_effect + noise

    df = pd.DataFrame({
        "participant_id": [f"P-{i:05d}" for i in range(n)],
        "group": group, "baseline_score": np.round(baseline, 2),
        "post_score": np.round(post, 2),
    })
    return df, TRUE_PROGRAM_EFFECT


if __name__ == "__main__":
    df, true_effect = simulate()
    print(df.shape, "true effect:", true_effect)
