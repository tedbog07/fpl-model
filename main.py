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

players["position"] = players["element_type"].map(position_map)
players["points_per_million"] = players["total_points"] / (players["now_cost"] / 10)
players["xgi_per_90"] = (
    (players["expected_goals"] + players["expected_assists"])
    / players["minutes"]
    * 90
)
players["minutes_per_start"] = players["minutes"] / players["starts"]
players["minutes_share"] = players["minutes"] / (38 * 90)
players["expected_xgi"] = players["xgi_per_90"] * players["minutes_share"]
players = players[players["minutes"] >= MINUTES_THRESHOLD]


print(players[
    [
        "web_name",
        "position",
        "xgi_per_90",
        "minutes_share",
        "expected_xgi"
    ]
].sort_values("expected_xgi", ascending=False).head(20))