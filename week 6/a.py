# import os
import colorama

# # path = os.path


# # Documents
# #     teaching
# #         .
# #         a.py
# #         ..  
# #     ..  


# print(path)

# print(x)
from colorama import Fore
import os
# print(Fore.GREEN + "This line is Green")
# print(Fore.RED + "This line is RED")
# print(Fore.BLUE + "This line is Blue")
print("xyz")

path = "../.."
dirs = os.listdir(path)

for dir in dirs:
    print(Fore.GREEN + dir)
    new_dir_path = path + "/" + dir
    if os.path.isdir(new_dir_path):
        new_dirs = os.listdir(path + "/" + dir)
        for new_dir in new_dirs:
            print(Fore.RED + f"----{new_dir}")
