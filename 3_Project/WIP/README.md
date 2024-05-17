# Introduction

📊 Dive into the data job market! This project focuses on data analyst roles and explores top-paying jobs, in-demand skills, and the intersection of high demand and high salary in data analytics.

🔍 Python Code? Check them out here: [project_python folder](/project_python/)

# Background

I wanted to navigate the data analyst job market more effectively, this project was created from a desire to find the top-paid and in-demand skills to find optimal jobs.  

The data is from my [Python Course](https://lukebarousse.com/python). It's packed with insights on job titles, salaries, locations, and essential skills.

### The questions I wanted to answer through my Python scripts were:
1. What are the skills most in demand for the top 3 most popular data roles?
2. How are in-demand skills trending for Data Analysts?
3. How well do jobs and skills pay for Data Analysts?
4. What is the optimal skill for data analysts to learn? (High Demand AND High Paying) 

# Tools I Used

For my deep dive into the data analyst job market, I harnessed the power of several key tools:

- **Python:** The backbone of my analysis, allowing me to analyze the data and find critical insights.
    - **Pandas Library:** The Python library used to analyze the data. 
    - **Matplotlib Library:** The library I used to visualize my data. 
- **Jupyter Notebooks:** The tool I used to run my Python scripts which let me easily include my notes and analysis.
- **Visual Studio Code:** My go-to for executing my Python scripts.
- **Git & GitHub:** Essential for version control and sharing my Python code and analysis, ensuring collaboration and project tracking.

# Prepare Data

Below are the steps I took to prepare the data for analysis. 

## Import & Clean Up Data

I imported the libraries, load in my CSV file, and cleaned up the DataFrame. 

```python
# Importing Libraries
import ast
import pandas as pd
import seaborn as sns
from datasets import load_dataset
import matplotlib.pyplot as plt  

# Loading Data
dataset = load_dataset('lukebarousse/data_jobs')
df = dataset['train'].to_pandas()

# Data Cleanup
df['job_posted_date'] = pd.to_datetime(df['job_posted_date'])
df['job_skills'] = df['job_skills'].apply(lambda x: ast.literal_eval(x) if pd.notna(x) else x)
```

## Filter US Jobs

Then I only got data jobs in the United States. 

```python
df_US = df[df['job_country'] == 'United States']

```

# The Analysis

Each python script for this project aimed at investigating specific aspects of the data job market. Here’s how I approached each question:

## What are the most demanded skills for the top 3 most popular data roles?

To find the most demanded skills for the top 3 most popular data roles. I filtered out those positions by which ones were the most popular, and got the top 5 skills for these top 3 roles. This query highlights the most popular job titles and their top skills, showing which skills I should pay attention to depending on the role I'm targeting. 

View my notebook with detailed steps here: [2_Skills_Count](/project_python/).

### Visualize Data

This is the basic code I used to visualize the data. 

```python
fig, ax = plt.subplots(len(job_titles), 1)


for i, job_title in enumerate(job_titles):
    df_plot = df_skills_perc[df_skills_perc['job_title_short'] == job_title].head(5)[::-1]
    sns.barplot(data=df_plot, x='skill_percent', y='job_skills', ax=ax[i], hue='skill_count', palette='dark:b_r')

plt.show()
```

### Results

Here's the breakdown of the most demanded skills for the top 3 most popular data roles:

![Likelihood of Skills Requested in the US Job Postings](images/Likelihood_of_Skills_Requested_in_US_Job_Postings.png)
*Bar graph visualizing the salary for the top 3 data roles and their top 5 skills associated with each*

Insights:

- **Dominant Skills by Role**: SQL is the most requested skill for Data Analysts and Data Scientists, with it in over half the job postings for both roles. For Data Engineers, Python is the most sought-after skill, appearing in 68% of job postings.
- **Specialized vs. General Skills**: Data Engineers require more specialized technical skills (AWS, Azure, Spark) compared to Data Analysts and Data Scientists who are expected to be proficient in more general data management and analysis tools (Excel, Tableau).
- **Commonality Across Roles**: Python is a versatile skill, highly demanded across all three roles, but most prominently for Data Scientists (72%) and Data Engineers (65%).

## 2. How are in-demand skills trending for Data Analysts?

To find how skills are trending in 2023 for Data Analysts, I filtered data analyst positions and grouped the skills by the month of the job postings. This script got the top 5 skills of data analysts by month, showing how popular skills were throughout 2023.

View my notebook with detailed steps here: [3_Skills_Trend](/project_python/).

### Visualize Data

This is the basic code I used to visualize the data. 

```python

from matplotlib.ticker import PercentFormatter

df_plot = df_DA_US_percent.iloc[:, :5]
sns.lineplot(data=df_plot, dashes=False, legend='full', palette='tab10')

plt.gca().yaxis.set_major_formatter(PercentFormatter(decimals=0))

plt.show()

```

### Results
Here's the trends of the top 5 skills of data analyst jobs in 2023:


![Trending Top Skills for Data Analysts in the US](images/Trending_Top_Skills_for_Data_Analysts_in_the_US.png)

*Bar graph visualizing the trending top skills for data analysts in the US.*

Insights:
- **Consistent Demand for SQL**: SQL remains the most consistently demanded skill throughout the year, although it shows a gradual decrease in demand.
- **Rising Importance of Excel**: Excel experienced a significant increase in demand starting around September, surpassing both Python and Tableau by the end of the year.
- **Fluctuations in Python and Tableau**: Both Python and Tableau show relatively stable demand throughout the year with some fluctuations but remain essential skills for data analysts. Power BI, while less demanded compared to the others, shows a slight upward trend towards the year's end.

## 3. How well do jobs and skills pay for Data Analysts?

To identify the highest-paying roles, I filtered data analyst positions by average yearly salary and location, focusing on remote jobs. This query highlights the high paying opportunities in the field.

View my notebook with detailed steps here: [2_Skills_Count](/project_python/).

### Prepare Data

```python

```

### Visualize Data

```python

```

### Results
Here's the breakdown of the top data analyst jobs in 2023:


![Top 10 Skills by Percent Demand in Job Postings](images/Top_10_Skills_by_Percent_Demand_in_Job_Postings.png)
*Bar graph visualizing the salary for the top 10 salaries for data analysts; ChatGPT generated this graph from my SQL query results*


## Bonus: What is the most optimal skill to learn for Data Analysts?

To identify the highest-paying roles, I filtered data analyst positions by average yearly salary and location, focusing on remote jobs. This query highlights the high paying opportunities in the field.

View my notebook with detailed steps here: [2_Skills_Count](/project_python/).

### Prepare Data

```python

```

### Visualize Data

```python

```

### Results
Here's the breakdown of the top data analyst jobs in 2023:


![Top 10 Skills by Percent Demand in Job Postings](images/Top_10_Skills_by_Percent_Demand_in_Job_Postings.png)
*Bar graph visualizing the salary for the top 10 salaries for data analysts; ChatGPT generated this graph from my SQL query results*


# What I Learned

Throughout this adventure, I've turbocharged my SQL toolkit with some serious firepower:

- **🧩 Complex Query Crafting:** Mastered the art of advanced SQL, merging tables like a pro and wielding WITH clauses for ninja-level temp table maneuvers.
- **📊 Data Aggregation:** Got cozy with GROUP BY and turned aggregate functions like COUNT() and AVG() into my data-summarizing sidekicks.
- **💡 Analytical Wizardry:** Leveled up my real-world puzzle-solving skills, turning questions into actionable, insightful SQL queries.

- # Insights
From the analysis, several general insights emerged:

# Conclusions
This project enhanced my SQL skills and provided valuable insights into the data analyst job market. The findings from the analysis serve as a guide to prioritizing skill development and job search efforts. Aspiring data analysts can better position themselves in a competitive job market by focusing on high-demand, high-salary skills. This exploration highlights the importance of continuous learning and adaptation to emerging trends in the field of data analytics.
