# ECE2112_P.A #3

### Pandas (Phyton Data Analysis)
### What is Pandas? 
#### Pandas is a Python library used for working with data sets. It has functions for analyzing, cleaning, exploring, and manipulating data. The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008.

### Objective
#### - To practice Pandas Library
#### - To Enhance oneself to the functions of Pandas
#### - To identify the codes and functions incorporated in the Pandas library 
#### - To be able to apply and use the different codes and functions in creating a Python program using a Pandas library

## Problem 1
![image](https://github.com/user-attachments/assets/0081ca23-6743-4baf-b990-dfca09d42990)

### Problem Insights:

 ##### •	You are required to load data from a .csv file using pandas.
#####  •	The .csv file likely contains some form of data related to cars.
#####  •	After loading the data, you need to display the first five rows using DataFrame.head() and the last five rows using DataFrame.tail().

#### Code to Solve the Problem
##### ![image](https://github.com/user-attachments/assets/3363cf68-23bf-49a4-a06f-f702fd56686b)
##### ![image](https://github.com/user-attachments/assets/64cf0f73-2ca3-4e25-984e-4b9f1ae438ca)
##### ![image](https://github.com/user-attachments/assets/9bc01d00-8fd3-4188-ad6f-351a55a3ca31)

### Explanation:
##### 1.	pd.read_csv('cars.csv'): This function reads the CSV file into a pandas DataFrame named cars.
##### 2.	cars.head(): Displays the first five rows of the DataFrame. 
##### 3.	cars.tail(): Displays the last five rows of the DataFrame.
##### 4. we create a python file, file = open('Angostora_Pandas_Problem1.py','w') and we use the function .write() to write the code into the file, then we use .close() function to close the file


### Outputs
##### Reading the File
![image](https://github.com/user-attachments/assets/f3b3c673-5e7e-4991-b39d-2f44b884e44e)
##### Using the Head Function
![image](https://github.com/user-attachments/assets/c3731b02-6360-48f8-9171-dc355d893d17)

##### Using the Tail Function
![image](https://github.com/user-attachments/assets/d4fd361a-e4a4-4479-9535-cb62c574f482)




## Problem 2
![image](https://github.com/user-attachments/assets/e8f3456e-27d0-4d43-b445-389a0ee8fec8)

### Problem Insights:
##### 1.	DataFrame Operations: The tasks involve extracting specific parts of a DataFrame using various indexing techniques (e.g., selecting specific columns or rows based on certain conditions).
##### 2.	Tasks Overview:
##### •	(a) Display the first five rows with odd-numbered columns (1, 3, 5, 7, …)
##### •	(b) Extract the row containing the car model 'Mazda RX4'
##### •	(c) Find out how many cylinders ('cyl') the 'Camaro Z28' has.
##### •	(d) Extract both the number of cylinders ('cyl') and gear type ('gear') for the models 'Mazda RX4 Wag', 'Ford Pantera L', and 'Honda Civic'.


### Code to Solve the Problem
##### ![image](https://github.com/user-attachments/assets/d5426474-f0f5-4eb0-a240-38ac0fdf8d66)
##### ![image](https://github.com/user-attachments/assets/2995be8c-4d74-4a05-a971-e31e345aed55)
##### ![image](https://github.com/user-attachments/assets/052cf202-13e1-4b7c-91c3-8db376983a97)
##### ![image](https://github.com/user-attachments/assets/91bb8617-756e-47ae-a3c8-790083657e0e)
##### ![image](https://github.com/user-attachments/assets/b2ed9445-c0d4-43c3-8d8b-f22e8266abd1)
##### ![image](https://github.com/user-attachments/assets/d33ba74a-acab-41d5-9870-42a9b130bf87)

### Explanation
##### 1.	Odd-Numbered Columns (a): •	Pandas indexing starts at 0, so “odd-numbered columns” in a zero-based index will refer to columns with indices 0, 2, 4, etc. However, the problem might refer to indices starting at 1, so clarity is needed about whether to use 1-based or 0-based indexing. 
##### 2.	Extracting Rows Based on Model (b, c, d): •	The problem assumes that the 'Model' column is accessible and correctly labeled. If not, adjustments will be needed for proper indexing.	In part (c) and (d), extracting specific rows based on car models assumes the car models are spelled exactly as written, which can cause issues if there are slight variations or extra spaces in the data. 
##### 3.	Indexing for Specific Columns and Values (d)	The instructions imply that column labels such as 'cyl' and 'gear' must be accessed. This assumes these labels exist and are correctly spelled.
### Output of the Code
##### ![image](https://github.com/user-attachments/assets/0cc410af-b2b7-4818-b821-a111fb2f9ffb)
##### ![image](https://github.com/user-attachments/assets/5d076d37-c323-4dfc-ae72-466d1a040d18)
##### ![image](https://github.com/user-attachments/assets/669685b5-42f1-4dc0-868f-df80905bb521)


##### Author: Tristan Zeth V. Angostora
##### P.A provided by: Engr. Ma. Madecheen S. Pangaliman, M.Sc.
##### • Faculty member at UST-ECE Department
##### • PhD EEE with specialization in AI and
##### Robotics student at UP-Diliman












