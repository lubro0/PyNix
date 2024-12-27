user_input = input("pl: ")
if user_input == "pl":
    import os
    os.system("mkdir plugins")
    os.system("cd plugins")
    with open("plugins/README.txt", "w") as file:
        file.write("SOON")
    os.system("cd ~")
  
