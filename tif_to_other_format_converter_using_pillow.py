# Using PILLOW

import glob
from PIL import Image

def tif_image_converter(old_format,new_format, img_path, path_to_store_converted_images):

    # old_format - The image format which is to be converted, is appended to img_path.
    path = glob.glob(img_path+"\*."+str(old_format))
    
    # adding backslash to the file path. As raw string does not allow direct '\' adding at the end. So, import os can be used or directly we can append.
    path_to_store_converted_images+="\\"

    for file in path:
        file_name = file.split('\\')[-1].split('.')[0] + "." + new_format
        path_to_store_images_with_file_name = path_to_store_converted_images+file_name
        # print(path_to_store_images_with_file_name)
        im = Image.open(file)
        print(im.save(path_to_store_images_with_file_name))


# Old Format - Existing image format. New format - The desirable format which you want to conver the image to.
old_format = "tif"
new_format = "jpg"

# img_path - the location of the images that is to be converted.
img_path = r"C:\Users\raghotham\Documents\stargan"
path_to_store_converted_images = r"C:\Users\raghotham\Documents\stargan\new_format_folder"

tif_image_converter(old_format,new_format, img_path, path_to_store_converted_images)
