
from astroquery.simbad import Simbad

# Setting up the Simbad instance to search for specific
# black hole and jet information
custom_simbad = Simbad()
custom_simbad.TIMEOUT = 500 # just in case in takes a while

# An example search for an object by name
result = custom_simbad.query_object("M87")

if result:
    print(result)
else:
    print("No result found.")


