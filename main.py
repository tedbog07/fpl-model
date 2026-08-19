# Fantasy Premier League prediction model
import requests
import pandas as pd

MINUTES_THRESHOLD = 500

url = "https://fantasy.premierleague.com/api/bootstrap-static/"

response = requests.get(url)

data = response.json()

players = pd.DataFrame(data["elements"])

players["expected_goals"] = pd.to_numeric(players["expected_goals"])
players["expected_assists"] = pd.to_numeric(players["expected_assists"])


position_map = {
    1: "Goalkeeper",
    2: "Defender",
    3: "Midfielder",
    4: "Forward"
}
goal_points_map = {
    "Goalkeeper": 10,
    "Defender": 6,
    "Midfielder": 5,
    "Forward": 4
}

players["position"] = players["element_type"].map(position_map)
players["points_per_million"] = players["total_points"] / (players["now_cost"] / 10)
players["xgi_per_90"] = (
    (players["expected_goals"] + players["expected_assists"])
    / players["minutes"]
    * 90
)
players["minutes_per_start"] = players["minutes"] / players["starts"]
players["minutes_share"] = players["minutes"] / (38 * 90)
players["start_rate"] = players["starts"] / 38
players["minutes_projection"] = (
    players["minutes_share"] * 0.5
    + players["start_rate"] * 0.5
)
players["expected_xgi"] = players["xgi_per_90"] * players["minutes_share"]
players["goal_points_value"] = players["position"].map(goal_points_map)

players["expected_goal_points"] = (
    players["expected_goals"] * players["goal_points_value"]
)
players["expected_assist_points"] = players["expected_assists"] * 3
players["expected_attacking_points"] = (
    players["expected_goal_points"]
    + players["expected_assist_points"]
)
players["expected_appearance_points"] = (
    players["minutes_share"] * 38 * 2
)
players["expected_total_points"] = (
    players["expected_attacking_points"]
    + players["expected_appearance_points"]
)
players["adjusted_attacking_points"] = (
    players["expected_attacking_points"]
    * players["minutes_projection"]
)
players["actual_pp90"] = (
    players["total_points"] / players["minutes"] * 90
)

players = players[players["minutes"] >= MINUTES_THRESHOLD]



print(players[
    [
        "web_name",
        "position",
        "minutes",
        "total_points",
        "actual_pp90"
    ]
].sort_values("actual_pp90", ascending=False).head(20))