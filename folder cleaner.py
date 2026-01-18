import os
import shutil

source = 'C:/Users/cc/Downloads'
destination = 'C:/Users/cc/Downloads/pictures'

images = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff']

for file in os.listdir(source):
    if any(file.lower().endswith(ext) for ext in images):
        shutil.move(f"{source}/{file}", f"{destination}/{file}")
        
    elif file.endswith(".html"):
        os.remove(f"{source}/{file}")
        
    else:
        print(f"Skipping file: {file}")

# for file in os.listdir(source):
#     if file.endswith('.tmp'):
#         shutil.move(f"{source}/{file}", f"{destination}/{file}")
        
#     elif file.endswith('.log'):
#         os.remove(f"{source}/{file}")
        
#     else:
#         print(f"Skipping file: {file}")
        
# print("File cleanup and transfer completed.")