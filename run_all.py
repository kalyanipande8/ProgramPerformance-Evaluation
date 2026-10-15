import json
import os

from src.simulate_program_data import simulate
from src.program_evaluation import difference_in_differences, validate_effect_recovery


def main():
    df, true_effect = simulate()
    result = difference_in_differences(df)
    recovery = validate_effect_recovery(result, true_effect)

    summary = {"n_participants": len(df), "evaluation": result, "effect_recovery": recovery}

    os.makedirs("results", exist_ok=True)
    with open("results/summary.json", "w") as f:
        json.dump(summary, f, indent=2)
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
