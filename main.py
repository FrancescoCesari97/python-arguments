

# * default arguments = A default value for certain parameters default is used when that argument is omitted  
####################* make your functions more flexible, reduces # of arguments
                    # * 1. positional, 2. DEFAULT. 3. keyword, 4. arbitrary



#  DEFAULT arguments
def net_price(list_price, discount=0, tax=0.05):
    return list_price * (1 - discount) * (1 + tax)

# print(net_price(500))

# print(net_price(500, 0.1))

# print(net_price(500, 0.1, 0))

import time


#* count app timer


# def count(end, start=0):
#     for x in range(start, end + 1):
#         print(x)
#         time.sleep(1)
#     print("DONE!")

# count(30, 15)


# * keyword arguments = an arguments preceded by an identifier
# *###################  helps with readability, order of arguments dosen't matter

# def Hello(greeting, title, first, last):
#     print(f"{greeting} {title}{first} {last}")

# Hello("hello", title="Mr.", first="Spongbob", last="Squarepants")


# for x in range(1, 11):
#     print(x, end=" ")

# print("1", "2", "3", "4", "5", sep="-")


#* fucntion to generate a phone number

# def get_phone(country, area, first, last):
#     return f"{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=39, area=123, first=456, last=7890)

# print(phone_num)


#* ARBITRARY 
#* *args = allows you to pass multiple non-key arguments  
#* **kwargs = allows you to pass multiple keyword arguments  
#            * unpacking operator


#* *args 

# def add(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
 

# print(add(1, 2, 3, 4, 5))


# def display_name(*names):
#     for name in names:
#         print(name, end=" ")
    

# display_name("Spongebob", "Squarepants")



#* **kwargs

# def print_address(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key} - {value}")

# print_address(street="13 fake street", city="Civitanoava", state="Marche", zip="62012")



# * printing a shipping label

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")
    print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')}")
    print(f"{kwargs.get('state')}")
    print(f"{kwargs.get('zip')}")

shipping_label("Dr.", "Spongebob",
               street="123 Fake St.",
               city="Civitanoava",
                state="Marche",
                zip="62012")