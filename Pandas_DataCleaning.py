# %%
#import pandas and import the csv file

import pandas as pd
file = pd.read_csv("D:\Desktop\VS\Datasets\File for Pandas.csv")
file

# %%
#Rename multiple columns in a list

file = file.rename(columns = {'NO':'Not_Outs','Mat':'No_of_Mathces','Inns':'No_of_Ings','HS':'Highest_Score',
                              'Ave':'AVG', 'BF':'Balls_Faced', 'SR':'Strike_Rate'})
file.head()

# %%
file.columns

# %%
file.describe

# %%
#Check Null Values
file.isnull().any()

# %%
file[file['Balls_Faced'].isna()==1]

# %%
file['Balls_Faced'] = file['Balls_Faced'].fillna(0)


#checking a player details for null values
file[file['Player'] == 'ED Weekes (WI)']

# %%
file[file['Strike_Rate'].isna()==1]

# %%
file['Strike_Rate'] = file['Strike_Rate'].fillna(0)

#checking a player details for null values
file[file['Player'] == 'CL Walcott (WI)']

# %%
#Drop duplicates
file.duplicated()

# %%
file[file['Player'].duplicated()==1]

# %%
file[file['Player'].isin(['GA Headley (WI)', 'JB Hobbs (ENG)', 'CA Davis (WI)','SR Tendulkar (IND)','SR Waugh (AUS)','Inzamam-ul-Haq (ICC/PAK)','V Sehwag (ICC/IND)'])]

# %%
file = file.drop_duplicates()

# %%
file

# %%
file.duplicated()

# %%
#Splittin up span into start and end years

# %%
file['Span'].str.split(pat = '-', expand=True)

# %%
file['Start_Year'] = file['Span'].str.split(pat = '-').str[0]

# %%
file['End_Year'] = file['Span'].str.split(pat = '-').str[1]

# %%
file

# %%
#seperating country from player name
file['Player'].str.split(pat='(')

# %%
file['Country'] = file['Player'].str.split(pat='(').str[1]

# %%
file

# %%
file['Country']

# %%
file['Country'] = file['Country'].str.rstrip(')')



# %%
file['Player'] = file['Player'].str.split(pat='(').str[0]

# %%
file['Balls_Faced'] = file['Balls_Faced'].str.rstrip('+')
#removing + sign after balls faced column 

# %%
file['Highest_Score'] = file['Highest_Score'].str.rstrip('*')

# %%
file.head()

# %%
#Change data types

# %%
file.dtypes

# %%
file['Highest_Score'] = file['Highest_Score'].astype(int)

# %%
file['Player'] = file['Player'].astype(str)



# %%
file = file.astype({
    'Player': str,
 
    'Start_Year': int,
    'Strike_Rate': float,
    'End_Year': int,
 
})

# %%
file = file.astype({
    'Start_Year' : int,
    'End_Year' : int
})

# %%
file.dtypes

# %%
#calculating career length
file['Career_Length'] = file['End_Year']-file['Start_Year']
file

# %%
#Average Career Length
file['Career_Length'].mean()

# %%
#Average batting strike rate of a batsman who career length is greater than 10
file[file['Strike_Rate'] > 10]['Strike_Rate']

# %%
file[file['Strike_Rate'] > 10]['Strike_Rate'].mean()

# %%
#number of players before 1960
file[file['Start_Year'] < 1960]

# %%
file[file['Start_Year'] < 1960]['Player'].count()


# %%
#max highest innings scored by a country
file.groupby('Country')['Highest_Score'].max().to_frame('High_inngs_count').reset_index().sort_values('High_inngs_count', ascending=False)

# %%
#100s, 50s, ducks average by country
file.groupby('Country')[['100','50', '0']].mean()

# %%



