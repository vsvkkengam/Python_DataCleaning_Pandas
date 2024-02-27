# Python_DataCleaning_Pandas
The Python data cleaning project using the pandas library. It reads a CSV file containing cricket player statistics, performs various cleaning and preprocessing tasks, and then analyzes the data.

# Steps Performed 
__Importing Libraries and Data:__ The script starts by importing the pandas library and reading a CSV file containing cricket player statistics.

__Renaming Columns:__ It renames multiple columns for better clarity using the rename() function.

__Checking for Null Values:__ The script checks for null values in the dataset using the isnull().any() function and then specifically inspects the 'Balls_Faced' and 'Strike_Rate' columns for null values.

__Handling Null Values:__ Null values in the 'Balls_Faced' and 'Strike_Rate' columns are filled with appropriate values.

__Handling Duplicates:__ Duplicate records are identified and removed from the dataset using the duplicated() and drop_duplicates() functions.

__Data Transformation:__ The 'Span' column is split into 'Start_Year' and 'End_Year' columns. Additionally, the 'Player' column is split to extract the country and player name separately. Plus, some columns are cleaned by removing characters like '+', '*', and ')'.

__Changing Data Types:__ Data types of certain columns such as 'Highest_Score', 'Start_Year', 'End_Year', 'Strike_Rate', and 'Career_Length' are converted to appropriate types using astype().

__Calculating Career Length:__ The length of each player's career is calculated by subtracting the start year from the end year.

__Analyzing Data:__ Various analyses are performed on the cleaned dataset, including calculating the average career length, average batting strike rate of players with career lengths greater than 10 years, counting players before 1960, finding the maximum highest innings scored by a country, and calculating the average number of 100s, 50s, and ducks by country.

# Conclusion:
The script concludes after performing all the cleaning and analysis tasks.
