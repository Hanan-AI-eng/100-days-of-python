# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dic={"Key":"value"}
# cvalue= a_dic["hi"]

#IndexError
# fruit=["a","b"]
# frui=fruit[3]

#TypeError
# text="abc"
# print(text+5)
#
# try:
#     file=open("a_file.txt")
#     a={"k":"v"}
#     print(a["k"])
# except FileNotFoundError:
#     file=open("a_file.txt","w")
#     file.write("hi bro f ")
# except KeyError as error_message:
#     print(f"that {error_message} key dose not exist")
# else:
#     content=file.read()
#     print(content)
# finally:
#     raise TypeError("hello") # we rais aan error

height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError(f"Human Height should not be over 3 meters not .")

bmi= weight/ height **2
print(bmi)

