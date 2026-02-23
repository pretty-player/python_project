# Function 1: Input Data (Returns a dictionary)
def get_employee_data():
    name = input("\nEnter Employee Name: ")
    basic_salary = float(input(f"Enter Basic Salary for {name}: "))
    return {"name": name, "basic": basic_salary}

# Function 2: Calculate Gross Salary (Takes parameters, returns a value)
def calculate_gross(basic):
    # Defining allowances as percentages of basic salary
    hra = basic * 0.20  # House Rent Allowance (20%)
    da = basic * 0.15   # Dearness Allowance (15%)
    gross = basic + hra + da
    return gross, hra, da

# Function 3: Display Salary Slip (Takes multiple arguments, no return)
def display_salary_slip(name, basic, hra, da, gross):
    print("\n" + "="*30)
    print(f"       SALARY SLIP")
    print("="*30)
    print(f"Employee Name : {name}")
    print(f"Basic Salary  : ₹{basic:,.2f}")
    print(f"HRA (20%)     : ₹{hra:,.2f}")
    print(f"DA (15%)      : ₹{da:,.2f}")
    print("-" * 30)
    print(f"GROSS SALARY  : ₹{gross:,.2f}")
    print("="*30)

# Main Function to orchestrate the flow
def main():
    print("--- Employee Management System ---")
    try:
        count = int(input("How many employees do you want to process? "))
        
        for i in range(count):
            # Step 1: Get Data
            emp = get_employee_data()
            
            # Step 2: Perform Calculations
            gross_total, hra_val, da_val = calculate_gross(emp['basic'])
            
            # Step 3: Output Results
            display_salary_slip(emp['name'], emp['basic'], hra_val, da_val, gross_total)
            
    except ValueError:
        print("Invalid input. Please enter numeric values for salary and counts.")

# Entry point of the program
if __name__ == "__main__":
    main()