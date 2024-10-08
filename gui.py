import tkinter as tk
from tkinter import messagebox
import data_processing
import google_sheets_api


def submit_data():
    try:
        # Collect data from entry fields
        data = data_processing.collect_data(
            builders_entry.get(),
            community_entry.get(),
            lot_entry.get(),
            name_entry.get(),
            status_entry.get(),
        )

        # Process the collected data
        processed_data = data_processing.process_data(data)

        # Append the processed data to Google Sheets
        google_sheets_api.append_data_to_sheet(processed_data)

        # Clear the entry fields after submission
        clear_fields()

        # Provide feedback to the user
        messagebox.showinfo("Success", "Data submitted successfully!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


def clear_fields():
    builders_entry.delete(0, tk.END)
    community_entry.delete(0, tk.END)
    lot_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    status_entry.delete(0, tk.END)


# Initialize the main window
root = tk.Tk()
root.title("Data Entry App")
root.geometry("250x200")

# Create labels and entries
builders_label = tk.Label(root, text="Builders:")
builders_entry = tk.Entry(root)

community_label = tk.Label(root, text="Community:")
community_entry = tk.Entry(root)

lot_label = tk.Label(root, text="Lot:")
lot_entry = tk.Entry(root)

name_label = tk.Label(root, text="Name:")
name_entry = tk.Entry(root)

status_label = tk.Label(root, text="Status:")
status_entry = tk.Entry(root)

# Grid layout
builders_label.grid(row=0, column=0)
builders_entry.grid(row=0, column=1)

community_label.grid(row=1, column=0)
community_entry.grid(row=1, column=1)

lot_label.grid(row=2, column=0)
lot_entry.grid(row=2, column=1)

name_label.grid(row=3, column=0)
name_entry.grid(row=3, column=1)

status_label.grid(row=4, column=0)
status_entry.grid(row=4, column=1)

# Create submit button
submit_button = tk.Button(root, text="Submit", command=submit_data)
submit_button.grid(row=5, columnspan=2, pady=10)

# Run the main loop
root.mainloop()
