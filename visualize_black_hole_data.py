import pandas as pd
import matplotlib.pyplot as plt

# Load the expanded dataset
df = pd.read_csv("expanded_black_hole_data.csv")

# Filter out rows with missing values for plotting (since we might have 'N/A' entries)
filtered_df = df[df['Black_Hole_Mass'] != 'N/A']
filtered_df = filtered_df[df['Jet_Length'] != 'N/A']
import pandas as pd
import matplotlib.pyplot as plt

# Load the expanded dataset
df = pd.read_csv("expanded_black_hole_data.csv")

# Filter out rows with missing values or non-positive values
filtered_df = df[df['Black_Hole_Mass'] != 'N/A']
filtered_df = filtered_df[df['Jet_Length'] != 'N/A']

# Convert Black_Hole_Mass and Jet_Length to numeric (since they may have been loaded as strings)
filtered_df['Black_Hole_Mass'] = pd.to_numeric(filtered_df['Black_Hole_Mass'], errors='coerce')
filtered_df['Jet_Length'] = pd.to_numeric(filtered_df['Jet_Length'], errors='coerce')

# Drop any rows that couldn't be converted or have non-positive values
filtered_df = filtered_df.dropna(subset=['Black_Hole_Mass', 'Jet_Length'])
filtered_df = filtered_df[(filtered_df['Black_Hole_Mass'] > 0) & (filtered_df['Jet_Length'] > 0)]

# Check if there's any data left to plot
if filtered_df.empty:
    print("No valid data to plot. Ensure that there are positive values for both Black Hole Mass and Jet Length.")
else:
    # Plot Black Hole Mass vs Jet Length
    plt.figure(figsize=(10, 6))
    plt.scatter(filtered_df['Black_Hole_Mass'], filtered_df['Jet_Length'], color='green', s=100)
    plt.xscale("log")  # Log scale for better visualization
    plt.yscale("log")  # Log scale for better visualization
    plt.xlabel("Black Hole Mass (Solar Masses)")
    plt.ylabel("Jet Length (Parsecs)")
    plt.title("Black Hole Mass vs Jet Length")
    plt.grid(True)
    plt.tight_layout()

    # Save the plot to a file
    plt.savefig("black_hole_mass_vs_jet_length.png")
    plt.show()

    print("Visualization complete. Saved to black_hole_mass_vs_jet_length.png")

