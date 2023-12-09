import csv
import tkinter as tk

# Read in the data from the CSV file
data = []
with open('clientaccounts.csv', 'r') as f:
  reader = csv.reader(f)
  for row in reader:
    data.append(row)

# Create the main window
root = tk.Tk()
root.title("ACCOUNT DETAILS")
# Create the labels for each column
for i, col in enumerate(data[0]):
  label = tk.Label(root, text=col, width=15, borderwidth=1, relief="solid")
  if (i != 3):
    label.grid(row=0, column=i)

# Create the labels for each row
for i, row in enumerate(data[1:]):
  for j, val in enumerate(row):
    label = tk.Label(root, text=val, width=15, borderwidth=1, relief="solid")
    if (j != 3):
      label.grid(row=i+1, column=j)

# Run the main loop
root.mainloop()