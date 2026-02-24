# The heterogeneous employee data
employees = [
    {
        "id": 101,
        "name": "Arjun",
        "ratings": [4, 5, 3, 4],
        "details": {"experience": 5, "dept": "IT"}
    },
    {
        "id": 102,
        "name": "Zoya",
        "ratings": [5, 5, 5],
        "details": {"experience": 5, "dept": "HR"}
    },
    {
        "id": 103,
        "name": "Bhavna",
        "ratings": [4, 5, 3, 4],
        "details": {"experience": 8, "dept": "Sales"}
    },
    {
        "id": 104,
        "name": "Arjun",
        "ratings": [4, 5, 3, 4],
        "details": {"experience": 10, "dept": "Admin"}
    }
]

def sort_employees(data):
    # Sorting Criteria:
    # 1. Average Rating (Descending) -> Multiply by -1
    # 2. Experience (Descending)     -> Multiply by -1
    # 3. Name (Ascending)            -> Keep as is
    
    data.sort(key=lambda x: (
        -(sum(x['ratings']) / len(x['ratings'])), # Primary: Avg Rating Desc
        -x['details']['experience'],              # Secondary: Exp Desc
        x['name']                                 # Tertiary: Name Asc
    ))
    return data

# Execute and Display
sorted_list = sort_employees(employees)

print(f"{'Name':<10} | {'Avg Rating':<10} | {'Exp':<5}")
print("-" * 30)
for emp in sorted_list:
    avg = sum(emp['ratings']) / len(emp['ratings'])
    print(f"{emp['name']:<10} | {avg:<10.2f} | {emp['details']['experience']:<5}")