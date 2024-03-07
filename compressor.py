import os
import subprocess

target_img_file_size=200  # in Kilobytes
input_path = "/home/fiona/temp/PetrolBills"
target_path = input_path + "/compressed_images"
file_list = [ file for file in os.listdir(input_path) if os.path.isfile(os.path.join(input_path, file)) ]
# print(file_list)

if not os.path.exists(target_path):
    os.makedirs(target_path)
    print(f"Output folder '{target_path}' for output images created successfully.")



for file in file_list:
    copy_command = f'cp {input_path}/{file} {target_path}/{file}'
    # print(copy_command)
    subprocess.run(copy_command, shell=True, capture_output=True, text=True)
    compress_command = f'jpegoptim --strip-all --size={target_img_file_size}K {target_path}/{file}'
    subprocess.run(compress_command, shell=True, capture_output=True, text=True)

print(f"Images compressed successfully! \n Output folder = {target_path} \n")