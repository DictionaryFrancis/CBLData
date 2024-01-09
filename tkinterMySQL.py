import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="@Tragom22",
    database="testandosql"
)

mycursor = connection.cursor()

choice = str(input("Would you like = DELETE, ADD or UPDATE? "))
if choice == "ADD":
    ############## Inserting Data  ############
    name = str(input("Add worked name: "))
    task = str(input("What task are you doing at the moment? "))

    sqlInserting = "INSERT INTO todolist (person_name,todo) VALUES (%s,%s)"
    valuesInsert = (name,task)
    mycursor.execute(sqlInserting,valuesInsert)
    connection.commit()
    print(mycursor.rowcount, "Record inserted")
    ############################################
elif choice == "DELETE":
    ############## Showing all data################
    mycursor.execute("SELECT * FROM todolist")

    myresult = mycursor.fetchall()

    print("TASK LIST:")
    for x in myresult:
      print(x)
    ################################################
    ############## Deleting Data  ############
    taskDelete = int(input("Task do you want to delete?: "))

    sqlDeleting = "DELETE FROM todolist WHERE ID = %s"
    valuesDelete = (taskDelete,)
    mycursor.execute(sqlDeleting,valuesDelete)
    connection.commit()
    print(mycursor.rowcount, f"Record inserted! You delete row {taskDelete}")
    ############################################
elif choice == "UPDATE":
    ############## Showing all data################
    mycursor.execute("SELECT * FROM todolist")

    myresult = mycursor.fetchall()

    print("TASK LIST:")
    for x in myresult:
      print(x)
    ################################################
    ############## Updating Data  ############
    taskUpdateID = int(input("Task do you want to update?: "))
    taskUpdate = str(input("Write again the task you are updating: "))

    sqlUpdate = "UPDATE todolist SET todo = %s WHERE ID = %s"
    valuesUpdate = (taskUpdate, taskUpdateID)
    mycursor.execute(sqlUpdate,valuesUpdate)
    connection.commit()
    print(mycursor.rowcount, f"Record inserted! You update row {taskUpdateID}")
    ############################################


############## Showing all data################
mycursor.execute("SELECT * FROM todolist")

myresult = mycursor.fetchall()

print("TASK LIST:")
for x in myresult:
  print(x)
################################################
