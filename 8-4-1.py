import re

data = 'かなり昔のRX-7で東京駅まで送ってもらい、成田空港からBoreing787で高松空港まで行き、帰りはN700系で岡山から帰りました。'
re.findall(r'[a-zA-Z-]+\d+', data)
