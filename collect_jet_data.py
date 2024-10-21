
from astroquery.simbad import Simbad
import pandas as pd

object_names = ["M87", "Cygnus A", "Centaurus A", "Sagittarius A*", "3C 273"]

# Setting up the Simbad instance to search for specific
# black hole and jet information
custom_simbad = Simbad()
custom_simbad.TIMEOUT = 500 # just in case in takes a while

# Data storage list
data = []

for obj in object_names:
    result = custom_simbad.query_object(obj)
    if result is not None:
        # Extracting basic information: Name, RA, DEC
        data.append({
            "Name": result["MAIN_ID"][0],
            "RA": result["RA"][0],
            "DEC": result["DEC"][0]
        })
    else:
        print(f"No result found for {obj}")

# Convert to a DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv("black_hole_data.csv", index=False)
print("Data collection complete. Saved to black_hole_data.csv")


