'''Language detection, trying to detect vinted.cz products with Polish origin.
Working, but dismissed as unreliable. Detects Czech words without diacritics 
in another language. Indentify "tl" as a country code for East Timor instead of "cs" 
for the Czech Republic'''
from langdetect import detect
import seaborn as sns
with open('dataset_vinted-premium-actor_2024-10-22_06-42-43-186.csv', mode='r', encoding='utf-8') as file: df = pd.read_csv(file)
[def detect_my(file): try: return detect(file) except: return 'unknown']
df['language'] = df['title'] .apply(detect_my) df.to_csv('updated_vinted_dataset_with_language.csv', index=False)
