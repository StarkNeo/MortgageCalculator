import locale

locale.setlocale(locale.LC_MONETARY, "en_US.UTF-8")


class Customer:
    def __init__(self, input_name, input_address, input_age):
        self.name = input_name
        self.address = input_address
        self.age = input_age
        self.mortgages=[]
        

    def addMortgages(self, mortgage):
        self.mortgages.append(mortgage)

    def getName(self):
        return self.name
    
    def getMortgage(self):
        for i in self.mortgages:
            return i


class Mortgage:
    balance = 0

    def __init__(self, input_loan, input_interest_rate, input_years):
        self.loan = input_loan
        self.interest = input_interest_rate
        self.years = input_years
        self.payments = input_years*12
    
    def monthly_payment(self):
        interest_compound =self.interest / 12
        monthly_pay = (
            (interest_compound * self.loan) * (1 + interest_compound) ** self.payments
        ) / (((1 + interest_compound) ** self.payments) - 1)
        return round(monthly_pay,2)

    def mortgage_amortization(self):
        balance = self.loan;
        payment =self.monthly_payment()
        print(
            """
        Credit Information
        --------------------------------
        Loan:{loan}
        Interest Rate: {interest}%
        Years: {years}
        Payments: {payments}
        Monthly Payment: {monthly}    
        --------------------------------
        Mortgage Amortization Table:
        -------------------------------------------------------------------------
        Period  |   Initial balance         |   Payment  |   Final Balance   |
                
        -------------------------------------------------------------------------
        """.format(
                loan=locale.currency(self.loan, grouping=True),
                interest=(self.interest * 100),
                years=self.years,
                payments=self.payments,
                monthly=locale.currency(self.monthly_payment(), grouping=True),
            )
        )
        
        for x in range(self.payments):
            initialBalance = round(balance * (1 + self.interest / 12),2)
            if initialBalance < payment:
                payment = initialBalance    
                
            balance = initialBalance-payment
            
            print("""            {periodo:>3}    {ibalance:>15}      {payment:>15}     {fbalance:>15}""".format(
                    periodo=x + 1,
                    ibalance =locale.currency(initialBalance,grouping = True),
                    payment=locale.currency(payment, grouping=True),
                    fbalance=locale.currency(balance, grouping=True),
                ))
            
            
            
            

print("""
---------------------------------------------------
            House Payment Calculator
Estimate your monthly payment on your mortgage loan
---------------------------------------------------
""")
name=input("Name: ");
address= input("Address: ");
age= input("Age: ")
customer=Customer(name, address,age);
print("What is the amount to be financed?")
loan= int(input("Amount: "));
print("What is the yearly interest rate? ")
interest =float(input("interest rate: "))/100;
print("What is the Loan term?")
years=int(input("Years: "));
hipoteca=Mortgage(loan,interest,years)
customer.addMortgages(hipoteca)
print(customer.mortgages[0].mortgage_amortization());
