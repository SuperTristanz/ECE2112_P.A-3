
# we import the pandas library
import pandas as pd

# We load the csv file 
df = pd.read_csv('cars.csv.crdownload')

# We locate the first 5 rows with odd numbered columns
problem_a = df.loc[0:5,1::2]

# Printing the First 5 rows with odd numbered columns
print(problem_a)

# displaying the row that contains the model of 'Mazda Rx4'
problem_b = df.loc[df['Model']== 'Mazda RX4']

#printing the row 'Mazda RX4'
print(problem_b)

# Display the cyclinders ('cly') does the car model 'Camaro Z28' have
problem_c = df.loc[df['Model] == 'Camaro Z28', ['Model', 'cyl']]

#Print the Answer on how many cylinders does the car Camaro z28 has
print(problem_c)


#Displaying how many cylinder and their gears that 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic' has
problem_d = df.loc['Model'].isin(['Mazda RX4 Wag', 'Ford Panterera L', 'Honda Civic']), ['Character','cyl','gear']

#Printing the Problem d
print(problem_d)

