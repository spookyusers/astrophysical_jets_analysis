from astroquery.simbad import Simbad
from astroquery.ipac.ned import Ned
import pandas as pd

# List of objects to query
object_names = ["M87", "Cygnus A", "Centaurus A", "Sagittarius A*", "3C 273"]

# Create a Simbad instance
custom_simbad = Simbad()
custom_simbad.TIMEOUT = 500

# Data storage list
data = []

# Alternative names for Sgr A*
alternative_names = {
    "Sagittarius A*": ["Sgr A*", "SgrA", "Galactic Center"]
}

# Query each object
for obj in object_names:
    simbad_result = custom_simbad.query_object(obj)
    if simbad_result is not None:
        # Initializing placeholders
        black_hole_mass = "N/A"
        jet_length = "N/A"

        # Get basic information: Name, RA, DEC from Simbad
        entry = {
            "Name": simbad_result["MAIN_ID"][0],
            "RA": simbad_result["RA"][0],
            "DEC": simbad_result["DEC"][0],
            "Black_Hole_Mass": black_hole_mass,
            "Jet_Length": jet_length
        }

        # Try to get additional properties from NED
        try:
            ned_result = Ned.query_object(obj)
            if len(ned_result) > 0:
                # Extracting additional information from the returned Astropy Table
                ned_row = ned_result[0]
                if 'Diameter' in ned_result.columns:
                    entry["Jet_Length"] = ned_row['Diameter']  # Approximate diameter if available
        except Exception as e:
            # If Sagittarius A* wasn't recognized, try alternative names
            if obj == "Sagittarius A*":
                found = False
                for alt_name in alternative_names["Sagittarius A*"]:
                    try:
                        ned_result = Ned.query_object(alt_name)
                        if len(ned_result) > 0:
                            ned_row = ned_result[0]
                            if 'Diameter' in ned_result.columns:
                                entry["Jet_Length"] = ned_row['Diameter']
                            found = True
                            break
                    except:
                        continue
                if not found:
                    print(f"Could not fetch data for {obj} or its alternatives.")
            else:
                print(f"Could not fetch data from NED for {obj}: {e}")

        # Append data entry
        data.append(entry)

    else:
        print(f"No result found for {obj}")

# Convert to a DataFrame and save as CSV
df = pd.DataFrame(data)
df.to_csv("expanded_black_hole_data.csv", index=False)
print("Data collection complete. Saved to expanded_black_hole_data.csv")

