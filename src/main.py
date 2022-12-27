# making an interactive version of the project.
# goal, ask the reader 5 questions. Each question will be answered with a query.
# the user will not see the query instead he will see the answer. 

import sqlite3

def executeQuery(input, conn):
	""" Based on myDMS.py, executes queries from input"""

	myResult = conn.execute(input) # run the query

	queryInfo_list = myResult.fetchall()

	for i in queryInfo_list:
		print(f"\t[+] {i}")

	# end of executeQuery()

def main():
    """The code will be ran here."""
    db = "myDB.sqlite3" 
    conn = sqlite3.connect(db) # connecting database
    print("-----------")
    print("Welcome To Your DataBase !!!")
    print()
    print("[+] Question 1: What is the median income for houses valued over 300k? (enter 1 to view) ")
    print()
    print("[+] Question 2: Are homes that are valued at 400k+ tend to be near water? (enter 2 to view)")
    print()
    print("[+] Question 3: What is the median of the median income in California? (enter 3 to view)")
    print()
    print("[+] Question 4: Does more rooms in a house make it more valuable? (enter 4 to view)")
    print()
    print("[+] Question 5: Is the population of an area equal to the households? (enter 5 to view)")
    print()
    input1 = input("What question do you want to look at first? enter 1 - 5 here ")

    # making if statements for inputs 1 - 5 here: 

    if input1 == "1": 
        print("WELCOME TO QUESTION 1: ")
        print()
        print("Here is the data gathered from the database: ")
        print()
        
        myQuery_str = f"select avg(median_income) from data where median_house_value > 300000;"

        res1 = executeQuery(myQuery_str, conn)


    if input1 == "2": 
        print("WELCOME TO QUESTION 2: ")
        
        print("Here is the data gathered from the database: ")
        print()
        
        myQuery_str = f"select ocean_proximity, max(median_house_value + 0) from data;"

        res2 = executeQuery(myQuery_str, conn)

    if input1 == "3": 
        print("WELCOME TO QUESTION 3: ")
    
        print("Here is the data gathered from the database: ")
        print()
        
        myQuery_str = f"select AVG(median_income) from data;"

        res3 = executeQuery(myQuery_str, conn)
    
    if input1 == "4": 
        print("WELCOME TO QUESTION 4: ")
        print("Here is the data gathered from the database: ")
        print()
        
        myQuery_str = f"select AVG(total_rooms), AVG(median_house_value) from data;"

        res4 = executeQuery(myQuery_str, conn)

    if input1 == "5": 
        print("WELCOME TO QUESTION 5: ")
        print("Here is the data gathered from the database: ")
        print()
        
        myQuery_str = f"SELECT population, households from data where population = households;"

        res5 = executeQuery(myQuery_str, conn)

if __name__ == '__main__':
    main()
