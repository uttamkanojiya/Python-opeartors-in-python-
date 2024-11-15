#program to display the various type of identity opeartor
#1. is opeartor
#   In this opeartor compare the memory location or identity of the object
#    if both the object having the same memory location or having same identity
#    then it gives "true"
#    if both the object having the different memory location or having different identity
a=23
b=23
print(a is b)
print(id(a))
print(id(b))
A=2
B="2"
print(A is B)
print(id(A))
print(id(B))
#2. is not opeartor
# This opeartor is oppsite of the is opeartor
#  this opeartor also compare the object but it is a oppsite of is not opeartor
#    if both the object having the same memory location or having the different identity
#    then its gives "false"
#    if both the object having different memory location or having the different identity
#    then it gives "true"
e=23
w=23
print(e is not w)
print(id(e))
print(id(w))
E=23
W="23"
print(E is not W)
print(id(E))
print(id(W))
