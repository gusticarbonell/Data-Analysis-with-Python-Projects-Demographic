import pandas as pd
import numpy as np

# read the dataset into a pandas DataFrame
df = pd.read_csv('dataset.csv')

# 1 How many people of each race are represented in this dataset? This should be a Pandas series with race names as the index labels. (race column)
race_counts = df['race'].value_counts()
print(race_counts)

# 2 What is the average age of men?
male_df = df[df['sex'] == 'Male']
average_age_male = male_df['age'].mean()
print("The average age of men is:", average_age_male)

# 3 What is the percentage of people who have a Bachelor's degree?
bachelors_count = df[df['education'] == 'Bachelors']['education'].count()
total_count = df['education'].count()
percentage = (bachelors_count / total_count) * 100
print(
    "Percentage of people with a Bachelor's degree: {:.2f}%".format(percentage))

# 4 What percentage of people with advanced education (Bachelors, Masters, or Doctorate) make more than 50K?
df['education_level'] = np.where(df['education'].isin(
    ['Bachelors', 'Masters', 'Doctorate']), 'Advanced', 'Not Advanced')
advanced_edu = df[df['education_level'] == 'Advanced']
advanced_edu_more_50k = advanced_edu[advanced_edu['salary'] == '>50K']
perc_advanced_edu_more_50k = (
    len(advanced_edu_more_50k) / len(advanced_edu)) * 100
print("Percentage of people with advanced education who make more than 50K: {:.2f}%".format(
    perc_advanced_edu_more_50k))

# 5 What percentage of people without advanced education make more than 50K?
df['advanced_edu'] = df['education'].isin(
    ['Bachelors', 'Masters', 'Doctorate'])
no_adv_edu = df[~df['advanced_edu']]
no_adv_edu_gt50K = no_adv_edu[no_adv_edu['salary'] == '>50K']
pct_no_adv_edu_gt50K = (len(no_adv_edu_gt50K) / len(no_adv_edu)) * 100
print("The percentage of people without advanced education who make more than 50K is {:.2f}%".format(
    pct_no_adv_edu_gt50K))

# 6 What is the minimum number of hours a person works per week?
min_hours = df['hours-per-week'].min()
print("The minimum number of hours a person works per week is:", min_hours)

# 7 What percentage of the people who work the minimum number of hours per week have a salary of more than 50K?
min_hours_df = df[df['hours-per-week'] == df['hours-per-week'].min()]
perc_min_hours_gt50K = (
    len(min_hours_df[min_hours_df['salary'] == '>50K']) / len(min_hours_df)) * 100
print("The percentage of people who work the minimum number of hours per week and have a salary of more than 50K is: {:.2f}%".format(
    perc_min_hours_gt50K))

# 8 What country has the highest percentage of people that earn >50K and what is that percentage?
high_income = df[df['salary'] == '>50K']
totals = high_income.groupby('native-country')['age'].count()
percentages = (high_income.groupby('native-country')
               ['age'].count() / df.groupby('native-country')['age'].count()) * 100
sorted_data = percentages.sort


# 9 Identify the most popular occupation for those who earn >50K in India.

# filter rows where native-country is India and salary is >50K
india_high_salary = df[(df['native-country'] == 'India')
                       & (df['salary'] == '>50K')]

# group the resulting DataFrame by occupation and count the number of occurrences of each occupation
occupation_counts = india_high_salary.groupby(
    'occupation')['occupation'].count()

# sort the values in descending order and take the first value to get the most popular occupation
most_popular_occupation = occupation_counts.sort_values(
    ascending=False).index[0]

print("The most popular occupation for those who earn >50K in India is:",
      most_popular_occupation)
