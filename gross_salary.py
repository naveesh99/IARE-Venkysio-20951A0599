salary=int(input("enter"))
federal=float(input())#percentage
state=float(input())#percentage
pension=float(input())#percentage
weeks=int(input())
total_deduction=(federal+state+pension)/100
deduction_salary=salary*(total_deduction)
a=salary-deduction_salary
print("salary per week is  after deduction is:",a)
print("salary after", weeks,"weeks is:",weeks*a)
