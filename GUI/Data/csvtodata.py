import csv
import pandas as pd
import json
csv = {
    'theme': 'H:/QuantEmotion/EmotionQuant/GUI/Data/theme.csv',
    'block': 'H:/QuantEmotion/EmotionQuant/GUI/Data/block.csv',
}

csv_data = {
    'theme': 'H:/QuantEmotion/EmotionQuant/GUI/Data/theme/themedata.py',
    'block': 'H:/QuantEmotion/EmotionQuant/GUI/Data/block/blockdata.py',
}

def readAllCsv():
    for key, value in csv.items():
        try:
            reader = pd.read_csv(value, dtype=str)
            data = reader.to_dict()
            print(data)
            formatter_data = json.dumps(data, indent=4, ensure_ascii=False)

            if key in csv_data:
                tagret = csv_data[key]
                with open(tagret, 'w') as f:
                    f.write(f'data = {formatter_data}\n')
        except Exception as e:
            print(e)

readAllCsv()

