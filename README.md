
# California Housing Prices

This project uses Python to connect to a SQLite database containing information about housing prices in California during the 1990s.

# Prerequisites
Before you begin, make sure you have the following requirements installed on your system:

* Python3
* SQLite

# Getting Started

Clone the repository to your local machine:

```
git clone git@github.com:your-username/California-Housing-Prices.git
```

Navigate to the project directory:

```
cd src 
```

Execute the python file:

```
python3 main.py
```

Choose from a variety of questions: 

```
Question 1: What is the median income for houses valued over 300k? 
   
Question 2: Are homes that are valued at 400k+ tend to be near water? 
   
Question 3: What is the median of the median income in California? 
    
Question 4: Does more rooms in a house make it more valuable? 
   
Question 5: Is the population of an area equal to the households? 
```

Additonal Information:

```
About this file
1. longitude: A measure of how far west a house is; a higher value is farther west
2. latitude: A measure of how far north a house is; a higher value is farther north
3. housingMedianAge: Median age of a house within a block; a lower number is a newer building
4. totalRooms: Total number of rooms within a block
5. totalBedrooms: Total number of bedrooms within a block
6. population: Total number of people residing within a block
7. households: Total number of households, a group of people residing within a home unit, for a block
8. medianIncome: Median income for households within a block of houses (measured in tens of thousands of US Dollars)
9. medianHouseValue: Median house value for households within a block (measured in US Dollars)
10. oceanProximity: Location of the house w.r.t ocean/sea
```

## Acknowledgements

 - [Dataset](https://www.kaggle.com/datasets/camnugent/california-housing-prices)

