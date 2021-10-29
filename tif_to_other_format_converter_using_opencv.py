# Using PILLOW

import glob
import cv2



# Old Format - Existing image format. New format - The desirable format which you want to conver the image to.
old_format = "tif"
new_format = "jpg"

# path is where you give the location of the images that is to be converted.
path = glob.glob(r"C:\Users\Raghotham\Downloads\image_format_converter\*"+"."+str(old_format))

# path_to_store_converted_images is where you give the location to store converted images.
path_to_store_converted_images = r"C:\Users\Raghotham\Downloads\image_format_converter\new_format_folder"

# adding backslash to the file path. As raw string does not allow direct '\' adding at the end. So, import os can be used or directly we can append.
path_to_store_converted_images+="\\"



for file in path:
    file_name = file.split('\\')[-1].split('.')[0] + "." + new_format
    path_to_store_images_with_file_name = path_to_store_converted_images+file_name
    print(path_to_store_images_with_file_name)
    im = cv2.imread(file)
    cv2.imwrite(path_to_store_images_with_file_name, im, [int(cv2.IMWRITE_JPEG_QUALITY),100])
    



