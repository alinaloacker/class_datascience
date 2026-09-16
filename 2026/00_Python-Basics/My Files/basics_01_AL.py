print("Hello, world!")
str='''hello
i can do this juhu??'''
str
print(str)
type(2.1)
cast_int = int(1.2)
print(cast_int)

cast_int = int(1.2)
cast_float = float(4)
cast_complex = complex(3.5)
cast_str = str(9.2)

print(type(cast_int), cast_int)
print(type(cast_float), cast_float)
print(type(cast_complex), cast_complex)
print(type(cast_str), cast_str)

imp_str = '5.3'
conv_str = float('5.3')
print(type(imp_str), imp_str)
print(type(conv_str), conv_str)

var = 7
var+= 1.5
print(var)

7==6
True==1
True==0

4!=5
4==5
4>=5
4<=4
4<=4.5


cost = 3            # individual cost 
benefit = 1         # social benefit
kappa = 0.5         # degree of morality

# condition for cooperation: 
# social benefit times kappa is greater than individual cost times (1-kappa)

if benefit*kappa >= cost*(1-kappa):
    print('The individual cooperates!')
else:print('oh no!')

a = "Hello"
a
print(a)

list_1 = [1,23,54]
print(list_1)
print(type(list_1),list_1)

slicing_list = [2,3,4,5]
slicing_list [0:2]

slicing_list = [0,1,2,3,4,5,6,7,8,9]
slicing_list[-1:6:-2]
slided_list = slicing_list[-1:6:-2]
print(slided_list)
print(slicing_list)
slicing_list [1] = 2
print(slicing_list)
slicing_list
slicing_list.append(19)
slicing_list
slicing_list.clear()
slicing_list
slicing_list = [0,1,2,3,4,5,6,7,8,9]

list=[12,6,5,2,34,1]
list.sort()
list
list.reverse()
list
tuple=tuple(list)
tuple
a,b,c,d,e,f = tuple
print (a)

dictionary_morality = dict(Florence=0.3, Jordane=0.2, Julia=0.5)  
dictionary_morality['Julia']
copy_dictionary_morality = dictionary_morality.copy()
copy_dictionary_morality


new_tuple=(1,2,3,4)
new_tuple
sliced_tuple=new_tuple[0:3:2]
sliced_tuple
new_tuple
new_tuple.append(5)
