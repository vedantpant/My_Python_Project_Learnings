#def raise_to_power(number, power):
 #   return number**power

#print(raise_to_power(5,3))

def raise_to_power(number, power):
    result = 1
    for index in range(power):
        result = result * number
    return result

print(raise_to_power(2, 3))
