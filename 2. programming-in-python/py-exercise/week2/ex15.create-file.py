
#file.write() for single line and file.writelines([]) for multiple lines.
with open("ex15.created-by-python.txt", "w") as file:  
    file.writelines(["\nWhat is Python?", "\nIt is a high level pro.language"])
 
    
#displays an error for correctly unlocated files
# try:
#     with open("sample/ex15.created-by-python.txt", "a") as file:
#         file.writelines(["\nWhat is Python?", "\nIt is a high level pro.language"])
# except FileNotFoundError as e:
#     print("ERROR",e)
   
        
           