# Backtesting Plan

## Purpose

Evaluate whether the FPL player strength model can predict future player performance.

The goal is not to perfectly predict FPL points, but to test whether the model identifies stronger players better than simpler alternatives.

---

# Core Question

Does a higher player strength score correlate with better future FPL performance?

---

# Test Design

## Input

Information available at a specific point in time:

- Player statistics
- FPL points history
- Underlying attacking statistics
- Minutes played
- Player position
- Team information

The model should only use information that would have been available at that time.

---

## Prediction

The model produces:

- Player strength score
- Ranking of players by predicted ability

---

## Outcome

Compare predictions against future performance:

- Future FPL points per 90
- Future total FPL points
- Future attacking returns

---

# Model Versions To Compare

## Baseline

Simple previous performance:


---

## Model v1

50/50 blend:

---

## Model v1.1

Confidence weighted:


---

# Evaluation Metrics

## Correlation

Does a higher player strength score predict higher future output?

---

## Ranking Accuracy

How many future high-performing players appear near the top of the ranking?

---

## Error

How different are predictions from actual outcomes?

---

# Future Improvements

Potential additions:

- Multiple seasons of player data
- Recency weighting
- Regression models
- Fixture difficulty adjustments
- Expected minutes model
- Transfer optimisation

---

# First Backtest

## Objective

Test whether player strength predicts future player quality.

## Setup

Use first half of season data to predict second half.

Input:
- Gameweeks 1-19

Prediction:
- Player strength score

Outcome:
- Gameweeks 20-38 points per 90

Success metric:
- Correlation between predicted player strength and future points per 90

---

# Dataset Plan

## Initial Scope

Test model across three historical seasons.

Seasons:
- 2023/24
- 2024/25
- 2025/26

## Required Data

Player gameweek-level data:

- Player ID
- Position
- Team
- Minutes
- FPL points
- Goals
- Assists
- Expected goals
- Expected assists

## Initial Test

For each season:

1. Use first half of season to build player strength.
2. Predict second half performance.
3. Compare predictions against actual future points per 90.