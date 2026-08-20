# FPL Model Roadmap

## Phase 1 — Player Strength Model

Question:

How good is this player when they play?

Output:

Expected FPL points per 90.

Status:

IN PROGRESS

Tasks:

- Establish baseline model
- Compare actual performance vs underlying statistics
- Test confidence weighting
- Evaluate against future PP90 and total points
- Build position-specific approaches


---

## Phase 2 — Expected Minutes Model

Question:

How often will this player play?

Potential inputs:

- historical minutes
- starts
- injuries
- rotation
- competition for places

Output:

Expected minutes.


---

## Phase 3 — Fixture Model

Question:

How difficult are upcoming matches?

Potential inputs:

- opponent strength
- home advantage
- team attack/defence strength


---

## Phase 4 — Player Valuation

Question:

Is this player worth their price?

Inputs:

- expected points
- price
- position scarcity


---

## Phase 5 — Optimisation

Question:

What squad maximises expected value?

Constraints:

- £100m budget
- squad rules
- formation
- club limits
- transfers
- captaincy