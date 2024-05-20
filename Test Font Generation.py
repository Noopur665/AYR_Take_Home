import os
from PIL import Image, ImageDraw, ImageFont

fonts_path = 'fonts'
output_path = 'Test Fonts'

def create_font_images(fonts_path, output_path, texts, image_size=(600, 200), font_size=150, final_size=(475, 99)):
    if not os.path.exists(output_path):
        os.makedirs(output_path)

    fonts = [f for f in os.listdir(fonts_path) if f.endswith('.ttf')]

    for font_name in fonts:
        font_path = os.path.join(fonts_path, font_name)
        count = 0 
        for text in texts:
            image = Image.new('RGB', image_size, color='white')
            
            draw = ImageDraw.Draw(image)
            
            font = ImageFont.truetype(font_path, font_size)
            
#             width, height = draw.textsize((0,0),text, font=font)
            bbox = draw.textbbox((0, 0), text, font=font)
            width = bbox[2] - bbox[0]
            height = bbox[3] - bbox[1]
            
            text_x = (image_size[0] - width) / 2
            text_y = (image_size[1] - height) / 2
            
            draw.text((text_x, text_y), text, fill='black', font=font)
            
            font_name = font_name.split('.')[0]
            
            # Save the image
            image_file_name = f'Image_{count}_{font_name}.png'
            image.save(os.path.join(output_path, image_file_name))
            print(f'Saved {image_file_name}')
            count+=1


texts = ['Hi There! This is my take home project', 'Strawberries are red']  # Texts to render in each font
create_font_images(fonts_path, output_path, texts)