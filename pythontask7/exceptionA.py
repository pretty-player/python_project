def safe_division():
    try:
        # Prompting for user input
        num1 = input("Enter the dividend (the number to be divided): ")
        num2 = input("Enter the divisor (the number to divide by): ")

        # Converting inputs to floats (this can raise a ValueError)
        n1 = float(num1)
        n2 = float(num2)

        # Performing division (this can raise a ZeroDivisionError)
        result = n1 / n2
        print(f"\nSuccess! {n1} divided by {n2} is: {result}")

    except ValueError:
        print("\nError: Invalid input. Please enter numeric values only.")
    
    except ZeroDivisionError:
        print("\nError: You cannot divide by zero! The universe doesn't like that.")
    
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
    
    finally:
        print("Calculation attempt finished.")

# Run the function
safe_division()