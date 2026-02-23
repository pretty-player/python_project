import csv
import os

def process_payroll(input_file, output_file):
    try:
        with open(input_file, mode='r', newline='') as infile:
            # 1. DictReader uses the first row as keys for the dictionary
            reader = csv.DictReader(infile)
            
            # 2. Define the new fieldnames (adding 'Bonus' and 'Total')
            fieldnames = reader.fieldnames + ['Bonus', 'Total']
            
            with open(output_file, mode='w', newline='') as outfile:
                # 3. DictWriter needs the fieldnames to create the header
                writer = csv.DictWriter(outfile, fieldnames=fieldnames)
                writer.writeheader()
                
                print(f"{'Name':<15} | {'Salary':<10} | {'Bonus':<8} | {'Total'}")
                print("-" * 50)

                for row in reader:
                    # 4. Perform calculations (convert strings to float)
                    salary = float(row['Salary'])
                    bonus = salary * 0.10  # 10% Bonus
                    total = salary + bonus
                    
                    # 5. Add new data to the row dictionary
                    row['Bonus'] = f"{bonus:.2f}"
                    row['Total'] = f"{total:.2f}"
                    
                    # 6. Write the updated dictionary to the new file
                    writer.writerow(row)
                    
                    print(f"{row['Name']:<15} | {salary:<10.2f} | {bonus:<8.2f} | {total:.2f}")

        print(f"\nSuccess! Updated payroll saved to: {output_file}")

    except FileNotFoundError:
        print(f"Error: '{input_file}' not found. Please create it first.")
    except KeyError as e:
        print(f"Error: Column {e} not found in the CSV. Check your header spelling.")

# --- Execution ---
process_payroll('bonusdata.txt', 'employees_with_bonus.csv')