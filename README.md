# Program Performance Evaluation

Difference-in-differences evaluation of a health program's effect on
participant outcomes, with the estimated effect validated against a
known true program effect embedded in the simulation.

> Evaluated a health program's performance across a 1,200-participant
> cohort using a difference-in-differences design; the estimated
> program effect (6.80 points) recovered the true simulated effect
> (6.5 points) within 4.57% error, with the effect statistically
> significant (p < 0.001).

## What's real vs. synthetic — read this first

**Real:** `src/program_evaluation.py` implements a genuine
difference-in-differences estimator (treatment-group change minus
control-group change) with a two-sample t-test for significance.
Because the simulation embeds a known true program effect
independently of the evaluation method, the 4.57% recovery error is a
real, measured result, not an asserted number.

**Synthetic:** there is no real program-participant dataset in this
environment. `src/simulate_program_data.py` generates 1,200
participants split into treatment/control groups, with a true 6.5-
point program effect added only to the treatment group on top of a
shared secular improvement trend both groups experience regardless of
the program.

## Results (real, from `run_all.py`)

```
1,200 participants (582 treatment, 618 control)

Treatment group mean change: +8.383
Control group mean change:   +1.587
DiD estimate:                 6.797
p-value:                      1.45e-94

True effect: 6.5
Estimated effect: 6.797
Absolute error: 0.297 (4.57%)
Effect detected as statistically significant: True
```

`tests/test_pipeline.py` (5 tests, all passing) checks cohort size,
effect recovery within 20% error, statistical significance, treatment
improves more than control, and balanced group sizes.

## Usage

```bash
pip install -r requirements.txt
python3 run_all.py
python3 -m pytest tests/ -v
```

## Project structure

```
src/
  simulate_program_data.py   # 1,200-participant treatment/control simulation
  program_evaluation.py      # difference-in-differences estimator
run_all.py
tests/test_pipeline.py
```

## Tech stack

Python 3.11, scipy (t-test), pandas, numpy, pytest.

## Limitations

- No real program-participant dataset is used.
- The DiD design assumes parallel trends absent the program, which
  holds by construction in this simulation but must be separately
  verified in real evaluations.
