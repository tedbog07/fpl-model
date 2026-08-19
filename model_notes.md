
# Model Notes

## Player Strength Model v1

### Purpose
Estimate player quality using both historical FPL output and underlying attacking statistics.

### Method

Player strength is calculated as:

player_strength =
0.5 × actual_pp90
+
0.5 × underlying_pp90

Where:

actual_pp90:
- FPL points per 90 minutes

underlying_pp90:
- Expected goals converted to FPL points
- Expected assists converted to FPL points

### Backtest

Test:
- Season: 2024/25
- Training period: GW1-GW19
- Evaluation period: GW20-GW38

Results:

Baseline:
- actual_pp90 correlation with future_pp90: 0.550

Player strength model:
- player_strength correlation with future_pp90: 0.593

Finding:
Adding underlying statistics improved future prediction by +0.043 correlation points.