# Write a program that reads in an investment amount, the annual interest rate, and the number of years,
# and then displays the future investment value using the following formula:
# futureInvestmentAmount = investmentAmount * (1 + monthlyInterestRate) ^ numberOfMonths

investmentAmount = float(input("Enter investment amount"))
interestRate = float(input("Enter interest rate"))
numberOfYears = float(input("Enter number of years"))


def investmentCalculator(investAmount, interestRate, numberOfYears):
    if investmentAmount <= 0 and interestRate <= 0 and numberOfYears <= 0:
        print("Error when calculating your investment amount")
    else:
        futureInvestmentAmount = investAmount * pow((1 + (interestRate / 100)), numberOfYears)
        print(futureInvestmentAmount)


investmentCalculator(investmentAmount, interestRate, numberOfYears)
