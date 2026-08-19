import pandas as pd

historical = pd.read_csv("data/merged_gw.csv")

print(historical.head())
print(historical.shape)

print(historical["GW"].min())
print(historical["GW"].max())

first_half = historical[historical["GW"] <= 19]

second_half = historical[historical["GW"] > 19]

print(first_half.shape)
print(second_half.shape)

first_half_players = first_half.groupby(
    ["name", "position"]
).sum(numeric_only=True)

print(first_half_players.head())

first_half_players["actual_pp90"] = (
    first_half_players["total_points"]
    / first_half_players["minutes"]
    * 90
)

first_half_players["underlying_attacking_points"] = (
    first_half_players["expected_goals"] * 5
    + first_half_players["expected_assists"] * 3
)

first_half_players["underlying_pp90"] = (
    first_half_players["underlying_attacking_points"]
    / first_half_players["minutes"]
    * 90
)

first_half_players["player_strength"] = (
    first_half_players["actual_pp90"] * 0.5
    + first_half_players["underlying_pp90"] * 0.5
)

first_half_players = first_half_players[
    first_half_players["minutes"] >= 300
]

print(
    first_half_players[
        [
            "total_points",
            "minutes",
            "actual_pp90",
            "underlying_pp90",
            "player_strength"
        ]
    ]
    .sort_values("player_strength", ascending=False)
    .head(20)
)

second_half_players = second_half.groupby(
    ["name", "position"]
).sum(numeric_only=True)

second_half_players = second_half_players[
    second_half_players["minutes"] > 0
]
second_half_players = second_half_players[
    second_half_players["minutes"] >= 300
]

second_half_players["future_pp90"] = (
    second_half_players["total_points"]
    / second_half_players["minutes"]
    * 90
)

print(
    second_half_players[
        ["total_points", "minutes", "future_pp90"]
    ]
    .sort_values("future_pp90", ascending=False)
    .head(20)
)

comparison = first_half_players.merge(
    second_half_players,
    on=["name", "position"],
    suffixes=("_pred", "_future")
)

print(
    comparison[
        [
            "player_strength",
            "future_pp90"
        ]
    ]
    .sort_values("player_strength", ascending=False)
    .head(20)
)

print(
    comparison[
        ["player_strength", "future_pp90"]
    ].corr()
)

print(
    comparison[
        ["actual_pp90", "future_pp90"]
    ].corr()
)