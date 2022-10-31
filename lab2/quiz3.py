# Write a program that reads in an investment amount, the annual interest rate, and the number of years,
# and then displays the future investment value using the following formula:
# futureInvestmentAmount = investmentAmount * (1 + monthlyInterestRate) ^ numberOfMonths

def investmentCalculator(investAmount, interestRate, numberOfYears) -> float:
    futureInvestmentAmount = investAmount * pow((1 + (interestRate / 1200)), numberOfYears * 12)
    return futureInvestmentAmount


investmentAmount: float = float(input("Enter investment amount"))
interestRate: float = float(input("Enter interest rate"))
numberOfYears: float = float(input("Enter number of years"))

futureInvestment: float = investmentCalculator(investmentAmount, interestRate, numberOfYears)
print(futureInvestment)
