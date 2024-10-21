
# visualize black hole data

import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("black_hole_data.csv")

# Plot Right Ascension (RA) vs Declination (DEC)
plt.figure(figsize=(10,6))
plt.scatter(df['RA'], df['DEC'], color='blue', s=50)
plt.xlabel("Right Ascension (RA)")
plt.ylabel("Declination (DEC)")
plt.title("Positions of Astrophysical Jet Sources")
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()
plt.savefig("black_hole_positions.png")
plt.show()

print("Visualization complete. Saved to black_hole_positions.png")



