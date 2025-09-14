# ACTIVITY 1 - PILLOW ACTIVITY
from PIL import Image, ImageDraw, ImageFont

# setup poster size and background gradient
posterWidth, posterHeight = 800, 1150
colorTop, colorMid, colorBottom = (230, 100, 180), (255, 200, 220), (230, 100, 180)
poster = Image.new('RGB', (posterWidth, posterHeight))

# formula for mixing 3 colors in a gradient
for y in range(posterHeight):
    if y < posterHeight // 2:
        ratio = y / (posterHeight // 2)
        r = int(colorTop[0] * (1 - ratio) + colorMid[0] * ratio)
        g = int(colorTop[1] * (1 - ratio) + colorMid[1] * ratio)
        b = int(colorTop[2] * (1 - ratio) + colorMid[2] * ratio)
    else:
        ratio = (y - posterHeight // 2) / (posterHeight // 2)
        r = int(colorMid[0] * (1 - ratio) + colorBottom[0] * ratio)
        g = int(colorMid[1] * (1 - ratio) + colorBottom[1] * ratio)
        b = int(colorMid[2] * (1 - ratio) + colorBottom[2] * ratio)
    ImageDraw.Draw(poster).line([(0, y), (posterWidth, y)], fill=(r, g, b))

# variable to call out when creating shapes and text
draw = ImageDraw.Draw(poster)

# frames and images setup
frameWidth, frameHeight, frameGap = 210, 140, 20
frameTop = 790
frameLeft = (posterWidth - (3 * frameWidth + 2 * frameGap)) // 2
images = ['a.png', 'b.png', 'c.png']

# create rectangle shapes as frames for ccis phantoms highlight images
for i in range(3):
    x = frameLeft + i * (frameWidth + frameGap)
    draw.rectangle([x, frameTop, x + frameWidth, frameTop + frameHeight], fill=(0, 0, 0), outline=(0, 0, 0), width=6)
    img = Image.open(images[i]).resize((frameWidth - 15, frameHeight - 15))
    poster.paste(img, (x + 7, frameTop + 7))

# import phantom mascot
mascot = Image.open('mascot.png').resize((700, 700))
poster.paste(mascot, ((posterWidth - 700) // 2, 200), mascot if mascot.mode == 'RGBA' else None)

# simple function to center text
def drawCentered(text, height, font_size, color):
    font = ImageFont.truetype('arialbd.ttf', int(font_size))
    box = draw.textbbox((0, 0), text, font=font)
    textWidth = box[2] - box[0]
    draw.text(((posterWidth - textWidth) // 2, height), text, font=font, fill=color)

# texts
drawCentered('CCIS PHANTOMS', 70, 87, (0, 0, 0))
drawCentered('HIMAMAT INTRAMURALS 2K25', 150, 48, (90, 0, 90))
drawCentered('UNLEASH THE PHANTOM SPIRIT!', 940, 40, (128, 0, 128))
drawCentered('SPORTSMANSHIP | RESPECT | INTEGRITY | TEAMWORK | PERSEVERANCE', 985, 17.5, (0, 0, 0))
draw.rectangle([(50, 1025), (750, 1080)], fill=(255, 60, 140), outline=(0, 0, 0)) # rectangle for hype text
drawCentered('GO PHANTOMS! #HIMAMAT2025', 1030, 40, (0, 0, 0))

# save poster -- made by jillian cassandra balon -- bscs-4
poster.save('CSELEC2_4_BalonJillianCassandra_Activity1.png')