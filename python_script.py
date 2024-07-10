import sqlite3

def get_string():
    while True:
        search_string = input("Enter a search string: ")
        if search_string:
                return search_string
        else:
            print("Please enter a search string")

def main():
    # Connect to the assignment SQL database
    conn = sqlite3.connect('assignment.db')
    cursor = conn.cursor()
    
    search_string = get_string()

    #Case-insensitive search query
    query = "SELECT name, marks FROM students WHERE name LIKE ? COLLATE NOCASE"
    cursor.execute(query, (search_string + '%',)) #Assuming the values only matches that starts with the user string
    
    rows = cursor.fetchall()
    
    #Check for the no. of rows
    if rows:
        total_marks = 0
        for row in rows:
            name, marks = row
            print(f"Name: {name}, Marks: {marks}")
            total_marks += marks
        
        average_marks = total_marks / len(rows)
        print(f"Total Marks: {total_marks}")
        print(f"Average Marks: {average_marks:.2f}")
    else:
        print("No matching entries found.")

    conn.close()

if __name__ == "__main__":
    main()
