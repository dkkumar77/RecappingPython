
import random #library for random print statement
    #Print statement;



def print_statement():

        print("Hello")



def assigning_Variables():

    x = 5
    y = "test"
    print(x)
    print(y)

    a,b,c = 2, "a", "c"


    print("Value of a is " + a)

    print(type(x)) # returns the data type for x

    # Text Type - str;
    # int, float, complex (numeric types) 1, 1.0, 1j   ( j is imaginary)
    # list, tuple, range  (sequence types)
    # set, frozenset (set types)
    # bool (true/false)
    # bytes, bytearray, memoryview

    # converting/casting from int to float  --> int x = 1    ---> a = float(x)



def randomNumberGenerator():

    print(random.rand(1,10))


def print_statement_with_multiple_lines():


    print("""Hello,My Name is, insert_user_here.""")


def boolean_logic():

    if 3 > 2:
        print("it won't print this")
    else:
        print("it will print this")



def python_operators():

    # Comparison Operators --> Equal x == y ; Not Equal x!=y ;    >    ;  <  ;  >=   ;   <=
    # and, or, not

    x = 1
    y = 1
    if (x==y):
        print("do this")
    else:
        print("do this")



    # identity operators    x is y, x is not y;

    # bitwise operators    &, | ,  ^ , ~ , << , >>    Respectively  and, or, XOR, not, left shift, right shift




def accessingElementsInList():

    # Lists, are similar to arrays in java;

    list = [1,2,3,4]

    print(list[1]) #prints the 1st index of list, which is the number 2
    print(list[-1]) #prints the last index of the list, which is 4

    print(list[0:2]) # prints index 0 to index 2
    print(list[1:]) # prints index 1 to the end
    print(list[:2]) # prints from beginning to index 2

    # to change the element of a list, it would just be list[whatever_index] = whatever_value


    for x in list:
        print(x)

        # this will print every element within the list we made earlier

        # Here is some more logic

    if 1 in list:
        print("yes")

        # this will print yes, since we know that there is a integer value of 1 in this list



def add_elements_in_list():

    here_is_a_list = ["1",2,3,"4"]

    # to add an element in a list, you simply use the append method

    here_is_a_list.append("add_element")

    # if you want to insert an element within the list we have already created, simply use the insert method

    here_is_a_list.insert(1,"insert_element")

    # if you want to remove something from a list, use the remove method

    here_is_a_list.remove(here_is_a_list[2])
    # NOTE: you can also write the actual value.
    # For instance, if you wanted to remove the value of three: here_is_a_list.remove(3)


    new_list = here_is_a_list.copy()   #Copying a list into a new list

    new_list.append("1","2")

    # to add two lists together just use the '+' operator

    # To clear all elements within a list:

    here_is_a_list.clear();




def learning_tuples():


    # A tuple is similar to a list, however, the values can not be changed
    # However, you can convert the tuple into a list  -- > x = (1,2,3)   <-- this is a tuple
    # Lets convert it to a list  y = list(x)
    # Now back to list --- >   x = tuple (y)

    this_is_a_tuple = (1,2,3,4)

    # This is how to check whether or not a specific value is in the tuple


    if 1 in this_is_a_tuple:
        print("yes it is ")

    # Consider this, lets say there is a specific amount of elements within a tuple.
    # How can one know how many elements there are?
    # Use this len(insert_tuple_name)

    print(len(this_is_a_tuple))


    # To delete a tuple just write:    del tuple_name




def using_Dictionaries():


    # A dictonary is a collection of data that has a key and a value. Dictonaries are
    # unordered, and can be changed.

    here_is_a_dictionary = { "Name" : "Deepak", "Age" : 20, "Hair Color" : "Black"}

    # Lets say you want to get the value of the key "Age"

    print(here_is_a_dictionary.get("Age"))

    # Lets say you dye your hair and you want to change your hair color to blonde

    here_is_a_dictionary["Hair Color"] = "Blonde"


    # To print the K values (key value):

    for x in here_is_a_dictionary:
        print(x)


    # To print the values of K:

    for x in here_is_a_dictionary:
        print(here_is_a_dictionary[x])


    # You can also use the ".values()" methods in order to get the values within the dictonary


    #Lets say you need to grab the length of this dictonary.

    x_val = len(here_is_a_dictionary)


    # Need to remove a value from the dictonary?

    here_is_a_dictionary.pop("Name")    # Enter one of the key values

    # Add element

    here_is_a_dictionary["Height"] = "6'3"

    # Convenient Methods
    # popItem() - Removes Last Element
    # del here_is_a_dictonary("Age")   < -- Removed Key and Value
    # here_is_a_dictonary.clear()   <-- clear the list

    # You can also have multiple dictonaries within a Dictonary

    multiple_dictonaries = {{ "Name" : "Deepak", "Age" : 20, "Hair Color" : "Black"},
                           { "Name" : "Joshua", "Age" : 23, "Hair Color" : "Blonde"},
                           { "Name" : "Matt", "Age": 22, "Hair Color": "Brown"}}



def using_for_loops():

    for e in range(6):
        print(e)
    # Statement above prints out 0-5
    # Statement belwo prints out 2-9

    for z in range(2,10):
        print(z)













