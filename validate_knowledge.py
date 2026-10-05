import json
from pathlib import Path

path = Path('knowledge/banking_knowledge.json')
with path.open('r', encoding='utf-8') as f:
    data = json.load(f)

print(data['account_opening']['title'])
print(data['account_opening']['answer'][0])
print('---')
print(data['credit_card']['title'])
print(data['credit_card']['answer'][0])
