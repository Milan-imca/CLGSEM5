import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Function to ask what to update (name or department)
def ask_what_to_update():
    update_choice.set(None)  # Clear previous selection
    label_update_option.grid(row=3, column=0, pady=10)
    radio_name.grid(row=3, column=1)
    radio_department.grid(row=3, column=2)
    button_confirm_update.grid(row=4, column=1, pady=10)

# Function to show the field to enter the updated value based on selection
def on_confirm_update():
    selected = update_choice.get()
    if selected:
        label_updated_value.grid(row=5, column=0, pady=10)
        entry_updated_value.grid(row=5, column=1)
        button_apply_update.grid(row=6, column=1, pady=10)
    else:
        messagebox.showwarning("Warning", "Please select what to update (Name/Department).")

# Function to update the value in the database
def apply_update():
    emp_id = entry_id.get()
    updated_value = entry_updated_value.get()
    field_to_update = update_choice.get()

    if field_to_update == "name":
        update_query = "UPDATE emp_details SET name = %s WHERE id = %s"
    elif field_to_update == "department":
        update_query = "UPDATE emp_details SET department = %s WHERE id = %s"
    else:
        messagebox.showwarning("Warning", "Please select a valid option to update.")
        return

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="123456",
            database="milan"
        )
        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute(update_query, (updated_value, emp_id))
            connection.commit()
            messagebox.showinfo("Success", f"Employee {field_to_update} updated successfully.")
    except mysql.connector.Error as error:
        messagebox.showerror("Error", f"Failed to update data: {error}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Function to clear input fields
def clear_fields():
    entry_id.delete(0, tk.END)
    entry_updated_value.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Employee Management")
root.geometry("400x300")

# Labels and Entry fields for Employee ID and update process
label_id = tk.Label(root, text="Employee ID:")
label_id.grid(row=0, column=0, pady=10)
entry_id = tk.Entry(root)
entry_id.grid(row=0, column=1, pady=10)

# Button to initiate the update process
button_update = tk.Button(root, text="Update", command=ask_what_to_update)
button_update.grid(row=1, column=1, pady=10)

# Label and Radio Buttons to select what to update (Name or Department)
label_update_option = tk.Label(root, text="What would you like to update?")
update_choice = tk.StringVar()

radio_name = tk.Radiobutton(root, text="Name", variable=update_choice, value="name")
radio_department = tk.Radiobutton(root, text="Department", variable=update_choice, value="department")

# Confirm button to proceed after selecting the field to update
button_confirm_update = tk.Button(root, text="Confirm", command=on_confirm_update)

# Label and Entry to input the new value to be updated
label_updated_value = tk.Label(root, text="Enter new value:")
entry_updated_value = tk.Entry(root)

# Apply the update
button_apply_update = tk.Button(root, text="Apply Update", command=apply_update)

# Clear button
button_clear = tk.Button(root, text="Clear", command=clear_fields)
button_clear.grid(row=7, column=1, pady=10)

# Start the Tkinter event loop
root.mainloop()
