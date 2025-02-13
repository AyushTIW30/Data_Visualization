# Data Visualization Series

This project demonstrates a series of data visualizations using Python libraries such as **Matplotlib**, **Seaborn**, **Pandas**, and **NumPy**. The script covers various types of plots like line charts, scatter plots, bar charts, histograms, and pie charts to represent different datasets.

## Libraries Used
- **Matplotlib**: For creating basic visualizations such as line plots, scatter plots, bar charts, and histograms.
- **Seaborn**: For enhanced visualizations with additional styling.
- **Pandas**: For data manipulation and handling CSV files.
- **NumPy**: For generating arrays and numerical operations.

## How to Run
### Prerequisites:
Ensure that the following libraries are installed on your system:
- **Matplotlib**
- **Seaborn**
- **Pandas**
- **NumPy**

You can install them using pip:
```bash
pip install numpy pandas matplotlib seaborn
Running the Script:
Download or clone the repository.
Ensure that the necessary data files (such as sharma-kohli.csv, tips.csv, etc.) are present in the same directory as the script.
Run the Python script:
bash
python script_name.py
The script will generate various visualizations depending on the section of code you choose to run.

Visualizations Included:
1. Line Plots
Simple line plots to show changes over time or comparisons between different data series.
Example: Price over years, Player scores over seasons.
python
plt.plot(year, price)
plt.title("Price Over Years")
plt.xlabel("Year")
plt.ylabel("Price")
plt.show()
2. Line Plots with Markers
Line plots featuring markers (e.g., +, *) to distinguish between data series.
3. Legends in Line Plots
Legends are added to line plots to label each series (e.g., comparing player scores).
python
plt.plot(match["index"], match["V Kohli"], label="Kohli")
plt.plot(match["index"], match["RG Sharma"], label="Rohit")
plt.legend(loc="upper right")
4. Scatter Plots
Used for plotting relationships between two variables, such as batting average and strike rate.
Example: Scatter plot showing total bill vs. tip size.
python
plt.scatter(x, y)
plt.show()
5. Bar Charts
Both vertical and horizontal bar charts are used to compare categorical data.
python
plt.barh(color, child, color="red")
plt.show()
6. Stacked Bar Charts
Represent multiple datasets stacked on top of each other to compare contributions to a whole.
7. Histograms
Used to show the frequency distribution of a dataset. Customizable bin ranges and log scaling.
python

plt.hist(arr, bins=[10, 20, 30, 40, 50, 60, 70], log=True)
plt.show()
8. Pie Charts
Used to show proportions of different categories in a dataset.
python
plt.pie(data, labels=sub)
plt.show()
Example Outputs:
Line Plot: Price fluctuations over the years.
Scatter Plot: Plotting batting averages against strike rates.
Bar Chart: Displaying batting performance by year.
Histogram: Distribution of player runs in a match.
Pie Chart: Contribution of different players in a match.
Notes:
The visualizations are based on the data provided in CSV files. Make sure to update the file paths as necessary.
The code is customizable for different datasets and additional visualizations can be added.
License
This project is licensed under the MIT License - see the LICENSE file for details.
