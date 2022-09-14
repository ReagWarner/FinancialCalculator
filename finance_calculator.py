import math

print("\n\n------------------------------------Welcome to HyperionDev Bank------------------------------------\n\n")

#Get name from user to welcome them

name = input("\n\t\tPlease enter your name:\n\n")
welcome = print(f"\n\t\tWelcome,{name}.\n\n")

#Get input from user with formatting 
#Save input as insurance_type variable

print("\n\n---------------------------------------------------------------------------------------------------------\n\n")

print("\n\t\tChoose either 'investment' or 'bond' from the menu below to proceed:\n\n")

investment_type = input("investment\t- to calculate the amount of interest you will earn on interest\nbond\t\t- to calculate the amount you'll have to pay on a home loan\n\n").upper()

#set a conditional statement for each investment type

#if user chooses 'investment':

print("\n\n---------------------------------------------------------------------------------------------------------\n\n")

if investment_type =='INVESTMENT':

    #get the investment amount from user
    #convert to a float

    investment_amount = float(input("\n\t\tPlease enter your depost amount in R's:\n\n"))
    
    #get interest rate from user 
    #convert to a float
    #divide interest rate by 100 to convert from a % to an integer


    interest_rate = float(input("\n\t\tPlease enter your interest rate in percentage:\n\t\t*please only enter a number*\n\n"))
    if interest_rate >-1:
        interest_percentage = interest_rate/100

    #get amount of years from user
    #convert to a float

    years = float(input("\n\t\tPlease enter the amount of years you wish to invest for:\n\n"))
    
    #get user to confirm compound or simple
    #use the upper function to convert all input to uppercase

    interest_type = input("\n\t\tPlease select 'compound' or 'simple' interest:\n\n").upper()

     #if interest is compound, use the compound formula
     #print out total compund interest with the format function

    if interest_type == 'COMPOUND':
            total_compound_interest = round(investment_amount * math.pow((1+interest_percentage),years))
            print(f"\n\t\tYour total compound interest is R{total_compound_interest}.")

     #if interest is simple, use the simple formula
     #print out total compund interest with the format function

    elif  interest_type == 'SIMPLE':
            total_simple_interest = round(investment_amount * (1 + interest_percentage*years))
            print(f"\n\t\tYour total simple interest is R{total_simple_interest}.")

    #if user enters nothing, print invalid

    else:
            print("\n\t\tYou have entered an invalid entry\n")

print("\n\n---------------------------------------------------------------------------------------------------------\n\n")


if investment_type =='BOND':

    #get the bond amount from user
    #convert to a float

    present_value = float(input("\n\t\tPlease enter the current value of your property in R's:\n\n"))
    
    #get interest rate from user 
    #convert to a float
    #divide interest rate by 12 to convert from annual to monthly

    interest_percentage = float(input("\n\t\tPlease enter your annual interest rate in percentage:\n\t\t*please only enter a number*\n\n"))
    
    monthly_interest = interest_percentage/12

    #get amount of month from user
    #convert to an integer

    months = int(input("\n\t\tPlease enter the amount of months you wish to repay your home loan:\n\n"))
    
    #get user to confirm compound or simple
    #use the upper function to convert all input to uppercase

    monthly_bond  = round((monthly_interest * present_value)/(1-(1 + monthly_interest)**(-months)))
    print(f"\n\t\tYour monthly bond repayment is R{monthly_bond}.")

    #if user enters nothing, print invalid
    
else:
        print("\n\t\tYou have entered an invalid entry\n")
