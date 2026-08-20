# FPL Model Project Context

## Purpose

Build a transparent Fantasy Premier League prediction model.

The goals are:

1. Learn data science and modelling skills.
2. Build a useful FPL tool.
3. Understand which signals predict future FPL performance.
4. Create a substantial portfolio project.

This project prioritises understanding and explainability over creating a black-box prediction system.

---

# Core Philosophy

The model is inspired by FPL models such as Tokvam's Transfer Algorithm.

The key principles are:

## 1. Separate player ability from opportunity

A player's FPL value depends on:

- how good they are when playing
- how often they play

A high-quality player with uncertain minutes may be a worse FPL asset than a slightly weaker player who starts every week.

---

## 2. Predict components, not points directly

The intended architecture:

Player Strength
+
Expected Minutes
+
Fixture Difficulty
+
Price

↓

Expected FPL Value

↓

Squad Optimisation

---

## 3. Backtesting is central

All modelling choices should be evaluated against historical future performance.

The question is always:

"Does this improve prediction?"

not:

"Does this look clever?"

---

# Current Model Status

## Completed

- FPL data ingestion
- Historical gameweek dataset
- First-half → second-half backtesting framework
- Player performance metrics
- Initial Player Strength model

---

# Current Player Strength Model

Purpose:

Estimate how good a player is when they play.

Current approach:

50% historical FPL performance
+
50% underlying performance

The model also includes a confidence adjustment based on minutes played.

---

# Current Findings

Player Strength correlation with future PP90:

Overall:
≈ 0.60

By position:

MID:
≈ 0.58

DEF:
≈ 0.39

FWD:
≈ 0.06

GK:
≈ -0.04

Important discovery:

PP90 may not be the correct validation target for all positions.

Forwards showed stronger relationships between xG/xA and future total points than future PP90.

Hypothesis:

Minutes and opportunity dominate FPL value.

---

# Current Priority

Improve Player Strength before building optimisation.

Next steps:

1. Compare baseline models.
2. Test against future total points.
3. Build position-specific models.
4. Add expected minutes.
5. Add fixture adjustment.
6. Build valuation model.
7. Build optimisation layer.

---

# Important Constraints

Do not jump prematurely into:

- complex machine learning
- neural networks
- dashboards
- optimisation

The prediction layer comes first.