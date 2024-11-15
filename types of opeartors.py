#program for practice of the opeartors in the python
#there are many opearors in python
print('1.arithmetic opeartors')
print()
print('A.addition opeartor')
A=156
B=123
print('A=156\nB=123')
addition=A+B
print(addition)
print()
print('B.substraction opeartor')
Q=1257
W=515
print('Q=1257\nW=515')
substraction=Q-W
print(substraction)
print()
print('C.multiplacation opeartor')
E=12
R=12
print('E=12\nR=12')
multiplacation=E*R
print(multiplacation)
print()
print('D.division opeartor')
print('there are two type of division opeartor viz')
print('1.normal division opeartor (/), 2.floor division opeartor (//)')
T=212
Y=4
print('T=212\nY=4')
normaldivision=T/Y
floordivision=T//Y
print(normaldivision)
print(floordivision)
print('if it is divide properly then the ans of floor division ans will be same ')
print('if not then the ans of floor division will be correct')
normaldivision == floordivision
print(normaldivision == floordivision)
print()
print('E.modules')
print('this opeartor is use to show the ans which is there in the remainder')
U=4535
I=55
print('U=4535\nI=55')
modules1=U%I
print(modules1)
modules2=I%U
print(modules2)
print('the ans of modules1 and modules2 are different')
print()
print('F.power opeartor')
O=12
power=O**3
print('O=12')
print(power)
print()
print('2.assignment opeartor')
print()
print('A.assiging opeartor')
print('there are only one opeartor which is (=)')
P=23341
print('P=23341')
print('here assignment opeartor is use to assign the value to the variable','p=23341')
print()
print('3.comparator opeartor')
print()
print('there are six types of comparetor opeartor viz')
print('A.ISEQUAL(==)')
S=1234
D=456
print("S=1234\nD=456")
S==D
print(S==D)
F=1234
print('S=1234\nF=1234')
S==F
print(S==F)
print('comparetor opeartoe is use to compare the two value of the variable')
print()
print('B.ISNOTEQUAL(!=)')
S=1234
D=456
print('S=1234\nD=456')
S!=D
print(S!=D)
print('this opeartor is use to compare the value of the two variables and then ans whether they are equal or not in true or false')
print()
print('C.ISLESSTHEN(<)')
print('this opeartor is use to tell us thta the given value of the variables is less then or not')
S=1234
D=456
print('S=1234\nD=456')
S<D
print(S<D)
print()
print('D.ISMORETHEN(>)')
print('this is the opeartor is use to compare whether the given value of the two variables is more then or not')
S=1234
D=456
print('S=1234\nD=456')
S>D
print(S>D)
print()
print('E.ISMORETHENEQUALTO (>=)')
print('This opeartor is use to tell us that the given two value of the variables are equal or morethen')
S=1234
D=456
print('S=1234\nD=456')
S>=D
print(S>=D)
print()
print('F.ISLESSTHENEQUALTO (<=)')
print('This opeartor is use to tell us that the given two value of the variables are equal or lessthen')
S=1234
D=456
print('S=1234\nD=456')
S<=D
print(S<=D)
print()
print('4.Membership opeartor')
print()
print('There are two type of membership opeartor viz')
print('A.in membership opeartor\nB.in not membership opeartor')
print()
print('A.in Membership opeartor')
print("This opeartor is use to check whether the given value is there in the list or not")
S='1234'
print("S='1234'")
print('3'in S)
print('4'in S)
print()
print('B. not in Membership opeartor')
print("This opeartor is use to check whether the given value is there in the list or not")
S='1234'
print("S='1234'")
print('45'not in S)
print('35'not in S)
print()
print("the combination of in and not in membership operator are as fallow")
print("S='1234'")
print('12'in S)
print('34'in S)
print('35'not in S)
print('6'not in S)
print('123'in S)
print('1243'in S)
print('1243'not in S)
print()
print('5.Identity opeartor')
print()
print('There are two type of identity opeartor viz')
print('A.is identity opeartor\nB.is not identity opeartor')
print()
print('A.is identity opeartor')
print()
print('This opeartor is use to compare the memory location of the value of the variables')
F=123
G=123
H=121
print('F=123,G=123\nH=121')
print(F is G)
print(G is F)
print(F is H)
print(G is H)
print()
print('B.is not identity opeartor')
print()
print('This opeartor is use to compare the memory location of the value of the variables')
F=123
G=123
H=121
print('F=123,G=123\nH=121')
print(F is G)
print(G is F)
print(F is not H)
print(G is not H)
print()
print('6.Bitwise opeartor')
print()
print('There are six type of Bitwise opeartor which work on the bites')
print('A.&(and) bitwise opeartor\nB.|(or) bitwise opeartor\nC.~(not) bitwise opeartor')
print('D.^(exor) bitwise opeartor\nE.<<(left shift) bitwise opeartor\nF.>>(right shift) bitwise opeartor')
print()
print('A.&(and) bitwise opeartor')
print()
print('This opeartor is use to print true when both the condition are TRUE')
print('If both the condition are different then it will print FALSE')
J=12
K=13
print('J=12\nK=13')
print((J>10)&(K<20))
print()
print('B.|(or) bitwise opeartor')
print()
print('This opeartor is use to print TRUE when any one condition is true')
print('If both the condition are false the it will print FALSE')
J=12
K=13
print('J=12\nK=13')
print((J>10)|(K>20))
print((J<10)|(K>20))
print()
print('C.^(exor) bitwise opeartor')
print()
print('This opeartor is use to print TRUE when both the condition are true')
print('If both the opeartor are different then it print TRUE')
J=12
K=13
print('J=12\nK=13')
print((J>10)^(K<20))
print((J<10)^(K>20))
print()
print('D.~(NOT) bitwise opeartor')
print()
print("This opeartor is different then the not opeartor formula for this is (~n)=-(n+1)")
J=12
K=13
print('J=12\nK=13')
print(~(J))
print(~(K))
print()
print('E.<<(left shift)')
print()
print('This opeartor is use to gain the bites')
G=123
print('G=123')
print(G<<123)
print()
print('F.>>(right shift)')
print()
print("This opeartor is use to loss the bites")
G=123
print('G=123')
print(G>>123)





