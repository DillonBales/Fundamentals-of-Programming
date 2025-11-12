def final_amt(p, r, n, t):
    """
    Apply the compound interest formula to p
    to produce the final amount.
    """

    a = p * (1 + r/n) ** (n*t)
    return a # This is new, and makes the function fruitful.

def final_amt_v2(principalAmount, nominalPercentageRate, numTimesPerYear, years):
 a = principalAmount * (1 + nominalPercentageRate / numTimesPerYear) ** (numTimesPerYear*years)
 return a

def final_amt_v3(amt, rate, compounded, years):
    a = amt * (1 + rate/compounded) ** (compounded*years)
    return a

# now that we have the function above, let us call it.
toInvest = float(input("How much do you want to invest?"))
fnl = final_amt(toInvest, 0.08, 12, 5)
print("At the end of the period you’ll have", fnl)