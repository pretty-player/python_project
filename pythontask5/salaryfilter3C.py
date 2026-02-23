def process_salaries(file_path, threshold):
    print(f"{'NAME':<15} {'DEPARTMENT':<15} {'SALARY':<10}")
    print("-" * 40)
    
    try:
        with open(file_path, 'r') as file:
            # Skip the header row if it exists
            header = file.readline() 
            
            for line in file:
                # 1. Clean the line (remove \n)
                clean_line = line.strip()
                
                # 2. Skip empty lines
                if not clean_line:
                    continue
                
                # 3. Split by comma to get individual columns
                parts = clean_line.split(',')
                
                # 4. Extract and validate data
                name = parts[0].strip()
                department = parts[1].strip()
                try:
                    salary = float(parts[2].strip())
                    
                    # 5. Filter and Display
                    if salary > threshold:
                        print(f"{name:<15} {department:<15} ${salary:,.2f}")
                except ValueError:
                    print(f"Skipping invalid data for {name}: {parts[2]}")

    except FileNotFoundError:
        print("Error: The data file was not found.")

# Execute the function
process_salaries("salarydata.txt", 50000)