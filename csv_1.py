import csv


def add_employee():
    file_name = 'employee.csv'
    with open(file_name, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        while True:
            emp_id = input("Enter Employee ID: ")
            name = input("Enter Employee Name: ")
            salary = float(input("Enter Employee Salary: "))
            
            writer.writerow([emp_id, name, salary])
            
            # Ask the user if they want to continue
            choice = input("Do you want to add another employee? (y/n): ").strip().lower()
            if choice != 'y':
                break
            print("-" * 20)
            
    print(f"\nRecords saved to {file_name}.\n")
