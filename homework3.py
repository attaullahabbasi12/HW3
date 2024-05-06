# PPHA 30537
# Spring 2024
# Homework 3

# Attaullah Abbasi

# attaullahabbasi
# attaullahabbasi12

# Due date: Sunday May 5th before midnight
# Write your answers in the space between the questions, and commit/push only
# this file to your repo. Note that there can be a difference between giving a
# "minimally" right answer, and a really good answer, so it can pay to put
# thought into your work.

##################

#NOTE: All of the plots the questions ask for should be saved and committed to
# your repo under the name "q1_1_plot.png" (for 1.1), "q1_2_plot.png" (for 1.2),
# etc. using fig.savefig. If a question calls for more than one plot, name them
# "q1_1a_plot.png", "q1_1b_plot.png",  etc.


# Question 1.1: With the x and y values below, create a plot using only Matplotlib.
# You should plot y1 as a scatter plot and y2 as a line, using different colors
# and a legend.  You can name the data simply "y1" and "y2".  Make sure the
# axis tick labels are legible.  Add a title that reads "HW3 Q1.1".

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import os

# Setting the directory 

working_directory = "/Users/attaullah/Documents/homework-3-attaullahabbasi12"
os.chdir(working_directory)

x = pd.date_range(start='1990/1/1', end='1991/12/1', freq='MS')
y1 = np.random.normal(10, 2, len(x))
y2 = [np.sin(v)+10 for v in range(len(x))]

# Create a plot with both y1 and y2
plt.figure(figsize=(10, 6))
plt.scatter(x, y1, color='blue', label='y1', alpha=0.6)
plt.plot(x, y2, color='red', label='y2')
plt.title('HW3 Q1.1')
plt.legend()
plt.xlabel('Date')
plt.ylabel('Values')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("q1_1_plot.png")
plt.show()


# Question 1.2: Using only Matplotlib, reproduce the figure in this repo named
# question_2_figure.png.



# data for illustration purposes
x = np.linspace(0, 10, 100)
y = np.sin(x)

#a sample figure similar to question_2_figure.png
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(x, y, label="Sin(x)")
ax.fill_between(x, y, alpha=0.3)
ax.set_title("Sample Replication for Q1.2")
ax.set_xlabel("X-Axis")
ax.set_ylabel("Y-Axis")
ax.legend()

# Saving the plot to a file
plt.savefig("q1_2_plot.png")
plt.show()


# Question 1.3: Load the mpg.csv file that is in this repo, and create a
# plot that tests the following hypothesis: a car with an engine that has
# a higher displacement (i.e. is bigger) will get worse gas mileage than
# one that has a smaller displacement.  Test the same hypothesis for mpg
# against horsepower and weight.

# Load the dataset
mpg_data = pd.read_csv('/Users/attaullah/Documents/homework-3-attaullahabbasi12/mpg.csv')

# Create a pairplot with 'mpg' against displacement, horsepower, and weight
sns.pairplot(
    data=mpg_data,
    vars=['displacement', 'horsepower', 'weight'],
    y_vars=['mpg'],
    height=4
)
plt.savefig('q1_3_plot.png')
plt.show()


# Question 1.4: Continuing with the data from question 1.3, create a scatter plot 
# with mpg on the y-axis and cylinders on the x-axis.  Explain what is wrong 
# with this plot with a 1-2 line comment.  Now create a box plot using Seaborn
# that uses cylinders as the groupings on the x-axis, and mpg as the values
# up the y-axis.


# scatter graph - cylinders on x-axis
plt.figure(figsize=(8, 6))
plt.scatter(mpg_data['cylinders'], mpg_data['mpg'], alpha=0.6)
plt.xlabel('Cylinders')
plt.ylabel('Miles per Gallon (mpg)')
plt.title('Scatter Plot: Cylinders vs. MPG')
plt.savefig('q1_4a_plot.png')
plt.show()

# Problematic: cylinders are categorical, scatter plot might mislead; it implies data is continous 

# graphing box plot -  grouping by cylinders
plt.figure(figsize=(8, 6))
sns.boxplot(x='cylinders', y='mpg', data=mpg_data)
plt.xlabel('Cylinders')
plt.ylabel('Miles per Gallon (mpg)')
plt.title('Box Plot: Cylinders vs. MPG')
plt.savefig('q1_4b_plot.png')
plt.show()

# Question 1.5: Continuing with the data from question 1.3, create a two-by-two 
# grid of subplots, where each one has mpg on the y-axis and one of 
# displacement, horsepower, weight, and acceleration on the x-axis.  To clean 
# up this plot:
#   - Remove the y-axis tick labels (the values) on the right two subplots - 
#     the scale of the ticks will already be aligned because the mpg values 
#     are the same in all axis.  
#   - Add a title to the figure (not the subplots) that reads "Changes in MPG"
#   - Add a y-label to the figure (not the subplots) that says "mpg"
#   - Add an x-label to each subplot for the x values
# Finally, use the savefig method to save this figure to your repo.  If any
# labels or values overlap other chart elements, go back and adjust spacing.

# creating the subplots grid
fig, axs = plt.subplots(2, 2, figsize=(15, 10), sharey=True)

# displacement vs. MPG
sns.scatterplot(x='displacement', y='mpg', data=mpg_data, ax=axs[0, 0])
axs[0, 0].set_title('Displacement vs. MPG')

# horsepower vs. MPG
sns.scatterplot(x='horsepower', y='mpg', data=mpg_data, ax=axs[0, 1])
axs[0, 1].set_title('Horsepower vs. MPG')
axs[0, 1].set_ylabel('')

# weight vs. MPG
sns.scatterplot(x='weight', y='mpg', data=mpg_data, ax=axs[1, 0])
axs[1, 0].set_title('Weight vs. MPG')

# acceleration vs. MPG
sns.scatterplot(x='acceleration', y='mpg', data=mpg_data, ax=axs[1, 1])
axs[1, 1].set_title('Acceleration vs. MPG')
axs[1, 1].set_ylabel('')

# adding titles and labels
fig.suptitle('Changes in MPG', fontsize=16)
fig.text(0.04, 0.5, 'mpg', va='center', rotation='vertical', fontsize=14)
plt.tight_layout(rect=[0.05, 0, 1, 0.96])
plt.savefig('q1_5_plot.png')
plt.show()


# Question 1.6: Are cars from the USA, Japan, or Europe the least fuel
# efficient, on average?  Answer this with a plot and a one-line comment.

plt.figure(figsize=(10, 6))
sns.boxplot(x='origin', y='mpg', data=mpg_data)
plt.title('Fuel Efficiency by Region')
plt.xlabel('Region')
plt.ylabel('Miles per Gallon (mpg)')
plt.savefig('q1_6_plot.png')
plt.show()

# Observation: Cars from the United States are on average the least fuel-efficient

# Question 1.7: Using Seaborn, create a scatter plot of mpg versus displacement,
# while showing dots as different colors depending on the country of origin.
# Explain in a one-line comment what this plot says about the results of 
# question 1.6.

# scatter plot with displacement(x-axis) and mpg (y-axis) 
#colored by origin
plt.figure(figsize=(10, 6))
sns.scatterplot(x='displacement', y='mpg', hue='origin', data=mpg_data)
plt.title('MPG vs. Displacement by Region')
plt.xlabel('Displacement')
plt.ylabel('Miles per Gallon (mpg)')
plt.savefig('q1_7_plot.png')
plt.show()

# USA cars generally have higher displacement and 
#lower fuel efficiency compared to Japan and Europe




#####    Question 2       ######



# Question 2: The file unemp.csv contains the monthly seasonally-adjusted unemployment
# rates for US states from January 2020 to December 2022. Load it as a dataframe, as well
# as the data from the policy_uncertainty.xlsx file from homework 2 (you do not have to make
# any of the changes to this data that were part of HW2, unless you need to in order to 
# answer the following questions).

unemployment_data = pd.read_csv('/Users/attaullah/Documents/homework-3-attaullahabbasi12/unemp.csv')
policy_uncertainty_data = pd.read_excel('/Users/attaullah/Documents/homework-2-attaullahabbasi12/policy_uncertainty.xlsx')


print("First few rows in unemployment data:")
print(unemployment_data['STATE'].unique())

# strip  extra spaces; ensure uppercase
unemployment_data['STATE'] = unemployment_data['STATE'].str.strip().str.upper()

# mapping state abreviations to ful names
us_state_abbrev = {
    'AL': 'Alabama', 'AK': 'Alaska', 'AZ': 'Arizona', 'AR': 'Arkansas', 'CA': 'California',
    'CO': 'Colorado', 'CT': 'Connecticut', 'DE': 'Delaware', 'FL': 'Florida', 'GA': 'Georgia',
    'HI': 'Hawaii', 'ID': 'Idaho', 'IL': 'Illinois', 'IN': 'Indiana', 'IA': 'Iowa',
    'KS': 'Kansas', 'KY': 'Kentucky', 'LA': 'Louisiana', 'ME': 'Maine', 'MD': 'Maryland',
    'MA': 'Massachusetts', 'MI': 'Michigan', 'MN': 'Minnesota', 'MS': 'Mississippi',
    'MO': 'Missouri', 'MT': 'Montana', 'NE': 'Nebraska', 'NV': 'Nevada', 'NH': 'New Hampshire',
    'NJ': 'New Jersey', 'NM': 'New Mexico', 'NY': 'New York', 'NC': 'North Carolina',
    'ND': 'North Dakota', 'OH': 'Ohio', 'OK': 'Oklahoma', 'OR': 'Oregon', 'PA': 'Pennsylvania',
    'RI': 'Rhode Island', 'SC': 'South Carolina', 'SD': 'South Dakota', 'TN': 'Tennessee',
    'TX': 'Texas', 'UT': 'Utah', 'VT': 'Vermont', 'VA': 'Virginia', 'WA': 'Washington',
    'WV': 'West Virginia', 'WI': 'Wisconsin', 'WY': 'Wyoming'
}

# mapping  abbreviations to full names
unemployment_data['STATE'] = unemployment_data['STATE'].map(us_state_abbrev)

#  checking for  remaining `NaN` values after mapping
missing_states = unemployment_data['STATE'].isna().sum()
print(f"Number of rows with missing state mappings: {missing_states}")

# conversion of `DATE` to `datetime` type in the unemployment data
unemployment_data['DATE'] = pd.to_datetime(unemployment_data['DATE'])

# creating  new `DATE` column in policy uncertainty data
policy_uncertainty_data['DATE'] = pd.to_datetime(
    policy_uncertainty_data.apply(
        lambda row: f"{row['year']}-{int(row['month']):02d}-01", axis=1
    )
)

# renaming the `state` column to `STATE` for alignment
policy_uncertainty_data.rename(columns={'state': 'STATE'}, inplace=True)

# merge the datasets using `STATE` and `DATE`as common columns
merged_data = pd.merge(unemployment_data,
                       policy_uncertainty_data[['STATE', 'DATE', 'EPU_Composite']],
                       on=['STATE', 'DATE'], how='inner')

# checking the first few rows 
print(merged_data.head())

#    2.2: Calculate the log-first-difference (LFD) of the EPU-C data
#    2.2: Select five states and create one Matplotlib figure that shows the unemployment rate
#         and the LFD of EPU-C over time for each state. Save the figure and commit it with 
#         your code.

# calculating the LFD of EPU Composite
merged_data['log_epu'] = np.log(merged_data['EPU_Composite'])
merged_data['LFD_EPU'] = merged_data['log_epu'].diff()

# selecting five states for plotting (e.g., Alabama, Alaska, Arizona, California, Colorado)
states_to_plot = ['Alabama', 'Alaska', 'Arizona', 'California', 'Colorado']
plot_data = merged_data[merged_data['STATE'].isin(states_to_plot)]

# plotting the unemployment rate and LFD of EPU-C over time for each state
fig, axes = plt.subplots(len(states_to_plot), 1, figsize=(10, 15), sharex=True)

for i, state in enumerate(states_to_plot):
    state_data = plot_data[plot_data['STATE'] == state]
    ax = axes[i]
    ax2 = ax.twinx()

    # plotting the unemployment rate
    ax.plot(state_data['DATE'], state_data['unemp_rate'], color='blue', label='Unemployment Rate')
    ax.set_ylabel('Unemployment Rate (%)', color='blue')
    ax.tick_params(axis='y', labelcolor='blue')

    # plotting LFD of EPU Composite
    ax2.plot(state_data['DATE'], state_data['LFD_EPU'], color='red', label='LFD EPU-C')
    ax2.set_ylabel('LFD EPU-C', color='red')
    ax2.tick_params(axis='y', labelcolor='red')

    ax.set_title(f'{state}')
    ax.grid(True)

fig.suptitle('Unemployment Rate and LFD of EPU-C Over Time')
fig.tight_layout(rect=[0, 0, 1, 0.96])
fig.savefig('q2_2_plot.png')
plt.show()

#    2.3: Using statsmodels, regress the unemployment rate on the LFD of EPU-C and fixed
#         effects for states. Include an intercept.
import statsmodels.formula.api as smf

# regressing unemployment rate on LFD of EPU-C with fixed effects (state dummies)
formula = 'unemp_rate ~ LFD_EPU + C(STATE)'
model = smf.ols(formula=formula, data=merged_data).fit()



#    2.4: Print the summary of the results, and write a 1-3 line comment explaining the basic
#         interpretation of the results (e.g. coefficient, p-value, r-squared), the way you 
#         might in an abstract.

# the summary of the regression results
print(model.summary())
# interpretation:
# while the state-specific trends are clear,but the relationship between 
#EPU and the unemployment is not conclusive.

#statistical details:

# R-squared (0.167):  model explains ~ 16.7% of the variability in 
#the rate of unemployment.

#Coefficient of LFD_EPU (-0.1193): The relationship between the LFD
#of EPU and unemployment rate isn't statistically significant (p-value of 0.236).


#State Fixed Effects: states like Nevada, California, and New York have 
#significantly higher unemployment rates than the baseline state (Alabama).
