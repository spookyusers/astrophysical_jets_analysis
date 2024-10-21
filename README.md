# Astrophysical Jets Analysis

## Project Overview

The **Astrophysical Jets Analysis** project aims to explore the relationship between **black hole mass** and **jet length** for different astrophysical sources. The goal is to create a dataset of black holes and their corresponding jets, perform visualizations, and eventually model the relationships between their properties. This study focuses on **active galactic nuclei (AGN)**, **quasars**, and other black holes that have been documented for their powerful jet activity.

### Project Goals:

1. **Data Collection**: Gather data about black holes, specifically their **mass** and **jet length**.
2. **Data Visualization**: Plot **black hole mass** against **jet length** to observe trends or correlations.
3. **Data Expansion**: Use tools like **Astroquery** and **NASA ADS** to find more data and enrich the dataset.
4. **Modeling**: Lay the groundwork for potential modeling of relationships between black hole properties.

## Getting Started

To get started with this project on your local machine, follow the instructions below.

### Prerequisites

- **Python 3.8+**: The codebase is built using Python 3.
- **Git**: For cloning the repository and tracking changes.
- **Virtual Environment**: Recommended for dependency isolation.
- **API Token for NASA ADS**: Required for accessing scientific papers through ADS. You can generate one [here](https://ui.adsabs.harvard.edu/user/settings/token).

### System Requirements

- **OS**: Tested on **Linux Ubuntu**.
- **Python Packages**: The following packages are required and will be installed via `requirements.txt`.
  - `pandas`
  - `matplotlib`
  - `astroquery`
  - `ads`

### Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/astrophysical_jets_analysis.git
   cd astrophysical_jets_analysis
   ```
2. **Create a Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
4. **Set Up NASA ADS Token**:
   Set up the ADS API token as an environment variable to interact with ADS:
   ```bash
   export ADS_DEV_KEY='your_ads_api_key_here'
   ```

## Project Structure

- **expanded_black_hole_data.csv**: The main dataset containing black hole names, coordinates, mass, and jet length.
- **collect_ads_data.py**: Script for querying NASA ADS to gather scientific literature on black holes.
- **collect_jet_data.py**: Script for gathering initial data about black holes using **Astroquery**.
- **visualize_black_hole_data.py**: Script for creating visualizations, such as scatter plots, of black hole mass vs. jet length.
- **requirements.txt**: Lists all required Python packages for the project.
- **README.md**: Contains information about the project, setup, and goals (this file).

## Using the Scripts

### Collecting Data from NASA ADS

To gather data using NASA ADS, run:
```bash
python collect_ads_data.py
```
This will generate a CSV file called `ads_black_hole_papers.csv` that lists relevant papers, which you can use to manually extract further black hole information.

### Expanding the Dataset

After reviewing papers collected from NASA ADS or other sources, add relevant black hole masses and jet lengths to the `expanded_black_hole_data.csv`.

### Visualizing the Data

To visualize the current dataset:
```bash
python visualize_black_hole_data.py
```
This script will generate a scatter plot showing **black hole mass vs. jet length** and save it as `black_hole_mass_vs_jet_length.png`.

## Technical Details

- **Programming Language**: Python 3
- **Data Sources**: 
  - **Simbad** and **NED** via **Astroquery** for initial black hole data.
  - **NASA ADS** for scientific papers.
- **Tools Used**: 
  - **Astroquery**: For accessing astronomical databases.
  - **NASA ADS API**: For searching scientific literature.
  - **Matplotlib**: For plotting and visualizing data.

## Development Workflow

Here is an outline of our workflow during this project:

1. **Data Collection**: Initially used **Astroquery** to gather basic information about black holes and their jets.
2. **Data Enrichment**: Utilized **NASA ADS** to find literature for additional data.
3. **Data Visualization**: Used **Matplotlib** to plot **black hole mass vs. jet length**.
4. **Manual Review and Input**: Enriched data by manually reviewing papers and adding black hole properties to the dataset.

## Future Work

- **Data Automation**: Further automate the process of data collection using NLP tools to parse scientific abstracts.
- **Modeling**: Use machine learning to explore potential relationships between **black hole mass** and **jet properties**.
- **Interactive Visualization**: Improve visualizations to be more interactive, possibly using **Plotly** or **Bokeh**.

## Contributors

- **Kym Derriman** - Project Lead & Developer
- **OpenAI ChatGPT** - Assistance in generating ideas and code guidance

## License

This project is licensed under the MIT License.


