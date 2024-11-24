# with open('weather_data.csv')as data_file:
#     data=data_file.readlines()
#     print(data)


#___________________________________________________________

# import csv

# with open('weather_data.csv')as data_file:
   
#     data=csv.reader(data_file)
#     temp=[]
#     for row in data:
#         if row[1]!='temp':
#             temp.append(int(row[1]))
#     print(temp)
# #_______________________________________________________________________________


# import pandas
# data=pandas.read_csv('weather_data.csv')
# print(type(data))
# print(data['temp'])
#_____________________________________________________________________

# import pandas
# data=pandas.read_csv('weather_data.csv')
# data_dict=data.to_dict()
# print(data_dict)
#_______________________________________________

# import pandas
# data=pandas.read_csv('weather_data.csv')
# data_dict=data.to_dict()
# temp_list=data['temp'].to_list()
# print(temp_list)
#_____________________________________-

# import pandas as pd

# # Read the CSV file
# data = pd.read_csv('weather_data.csv')

# # Initialize variables
# initial_temp = 0
# total_temp = 0

# # Convert DataFrame to list of lists
# data_list = data.values.tolist()

# # Loop through the rows of the data
# for i in range(len(data_list)):
#     # Assuming temperatures are in the second column (index 1)
#     initial_temp += data_list[i][1]
#     total_temp += data_list[i][1]

# # You can print or return the results
# print(f"Initial Temperature: {initial_temp}")
# print(f"Total Temperature: {total_temp}")
#___________________________________________________________-

# import pandas as pd

# # Read the CSV file
# data = pd.read_csv('weather_data.csv')

# # Initialize variables
# total_temp = 0
# num_entries = 0

# # Convert DataFrame to list of lists
# data_list = data.values.tolist()

# # Loop through the rows of the data
# for row in data_list:
#     # Assuming the temperature is in the second column (index 1)
#     total_temp += row[1]  # Sum the temperature values
#     num_entries += 1      # Count the number of temperature entries

# # Calculate the average temperature
# if num_entries > 0:
#     average_temp = total_temp / num_entries
#     print(f"Average Temperature: {average_temp}")
# else:
#     print("No temperature data available.")
#_________________________________-

# import pandas as pd

# # Read the CSV file
# data = pd.read_csv('weather_data.csv')

# # Convert the DataFrame to a dictionary (optional, for inspection)
# data_dict = data.to_dict()
# print(data_dict)

# # Extract the 'temp' column into a list
# temp_list = data['temp'].to_list()
# print("Number of temperature entries:", len(temp_list))

# # Calculate the average temperature
# average_temp = sum(temp_list) / len(temp_list)  # Correct way to calculate the average
# print("Average Temperature:", average_temp)
#_________________________________________________________--

# import pandas as pd

# # Load the data from CSV
# data = pd.read_csv('weather_data.csv')

# # Convert the DataFrame to a dictionary (optional, for inspection)
# data_dict = data.to_dict()
# print(data_dict)

# # Convert the 'temp' column to a list
# temp_list = data['temp'].to_list()

# # Find and print the maximum temperature value in the list
# print( max(temp_list))
# print(min(temp_list))
# print(data[data.temp==data.temp.max()])#در رو راه میره

#_________________________________________________________________________________________________

# data[x]#دسترسی ب ستون
# data[data[x]]دسترسی افقی


#3-----------------------------------------------------------
import pandas as pd

# Load the data from CSV
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

# Count the number of squirrels with gray fur color
gray_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_count = len(data[data['Primary Fur Color'] == 'Red'])

# Print the count
print(red_count)
