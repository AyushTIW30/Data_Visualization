### Data_Visualization
It contain all the data and resource related to Data Visualization
# Data Visualization Series
This project showcases various data visualizations using Python libraries such as Matplotlib, Seaborn, and Pandas. The visualizations include line plots, scatter plots, bar charts, histograms, and pie charts, demonstrating how to represent and analyze data effectively.

Libraries Used:
NumPy: For numerical operations and generating datasets.
Pandas: For data manipulation and loading CSV files.
Matplotlib: For creating basic visualizations like line plots, scatter plots, bar charts, histograms, and pie charts.
Seaborn: For additional styling and statistical visualizations.
Script Breakdown:
1. Line Plots
Example of a simple line plot to visualize changes over time, such as prices over years or player's performance across seasons.
Customizations include labels, colors, and line styles.
Example:

python

plt.plot(year, price)
plt.title("Price Over Years")
plt.xlabel("Year")
plt.ylabel("Price")
plt.show()
2. Line Plots with Markers
Line plots with markers (like + and *) to differentiate between the data series.
Used to compare different players' performances or similar metrics over time.
3. Adding Legends to Line Plots
Legends are added to line plots to label different data series (e.g., comparing players' scores over time).
4. Customized Axes Limits
Demonstrates how to control the visible range of axes using xlim() and ylim() functions.
5. Scatter Plots
Scatter plots used to display relationships between two variables.
Examples include plotting batting averages against strike rates or total bill vs. tips.
6. Bar Charts
Vertical and horizontal bar charts are used to compare categorical data.
Example: Displaying children's favorite colors or different seasons of a player's performance.
7. Stacked Bar Charts
Shows multiple data sets stacked on top of each other to compare parts of a whole across categories.
8. Histograms
Used to show the distribution of data. The script includes a histogram for batting scores, with customized bin ranges and log scaling.
9. Pie Charts
Pie charts to represent data proportions. Examples include showing the percentage distribution of player runs in a specific match.
Example Outputs:
Line Plot: Tracks price fluctuations over the years.
Scatter Plot: Displays correlations between variables (e.g., batting average vs. strike rate).
Bar Chart: Represents season-wise batting performance for players.
Histogram: Shows the frequency distribution of batsman runs in a match.
Pie Chart: Breaks down the contributions of players in a specific match.
How to Run:
Install the required libraries using pip:
bash
pip install numpy pandas matplotlib seaborn
Ensure you have the necessary CSV files (sharma-kohli.csv, tips.csv, etc.) in the same directory.
Run the Python script.
Notes:
The visualizations are based on the data provided in the respective CSV files.
You can customize the datasets and parameters for further analysis.
