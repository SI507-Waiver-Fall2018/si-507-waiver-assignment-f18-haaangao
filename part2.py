# Han Gao / hangao

# these should be the only imports you need
import sys
import sqlite3

# write your code here
# usage should be 
#  python3 part2.py customers
#  python3 part2.py employees
#  python3 part2.py orders cust=<customer id>
#  python3 part2.py orders emp=<employee last name>

argument = sys.argv[1]

conn = sqlite3.connect('Northwind_small.sqlite')
c = conn.cursor()

print('***** Part 2 Output *****')


# print the list of all customers
if (argument == 'customers'):
    result = c.execute('''
    SELECT Id, CompanyName 
    FROM Customer
    ''')
    print("ID" + "\t" + "Customer Name")
    for row in result:
        print (*row, sep='\t')

# print the list of all employees
if (argument == 'employees'):
    result = c.execute('''
    SELECT LastName, FirstName 
    FROM Employee
    ''')
    print("Employee Name")
    for row in result:
        print (*row)

# print the list of orders dates for specific customer
if (argument == 'orders' and 'cust' in sys.argv[2]):
    customerId = sys.argv[2].replace("cust=", "")

    result = c.execute('''
    SELECT o.OrderDate 
    FROM "Order" o
    WHERE o.CustomerId = ?
    ''', [customerId])
    print("Order Dates for All Orders Placed for Customer",customerId)
    for row in result:
        print (*row, sep='\n')

# print the list of order dates for all orders managed by the specific employee
if (argument == 'orders' and 'emp' in sys.argv[2]):
    empLastname = sys.argv[2].replace("emp=", "")

    result = c.execute('''
        SELECT OrderDate
        FROM 'Order' o
        JOIN Employee e
        ON o.employeeId = e.Id
        WHERE e.LastName = ?
    ''', [empLastname])
    print("Order Dates for All Orders Managed by Employee",empLastname)
    for row in result:
        print (*row, sep='\n')

conn.close()