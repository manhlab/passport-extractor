from PIL import ImageDraw, Image, ImageEnhance
import os
import easyocr
import tqdm

def text_recognition(file_path, text_file_name):
    reader = easyocr.Reader(["ru"])
    result = reader.readtext(file_path, detail=0, paragraph=True)
    with open (text_file_name, "a") as file:
        for line in result:
            file.write(f"{line} ")
        file.write(f"\n")
    
def contrast(input_image_path, output_image_path):
    color_image = Image.open(input_image_path)
    enhancer = ImageEnhance.Contrast(color_image)
    im_output = enhancer.enhance(1.5)
    im_output.save(output_image_path)

def sharpness(input_image_path, output_image_path):
    color_image = Image.open(input_image_path)
    enhancer = ImageEnhance.Sharpness(color_image)
    im_output = enhancer.enhance(1.5)
    im_output.save(output_image_path)
   
def brightness(input_image_path, output_image_path):
    color_image = Image.open(input_image_path)
    enhancer = ImageEnhance.Brightness(color_image)
    im_output = enhancer.enhance(1.5)
    im_output.save(output_image_path)
def black_and_white(input_image_path, output_image_path):
    color_image = Image.open(input_image_path)
    bw = color_image.convert('L')
    bw.save(output_image_path)
    
if __name__=='__main__':
    directory = './yolov5/Russian_Passport/images'
    files = os.listdir(directory)
    for f_name in tqdm.tqdm( files, total=len(files) ):
        file = directory + "/" + f_name
        sharpness(file, file)
        contrast(file, file)
        brightness(file, file)
        black_and_white(file, file)
        text_recognition(file_path=file, text_file_name="./result.txt")