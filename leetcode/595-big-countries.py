import pandas as pd

data = {
    "name": ["Afghanistan", "Albania", "Algeria", "Andorra", "Angola"],
    "continent": ["Asia", "Europe", "Africa", "Europe", "Africa"],
    "area": [652230, 28748, 2381741, 468, 1246700],
    "population": [25500100, 2831741, 37100000, 78115, 20609294],
    "gdp": [20343000000, 12960000000, 188681000000, 3712000000, 100990000000]
}

inpt = pd.DataFrame(data)

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    return world.loc[(world["area"] >= 3000000) | (world["population"] >= 25000000), ["name", "population", "area"]]


print(big_countries(inpt))