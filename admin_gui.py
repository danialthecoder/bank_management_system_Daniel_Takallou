import tkinter as tk 
from tkinter import messagebox, ttk
from core import AdminPanel


class AdminGUI:

    def __init__(self,bank_system):
        self.bank= AdminPanel()
        self.root=tk.TK()
        self.root.title('Bank Management System')
        self.root.geometry('800x600')
        self.root.resizable(False,False)
        self.show_login_window()
        self.root.mainloop()

    def clear(self): 
        for widget in self.root.winfo_children():
         widget.destroy() 
    def show_login_window(self):
        self.clear()
        tk.Label(self.root, text="Admin Login", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Label(self.root, text="Username:").pack()
        self.username_entry = tk.Entry(self.root)
        self.username_entry.pack()
        tk.Label(self.root, text="Password:").pack()
        self.password_entry = tk.Entry(self.root, show="*")
        self.password_entry.pack()
        tk.Button(self.root, text="Login", bg="blue", fg="white", command=self.login).pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # For demo, hardcoded admin credentials
        if username == "admin" and password == "1234":
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials")


    def show_dashboard(self):

        self.clear()
        tk.Label(self.root, text="Admin Dashboard", font=("Arial", 18, "bold")).pack(pady=20)
        tk.Button(self.root, text="Create Customer", width=25, command=self.gui_create_customer).pack(pady=5)
        tk.Button(self.root, text="Create Account", width=25, command=self.gui_create_account).pack(pady=5)
        tk.Button(self.root, text="View Accounts", width=25, command=self.gui_view_accounts).pack(pady=5)
        tk.Button(self.root, text="View Transactions", width=25, command=self.gui_view_transactions).pack(pady=5)
        tk.Button(self.root, text="Delete Account", width=25, command=self.gui_delete_account).pack(pady=5)
        tk.Button(self.root, text="Logout", width=25, bg="red", fg="white", command=self.show_login_window).pack(pady=20)


    
    def gui_create_customer(self):
        self.clear()
        tk.Label(self.root, text="Create Customer", font=("Arial", 16, "bold")).pack(pady=10)
        form = tk.Frame(self.root); form.pack(pady=10)
        labels = ["Name", "Email", "Age", "Phone", "Address"]
        self.cust_entries = {}
        for i, label in enumerate(labels):
        tk.Label(form, text=label).grid(row=i, column=0, sticky="e", padx=5, pady=5)
        entry = tk.Entry(form, width=40)
        entry.grid(row=i, column=1, padx=5, pady=5)
        self.cust_entries[label.lower()] = entry

    def submit():
        try:
             name = self.cust_entries["name"].get()
             email = self.cust_entries["email"].get()
             age = int(self.cust_entries["age"].get())
             phone = self.cust_entries["phone"].get()
             address = self.cust_entries["address"].get()
             self.bank.create_customer(name, email, age, phone, address)
             messagebox.showinfo("Success", "Customer created")
             self.show_dashboard()
            except Exception as e:
                messagebox.showerror("Error", str(e))
                
             tk.Button(self.root, text="Submit", command=submit).pack(pady=10)
             tk.Button(self.root, text="Back", command=self.show_dashboard).pack()
             
    def gui_view_accounts(self):
        self.clear()
        tk.Label(self.root, text="View Accounts", font=("Arial", 16, "bold")).pack(pady=10)
        frame = tk.Frame(self.root); frame.pack(fill="both", expand=True, padx=10, pady=10)
        columns = ("id", "customer_id", "type", "balance", "card_number")
        tree = ttk.Treeview(frame, columns=columns, show="headings") for col in columns:
        for col in columns:
            tree.heading(col, text=col); tree.column(col, width=150)
        tree.pack(fill="both", expand=True)
        try:
            accounts = self.bank.session.query(Account).all()
            for acc in accounts:
                tree.insert("", "end", values=(acc.id, acc.customer_id, acc.type, acc.balance, acc.card_number)) except Exception as e:
                    except Exception as e:
                        messagebox.showerror("Error", str(e))
                    tk.Button(self.root, text="Back", command=self.show_dashboard).pack(pady=10)
    def gui_view_transactions(self):
        self.clear()
        tk.Label(self.root, text="View Transactions", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self.root, text="Account ID:").pack()
        acc_id_entry = tk.Entry(self.root); acc_id_entry.pack()
        frame = tk.Frame(self.root); frame.pack(fill="both", expand=True, padx=10, pady=10)
        columns = ("id", "account_id", "type", "amount", "timestamp")
        tree = ttk.Treeview(frame, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col); tree.column(col, width=150)
        tree.pack(fill="both", expand=True) 

        def load():
            try:
                account_id= int(acc_id_entry.get())
                txns = self.bank.show_transaction(account_id)
                for i in tree.get_children(): tree.delete(i)
                for t in txns:
                    tree.insert("", "end", values=(t.id, t.account_id, t.type, t.amount, t.timestamp))
            except Exception as e:
                messagebox.showerror("Error", str(e))

       tk.Button(self.root, text="Load", command=load).pack(pady=10)
       tk.Button(self.root, text="Back", command=self.show_dashboard).pack()
    def gui_delete_account(self):
        self.clear()
        tk.Label(self.root, text="Delete Account", font=("Arial", 16, "bold")).pack(pady=10)
        tk.Label(self.root, text="Account ID:").pack()
        acc_id_entry = tk.Entry(self.root); acc_id_entry.pack()

        def delete():
            try:
                account_id= int(acc_id_entry.get())
                acc= self.bank.session.get(Account, account_id)
                if not acc:
                    raise Exception("Account not found")
                    self.bank.session.delete(acc)
                    self.bank.session.commit()
                    messagebox.showinfo("Success", "Account deleted")
                    self.show_dashboard()
                except Exception as e:
                    messagebox.showerror("Error", str(e))

           tk.Button(self.root, text="Delete", command=delete).pack(pady=10)
           tk.Button(self.root, text="Back", command=self.show_dashboard).pack()

if __name__ == "__main__":
    AdminGUI()

                    
