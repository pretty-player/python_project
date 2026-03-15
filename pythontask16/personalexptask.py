import tkinter as tk
from tkinter import ttk, messagebox

class ExpenseTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")
        self.root.geometry("600x450")

        # Variables
        self.item_var = tk.StringVar()
        self.amount_var = tk.DoubleVar()
        self.total_expense = 0.0

        # --- UI Layout ---
        header = tk.Label(root, text="Expense Tracker", font=("Arial", 18, "bold"), pady=10)
        header.pack()

        # Input Frame
        input_frame = tk.Frame(root, pady=10)
        input_frame.pack()

        tk.Label(input_frame, text="Item:").grid(row=0, column=0, padx=5)
        tk.Entry(input_frame, textvariable=self.item_var).grid(row=0, column=1, padx=5)

        tk.Label(input_frame, text="Amount (₹):").grid(row=0, column=2, padx=5)
        tk.Entry(input_frame, textvariable=self.amount_var).grid(row=0, column=3, padx=5)

        # Buttons
        btn_frame = tk.Frame(root, pady=10)
        btn_frame.pack()

        tk.Button(btn_frame, text="Add Expense", command=self.add_expense, bg="#4CAF50", fg="white").pack(side=tk.LEFT, padx=10)
        tk.Button(btn_frame, text="Delete Selected", command=self.delete_expense, bg="#f44336", fg="white").pack(side=tk.LEFT, padx=10)

        # Expense List (Table)
        self.tree = ttk.Treeview(root, columns=("Item", "Amount"), show='headings', height=8)
        self.tree.heading("Item", text="Expense Item")
        self.tree.heading("Amount", text="Amount (₹)")
        self.tree.pack(pady=10, padx=20, fill=tk.BOTH)

        # Summary Label
        self.summary_label = tk.Label(root, text="Total Expenses: ₹0.00", font=("Arial", 12, "bold"), pady=10)
        self.summary_label.pack()

    def add_expense(self):
        item = self.item_var.get()
        amount = self.amount_var.get()

        if item == "" or amount <= 0:
            messagebox.showwarning("Input Error", "Please enter a valid item name and amount.")
            return

        # Add to table
        self.tree.insert("", tk.END, values=(item, f"{amount:.2f}"))
        
        # Update Total
        self.total_expense += amount
        self.update_summary()

        # Clear inputs
        self.item_var.set("")
        self.amount_var.set(0.0)

    def delete_expense(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("Selection Error", "Please select an item to delete.")
            return

        for item in selected_item:
            values = self.tree.item(item, 'values')
            self.total_expense -= float(values[1])
            self.tree.delete(item)
        
        self.update_summary()

    def update_summary(self):
        self.summary_label.config(text=f"Total Expenses: ₹{self.total_expense:.2f}")

if __name__ == "__main__":
    root = tk.Tk()
    app = ExpenseTracker(root)
    root.mainloop()