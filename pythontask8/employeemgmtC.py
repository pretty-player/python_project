class Employee:
    def __init__(self, name, salary):
        """Initializes common employee attributes."""
        self.name = name
        self.salary = salary

    def calculate_total_salary(self):
        """Base method for salary calculation."""
        return self.salary

    def display_details(self):
        print(f"Employee: {self.name}")
        print(f"Base Salary: ₹{self.salary}")

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        """Uses super() to inherit name and salary, then adds bonus."""
        super().__init__(name, salary)
        self.bonus = bonus

    def calculate_total_salary(self):
        """Overrides the parent method to include the bonus."""
        total = self.salary + self.bonus
        return total

    def display_details(self):
        """Extends parent display logic."""
        super().display_details()
        print(f"Management Bonus: ₹{self.bonus}")
        print(f"Total Compensation: ₹{self.calculate_total_salary()}")

# --- Testing the Inheritance ---

# Regular Employee
emp1 = Employee("Silambu P", 50000)
print("--- Standard Employee Record ---")
emp1.display_details()

print("\n" + "-"*30 + "\n")

# Manager (Subclass)
mgr1 = Manager("Silambarasan P", 85000, 15000)
print("--- Managerial Record ---")
mgr1.display_details()