
def func (t,i):
    from PIL import Image, ImageDraw, ImageFont
    im = Image.new('RGB', (1920,1080), color=('#9932CC'))
# Создаем объект со шрифтом
    font = ImageFont.truetype('C:/Windows/Fonts/Hatten.ttf', size=56)
    draw_text = ImageDraw.Draw(im)
    draw_text.text(
        (800, 600),
        t,
        # Добавляем шрифт к изображению
        font=font,
        fill='#1C0606')
    #im.show()
    im.save(f'C:/Users/user/Documents/142a/picha{i}.jpg')
t=['До',
    'РЕ',
    'PE#']
for i in range (3):
    func(t[i],i)

