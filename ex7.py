# Enter number in range 10 - 20 until you enter other number out of range
# display "Continue" if number in range 10 - 20
# display "Out of range" if number difference from range 10 - 20
number=20
result=""
for i in range(number):
    if i>10 and i<20:
        result="Continue"
    else:
        result="Out of range"
print(result)