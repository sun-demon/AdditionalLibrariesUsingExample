from PIL import Image, ImageDraw, ImageFont


def draw():
    image_path = '../image/'

    # sky
    image = Image.new('RGBA', (1000, 1000), (144, 231, 255))
    image_draw = ImageDraw.Draw(image)

    # ground
    image_draw.rectangle((0, 900, 1000, 1000), fill=(1, 164, 90))
    image_draw.line((0, 900, 1000, 900), fill=(1, 100, 22), width=20)

    # facade
    image_draw.rectangle((200, 650, 800, 900), fill=(83, 134, 194), outline=(11, 93, 153), width=10)
    # door
    image_draw.rectangle((450, 700, 550, 900), fill=(89, 0, 24), outline=(53, 1, 15), width=6)
    # windows
    image_draw.rectangle((300, 700, 400, 830), fill=(240, 250, 255), outline=(11, 93, 153), width=8)
    image_draw.rectangle((600, 700, 700, 830), fill=(240, 250, 255), outline=(11, 93, 153), width=8)

    # roof
    image_draw.polygon(((500, 350), (900, 650), (100, 650)), fill=(237, 82, 82), outline=(130, 50, 50), width=8)
    # window
    image_draw.ellipse((450, 475, 550, 575), fill=(240, 250, 255), outline=(130, 50, 50), width=8)

    # fence
    for i in range(100, 950, 50):
        image_draw.rectangle((i-10, 800, i+10, 950), fill=(135, 76, 5), outline=(85, 47, 1), width=7)
    image_draw.rectangle((75, 830, 925, 850), fill=(135, 76, 5), outline=(85, 47, 1), width=7)
    image_draw.rectangle((75, 900, 925, 920), fill=(135, 76, 5), outline=(85, 47, 1), width=7)

    # text
    text = 'HOUSE'
    text_width, text_height = 80, 30
    font = ImageFont.truetype('arial.ttf', 20)
    text_image = Image.new('RGBA', (text_width, text_height), (0, 0, 0, 0))
    text_image_draw = ImageDraw.Draw(text_image)
    text_image_draw.text((0, 0), text, font=font, fill=(0, 0, 0, 0), stroke_width=2, stroke_fill=(0, 0, 0, 30))
    text_image = text_image.rotate(180, resample=Image.BICUBIC, expand=True)
    parity = False
    for j in range(0, 1000, j_step := round(text_height * 1.1)):
        parity = not parity
        for i in range(0, 1000, i_step := round(text_width * 1.1)):
            image.paste(im=text_image, box=(i - (0 if parity else text_width // 2), j), mask=text_image)

    # saving
    image.save(image_path + 'home.png', 'PNG')
    image.show()


if __name__ == '__main__':
    draw()
