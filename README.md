# Happiness Data Explorer: Interactive Visualization of Well-being Factors

This project creates a simple, interactive **web application** that allows users to explore the relationship between different factors influencing global happiness. It utilizes **Streamlit** for the web interface and **Plotly Express** for dynamic, insightful visualizations.

## Overview

The "Happiness Data Explorer" is designed to make it easy to visualize how metrics like Gross Domestic Product (GDP), happiness scores, and generosity might correlate with each other. By providing interactive dropdown menus for axis selection, users can quickly generate scatter plots to uncover potential trends and relationships within the data, helping to understand the drivers of well-being.

## Features

* **Interactive Scatter Plots:** Generates dynamic scatter plots to visualize the relationship between two selected variables.
* **Customizable Axes:** Allows users to choose which data points (e.g., GDP, happiness, generosity) appear on the X and Y axes using intuitive dropdown menus.
* **Clear Labeling:** Automatically updates plot titles and axis labels to reflect the user's selections.
* **Web Interface:** Built with Streamlit for easy access and interaction through a web browser.
* **Data Exploration:** Facilitates quick visual exploration of correlations within happiness-related datasets.

## Technologies Used

* Python
* Streamlit (for the web application)
* Plotly Express (for interactive charts)
* Pandas (for data handling and reading CSV files)

## How It Works

The application operates by performing the following steps:

1.  **Application Initialization:**
    * Sets up the Streamlit application with a main header "In Search for Happiness".

2.  **User Input for Axes:**
    * Two `st.selectbox` widgets are presented to the user, allowing them to select a variable for the X-axis and another for the Y-axis. The available options are "gdp", "happiness", and "generosity".
    * A subheader dynamically displays the selected variables (e.g., "gdp and happiness").

3.  **Data Loading:**
    * The application reads the data from a CSV file named `happy.csv`.

4.  **Data Extraction and Plotting:**
    * Based on the user's selections from the dropdowns, the corresponding columns are extracted from the `happy.csv` DataFrame.
    * `plotly.express.scatter` is then used to create an interactive scatter plot using the selected X and Y axis data.
    * The plot's labels are set dynamically to match the chosen variables.

5.  **Visualization Display:**
    * The generated interactive Plotly scatter plot is displayed within the Streamlit web application using `st.plotly_chart()`.

## Data Requirement

This project requires a CSV file named `happy.csv` to be present in the same directory as the script. This `happy.csv` file is expected to contain at least the following columns:

* `gdp` (e.g., representing GDP per capita or similar economic indicator)
* `happiness` (e.g., a happiness score or index)
* `generosity` (e.g., a measure of generosity or charitable contributions)

The columns will be used to populate the dropdown selection boxes and generate the interactive scatter plots.
