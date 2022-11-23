from PIL import Image, ImageDraw, ImageFont

im = Image.new('RGB', (500,200), color=('#FAACAC'))
# Создаем объект со шрифтом
font = ImageFont.truetype('C:\Windows\Fonts\Hatten.ttf', size=56)
draw_text = ImageDraw.Draw(im)
draw_text.text(
    (100, 100),
    'Газета "ПРАВДА"',
    # Добавляем шрифт к изображению
    font=font,
    fill='#1C0606')
im.show()

