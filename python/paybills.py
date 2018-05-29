"""
Project: Bill Pay Automation
Goal: Save time from manually paying bills every month
Author: Joshua Gomez (Kaizen)
Version: 0.1
"""

# Payment Dictionary for holding my payment options
payment_methods = {'visa': '1234123412341234', 'checking': '1111111'}
visa = payment_methods['visa']
checking = payment_methods['checking']

print (payment_methods)
print ("Your bills have been paid using the following payment method: " + visa)
