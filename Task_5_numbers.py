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


# -------------------------
# OPTION 2
# -------------------------
# This script uses a different library that needs to be installed before it
# can be imported and used in the script. For this script it is fine to use
# either of the options, but this one is most optimized
from num2words import num2words
for i in range(0, 101):
    if i % 10 == 0 and i!=0:
        print(num2words(i))
    else:
        print (i)

