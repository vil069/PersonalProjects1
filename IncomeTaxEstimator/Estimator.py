#This is a personal project, written to mimic other free online income tax calculators.
#Do not use this program over more well known/trusted programs or professional services.

#This program uses the tax information as provided by https://www.debt.org/tax/brackets/
import math
def bracket_calculator(income, lbounds, ubounds):
    bracket = None
    if income <= (ubounds[0]): bracket = 1    
    elif lbounds[1] <= income <= (ubounds[1]): bracket = 2
    elif lbounds[2] <= income <= (ubounds[2]): bracket = 3
    elif lbounds[3] <= income <= (ubounds[3]): bracket = 4
    elif lbounds[4] <= income <= (ubounds[4]): bracket = 5
    elif lbounds[5] <= income <= (ubounds[5]): bracket = 6
    else: bracket = 7
    return bracket
        

def calculate_tax(income, filer_opt, deduction):
    taxable_income = income - deduction
    tax_percents = [.1, .12, .22, .24, .32, .35, .37]
    taxes = 0

    def helper(bracket, lbounds, ubounds):
        total = 0
        if bracket == 7:
            for i in range(0, len(ubounds)):
                total += (ubounds[i] - lbounds[i])*tax_percents[i]
        else:
            for i in range(0, bracket-1):
                total += (ubounds[i] - lbounds[i])*tax_percents[i]
        total += (taxable_income-lbounds[bracket-1])*tax_percents[bracket-1]
        return total

    if filer_opt == 1:
        #Single Filer
        #2020 Tax Bracket bounds
        lbounds = [0, 9876, 40126, 85526, 163301, 207351, 518401]
        ubounds = [9875, 40125, 85525, 163300, 207350, 518400]
        bracket = bracket_calculator(taxable_income, lbounds, ubounds)
        taxes = helper(bracket, lbounds, ubounds)

    elif filer_opt == 2:
        #Married filing jointly
        lbounds = [0, 19751, 80251, 171051, 326601, 414701, 622051]
        ubounds = [19750, 80250, 171050, 326600, 414700, 622050]
        bracket = bracket_calculator(taxable_income, lbounds, ubounds)
        taxes = helper(bracket, lbounds, ubounds)
    elif filer_opt == 3:
        #Married filing separately
        lbounds = [0, 9876, 40126, 85526, 163301, 207351, 311026]
        ubounds = [9875, 40125, 85525, 163300, 207350, 311025] 
        bracket = bracket_calculator(taxable_income, lbounds, ubounds)
        taxes = helper(bracket, lbounds, ubounds)
    else:
        #Head of household
        lbounds = [0, 14101, 53701, 85501, 163301, 207351, 518401]
        ubounds = [14100, 53700, 85500, 163300, 207350, 518400]
        bracket = bracket_calculator(taxable_income, lbounds, ubounds)
        taxes = helper(bracket, lbounds, ubounds)
    return math.ceil(taxes)
def main():
    opt_list = []
    opt_list.append("Single filter")
    opt_list.append("Married filing jointly")
    opt_list.append("Married filing separately")
    opt_list.append("Head of household")

    while True:
        try:
            print("Of the following options, which are you filing as?\n")
            for i in range(1, 5):
                print(str(i) + ". " + opt_list[i-1])
            filing_type = int(input("\nPlease enter the corresponding number: "))
            if (filing_type >= 1) and (filing_type <= 4):
                break
            else:
                print("Please enter a number corresponding to the options above.")
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
    while True:
        try:
            income = int(input("\nPlease enter the income amount: "))
            break
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
    while True:
        try:
            deduction = int(input("\nPlease enter the deduction amount: "))
            break
        except ValueError:
            print("Error: Please enter a valid number.")
            continue
    print("\nYour income tax estimate is: $" + str(calculate_tax(income, filing_type, deduction)))

if __name__ == "__main__":
    main()