import random

#create pets name here
# with open("ex17.store-pets-name.txt", "w") as file:
#     file.writelines(["Ace","\nAtlas","\nBailey","\nBear","\nBlaze","\nBoomer","\nBuddy","\nCoco","\nCooper","\nDuke","\nDozer","\nEcho","\nGizmo","\nHarley","\nMac","\nMax","\nMilo","\nOscar","\nRex","\nRocky","\nRocket","\nWolfie"])
    


data = open("ex17.store-pets-name.txt","r")
data_content = data.read()
data_content_list = data_content.split("\n")
# print(data_content)  

#randomly pick a single pet name.
print(random.choice(data_content_list))









                                                                                                                                                                                
                                                                                                                                                                                
                                                                                                                                                                                
                                                                                                                                                                                
                                                                                                                                                                                
                                                                                                                                                                                