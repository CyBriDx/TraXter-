from flask import Flask
from flask import send_file
from flask import request
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

@app.route('/data')
def data():
        slicerValues = request.args.get('Values')
        slicerNames = request.args.get('Filters')
        unixTime = request.args.get('EPOCH')
        username = request.args.get('UserName')
        text = 'Slicers: ' + slicerNames + '\nValues: ' + slicerValues \
            + '\nTime: ' + unixTime + '\nUser Name: ' + username
        font = \
           ImageFont.truetype('/usr/share/fonts/truetype/hack/Hack-Bold.ttf'
                            , 28, encoding='unic')
        (text_width, text_height) = font.getsize(text)
        canvas = Image.new('RGB', (text_width + 10, text_height * 6),
                            'orange')
        draw = ImageDraw.Draw(canvas)
        draw.text((5, 5), text, 'blue', font)
        canvas.save('unicode-text.png', 'PNG')
        return send_file('unicode-text.png', mimetype='image/png')
