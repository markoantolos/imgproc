from PIL import Image, ImageDraw

def boxes(image, boxes):
    if image.mode != 'RGBA':
        image = image.convert('RGBA')
    boxes_image = Image.new('RGBA', image.size, 'white')
    draw = ImageDraw.Draw(boxes_image)
    for box in boxes:
        draw.rectangle(box, fill=(255, 0, 0, 120))
    output = Image.blend(image, boxes_image, alpha = 0.5)
    return output

