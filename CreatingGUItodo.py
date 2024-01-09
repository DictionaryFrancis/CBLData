from customtkinter import CTk, CTkLabel, CTkComboBox, CTkButton
import mysql.connector


############## Calling MYSQL ####################
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="@Tragom22",
    database="testandosql"
)

mycursor = connection.cursor()
############################################


app = CTk()
app.geometry("500x400")
app.title("Invoice Maker!")


############ FUNCTIONS ##################
def handle_status():
    status = f"{options.get()}"
    print(f"You select {status}")


    if status == "ADD":
        ############## Inserting Data  ############
        name = str(input("Add worked name: "))
        task = str(input("What task are you doing at the moment? "))

        sqlInserting = "INSERT INTO todolist (person_name,todo) VALUES (%s,%s)"
        valuesInsert = (name, task)
        mycursor.execute(sqlInserting, valuesInsert)
        connection.commit()
        print(mycursor.rowcount, "Record inserted")
        ############################################
    elif status == "DELETE":
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
        mycursor.execute(sqlDeleting, valuesDelete)
        connection.commit()
        print(mycursor.rowcount, f"Record inserted! You delete row {taskDelete}")
        ############################################
    elif status == "UPDATE":
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
        mycursor.execute(sqlUpdate, valuesUpdate)
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


##########################################

############## LAYOUT INSIDE THE GUI ##########################
label_test = CTkLabel(master=app, text="Select the Company")
label_test.place(relx=0.5, rely=0.15, anchor="center")
options = CTkComboBox(master=app, values=["ADD", "DELETE", "UPDATE"])
options.place(relx=0.5, rely=0.24, anchor="center")

btn_option = CTkButton(master=app, text="Confirm Status", corner_radius=15,
                       command=handle_status
                       )
btn_option.place(relx=0.5, rely=0.40, anchor="center")
#################################################################

# APP WORK
app.mainloop()
