
def get_input():
    name = input("Enter Employee Name: ")
    basic_salary = float(input("Enter Basic Salary: "))
    allowance = float(input("Enter Allowance: "))
    tax_rate = float(input("Enter Tax Rate (%): "))
    return name, basic_salary, allowance, tax_rate


def calculate_gross_salary(basic_salary, allowance):
    return basic_salary + allowance


def calculate_tax(gross_salary, tax_rate):
    return gross_salary * tax_rate / 100


def calculate_net_salary(gross_salary, tax):
    return gross_salary - tax


def print_salary(name, basic, allowance, gross, tax, net):
    print("\n--- Employee Salary Slip ---")
    print("Employee Name:", name)
    print("Basic Salary:", basic)
    print("Allowance:", allowance)
    print("Gross Salary:", gross)
    print("Tax Amount:", tax)
    print("Net Salary:", net)


name, basic, allowance, tax_rate = get_input()

gross = calculate_gross_salary(basic, allowance)
tax = calculate_tax(gross, tax_rate)
net = calculate_net_salary(gross, tax)

print_salary(name, basic, allowance, gross, tax, net)