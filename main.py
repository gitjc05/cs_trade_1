import requests
from info import stickers, capsules

main_url2 = f'http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name=StatTrak%E2%84%A2 M4A1-S | Hyper Beast (Minimal Wear)'

main_url = f'http://steamcommunity.com/market/priceoverview/?appid=730&currency=1&market_hash_name='

urls_extensions = [
    "Sticker%20%7C%20Apeks%20(Glitter)%20%7C%20Paris%202023",
    "Sticker%20%7C%20Apeks%20(Holo)%20%7C%20Paris%202023",
    "Sticker%20%7C%20Apeks%20%28Gold%29%20%7C%20Paris%202023",
    "Sticker%20%7C%20Fluxo%20%28Holo%29%20%7C%20Paris%202023",
    "Sticker%20%7C%20Into%20The%20Breach%20%28Holo%29%20%7C%20Paris%202023",
    "Sticker%20%7C%20Monte%20%28Holo%29%20%7C%20Paris%202023",
    "Sticker%20%7C%20Monte%20%28Gold%29%20%7C%20Paris%202023",
    "Sticker%20%7C%20Fnatic%20(Holo)%20%7C%20Paris%202023"
]

capsule_urls = [
    "Paris%202023%20Challengers%20Sticker%20Capsule",
    "Paris%202023%20Contenders%20Sticker%20Capsule",
    "Paris%202023%20Legends%20Sticker%20Capsule"
]

stick_names = [x for x in stickers]
stickers_total = 0
capsule_names = [x for x in capsules]
capsule_total = 0

for i in range(0, len(urls_extensions)):
    url = main_url + urls_extensions[i]
    r = requests.get(url=url)
    cur_price = r.json()["lowest_price"]
    cur_sticker = stick_names[i]
    initial_price = stickers[cur_sticker][1]
    cur_quantity = stickers[cur_sticker][0]
    cur_total = int(cur_quantity)*float(cur_price[1:])
    stickers_total += cur_total
    response = f'{cur_sticker}: {cur_price}, quantity: {cur_quantity}, total: {cur_total}, current Profit: {(int(cur_quantity)*float(cur_price[1:]))-(int(cur_quantity)*float(initial_price))}'
    print(response)

print("stickers total: "+str(stickers_total))

for i in range(0, 3):
    url = main_url + capsule_urls[i]
    r = requests.get(url=url)
    cur_price = r.json()["lowest_price"]
    cur_sticker = capsule_names[i]
    initial_price = capsules[cur_sticker][1]
    cur_quantity = capsules[cur_sticker][0]
    cur_total = int(cur_quantity)*float(cur_price[1:])
    capsule_total += cur_total
    response = f'{cur_sticker}: {cur_price}, quantity: {cur_quantity}, total: {cur_total}, current Profit: {(int(cur_quantity)*float(cur_price[1:]))-(int(cur_quantity)*float(initial_price))}'
    print(response)

print("Capsule total: "+str(capsule_total))

print("total: " + str(capsule_total+stickers_total))

