import pandas as pd

cpd = dict()
j = dict()

cpd["wet_grass"] = pd.DataFrame(
    [[False, False, False, 1],
     [False, False, True, 0],
     [True, False, False, 0.1],
     [True, False, True, 0.9],
     [False, True, False, 0.1],
     [False, True, True, 0.9],
     [True, True, False, 0.01],
     [True, True, True, 0.99]],
    columns=["sprinkler", "rain", "wet_grass", "p"]
)
cpd["wet_grass"] = cpd["wet_grass"].pivot_table(index=["sprinkler", "rain"], columns="wet_grass", values="p")

rain = pd.DataFrame(
    [[False, 0.5],
     [True, 0.5]],
    columns=["rain", "p"]
)
j["rain"] = rain.pivot_table(columns="rain")


def wet_grass(cloudy=None, sprinkler=None, rain=None):
    if sprinkler and rain:
        return cpd["wet_grass"].ix[sprinkler, rain]
    elif sprinkler:
        return None
