import os

class os_extention:
    
    def check(folder_path):
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
            print(f"The folder '{folder_path}' was successfully created.")
        else:
            print(f"The folder '{folder_path}' already exists.")