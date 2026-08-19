# FPL Model Specification v0.1

## Goal

Build a transparent Fantasy Premier League prediction model that estimates player value using underlying ability, expected minutes, fixtures and price.

The philosophy is inspired by models such as the Transfer Algorithm:
- separate player ability from playing opportunity
- use underlying statistics rather than only historical points
- value recent information more highly
- optimise decisions under budget constraints

---

# Model Architecture

## 1. Player Strength Model

### Question

How good is this player when they play?

### Inputs

Potential inputs:
- historical FPL points
- expected goals (xG)
- expected assists (xA)
- expected goal involvement (xGI)
- shots
- chances created
- defensive statistics

### Output

Underlying points per minute estimate.

---

## 2. Expected Minutes Model

### Question

How often will this player play?

### Inputs

Potential inputs:
- previous minutes
- starts
- injuries
- suspensions
- competition for places
- team rotation
- manual adjustments

### Output

Expected minutes over the projection period.

---

## 3. Fixture Model

### Question

How difficult are upcoming matches?

### Inputs

Potential inputs:
- opponent strength
- home/away advantage
- betting odds
- defensive/attacking team strength

### Output

Fixture-adjusted expected points.

---

## 4. Player Valuation Model

### Question

Is this player worth their price?

### Inputs

- expected points
- player price
- squad budget constraints
- position scarcity

### Output

Player value ranking.

---

## 5. Squad Optimisation

### Question

What is the optimal squad?

Constraints:
- £100m budget
- squad size
- position requirements
- maximum 3 players per club
- transfer rules

Possible outputs:
- starting XI
- bench
- captain
- transfers

---

# Modelling Principles

## 1. Separate ability from opportunity

A player's underlying quality and their expected playing time should be modelled separately.

A great player who does not play is not a great FPL asset.

---

## 2. Predict components, not points directly

The model should estimate the factors that create FPL points:

- attacking output
- defensive output
- appearance likelihood
- clean sheet probability
- bonus potential

rather than simply predicting total points from past points.

---

## 3. Prefer explainable models

Each prediction should have a reason behind it.

The model should answer:

"Why does it think this player is valuable?"

---

## 4. Test assumptions

Model choices should be evaluated by backtesting.

Examples:

- How much should recent data be weighted?
- How much should underlying statistics matter compared to actual points?
- How accurate are minutes projections?

---

## 5. Optimisation comes after prediction

The optimiser should make decisions from good projections.

It should not hide poor assumptions behind mathematical complexity.

---

# Player Strength Model v1

## Purpose

Estimate a player's underlying ability when they are on the pitch.

## Philosophy

Player strength should not rely only on historical FPL points.

Actual points contain both skill and randomness.

Underlying statistics provide information about repeatable performance.

## Formula

Initial version:

Player Strength =
50% actual FPL performance
+
50% underlying-stat performance

Both components will be measured per 90 minutes.

## Recency

More recent seasons and matches should receive greater weighting than older data.

## Future Development

Possible improvements:
- regression models
- machine learning approaches
- feature importance analysis
- comparison against baseline model