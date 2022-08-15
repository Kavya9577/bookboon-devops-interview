# -------------------------
# OPTION 1
# -------------------------
# This script is a work-around to avoid using any additional libraries 
# and only using the Python Standard library
tens = {10: 'ten', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 
        60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 
        100: 'hundred'}
for i in range(0, 101):
    if i % 10 == 0 and i!=0:
        print(tens[i])
    else:
        print (i)
