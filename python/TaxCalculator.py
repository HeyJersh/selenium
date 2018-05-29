"""
Project: Program to help calculate net income after deducting state taxes from gross income in different states
Goal: Coding Practice
Author: Josh Gomez (Kaizen)
"""

# Method constructor passing state and gross income arguments
def net_income(state, gross_income):

    # Organzing tax rates
    fed_tax_rate = 0.25
    fed_tax = gross_income * fed_tax_rate
    state_tax = {"ga": 0.06, "ca": 0.08}

    # Use the matching state tax rate provided by the 'state' argument
    if state in state_tax:
        tax_amount = fed_tax + (gross_income * state_tax[state])
        net_income = gross_income - tax_amount
        print ("Tax amount due is: " + str(tax_amount))
        print ("Net Income amount is: " + str(net_income))
    else: 
        print ("I don't know have any tax information for " + state)      

# Initialize the method
net_income("ga", 47000)