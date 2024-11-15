#program to display the various type of bitwise opeartor
#1.&(and) bitwise opeartor
    # In (&)and bitwise opeartor
    #    if both bits are zero(0) it will give 0
    #    and if both the bits are one(1) it will give 1
a=5
b=7
print(a&b)
#2.|(or) bitwise opeartor
    # In |(or) bitwise opeartor
    #     if both the value of bits is zero(0) it will give one(0)
    #     if the value of bits is different i.e zero(0) and one(1)
    #     it will give one(1)
print(a|b)
#3.^(Exor) bitwise opeartor
    # In ^(Exor) bitwise opeartor
    #   if both the value of bits are same then its give zero(0)
    #   and if both the value of bits are different then its give one(1)
print(a^b)
#4.~(Not) bitwise opeartor
    # In ~(Not) bitwise opeartor
    #    simple formule is {~n= -(n+1),where n is anynumber }
print(~b)
#5.<<(left shift) bitwise opeartor
    # In <<(left shift) bitwise opeartor
    #    its gain the bits
    #    simple formula is {(X<<n)=x*n**2,where n is anynumber}
print(b<<100)
#6.>>(right shift) bitwise opeartor
    # In >>(right shift) bitwise opeartor
    #   its lose the bits
    #   simple formula is {(x>>n)=x/n**2,where n is any number}
    
