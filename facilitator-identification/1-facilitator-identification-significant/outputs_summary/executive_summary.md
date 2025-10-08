# Executive Summary — Person-level Analyses

**Dataset:** person-year with derived outcomes and annotations.

**Controls considered:** speaking duration (`p_speaking_duration_sec`) and number of turns (`p_turns`).

## Outlier checks (controls)

| Control | Outliers (N) | Outliers (%) | Kept rows |
|---|---:|---:|---:|
| `p_speaking_duration_sec` | 29 | 3.8% | 717 |
| `p_turns` | 48 | 6.2% | 717 |

## Facilitator vs Non-facilitator (`role_facilitator`)

_No models fit._

## Number of teams (count) (`num_teams`)

**Significant annotation terms (p < 0.05, full data):**

| Term | Model | Coef (SE) | p | CI | N | Pseudo R² |
|---|---|---:|---:|---|---:|---:|
| `ann_idea_management_mean_score` | Number of teams (count) — ANN only, full | -1.577 (0.759) | 0.0389 | [-3.072, -0.081] | 273 |  |
| `ann_idea_management_mean_score` | Number of teams (count) — ANN+controls, full | -1.571 (0.762) | 0.0405 | [-3.073, -0.069] | 273 |  |
| `ann_participation_dynamics_mean_score` | Number of teams (count) — ANN only, full | -0.742 (0.235) | 0.00181 | [-1.205, -0.279] | 273 |  |
| `ann_participation_dynamics_mean_score` | Number of teams (count) — ANN+controls, full | -0.739 (0.236) | 0.00196 | [-1.205, -0.274] | 273 |  |

## Number of funded teams (count) (`num_funded_teams`)

**Significant annotation terms (p < 0.05, full data):**

| Term | Model | Coef (SE) | p | CI | N | Pseudo R² |
|---|---|---:|---:|---|---:|---:|
| `ann_evaluation_practices_mean_score` | Number of funded teams (count) — ANN+controls, full | 0.497 (0.232) | 0.0331 | [0.040, 0.953] | 273 |  |
| `ann_evaluation_practices_mean_score` | Number of funded teams (count) — ANN only, full | 0.493 (0.231) | 0.0336 | [0.038, 0.947] | 273 |  |
| `ann_integration_practices_mean_score` | Number of funded teams (count) — ANN only, full | 0.433 (0.207) | 0.0376 | [0.025, 0.840] | 273 |  |
| `ann_integration_practices_mean_score` | Number of funded teams (count) — ANN+controls, full | 0.426 (0.209) | 0.0431 | [0.013, 0.838] | 273 |  |
