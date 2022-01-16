import json
import requests

headers = {
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (iPad; CPU OS 11_0 like Mac OS X) AppleWebKit/604.1.34 (KHTML, like Gecko) Version/11.0 Mobile/15A5341f Safari/604.1"
}


def get_json(url):
    s = requests.Session()
    response = s.get(url=url, headers=headers)

    with open('aucs.json', 'w', encoding='utf-8') as file:
        json.dump(response.json(), file, indent=4, ensure_ascii=False)


def get_aucs():
    s = requests.Session()
    response = s.get(url='https://topdeck.ru/apps/toptrade/api-v1/auctions', headers=headers)
    data = response.json()

    result_data = []

    for lot in data:
        result_data.append({
            'Lot': lot.get('lot'),
            'Shipping': lot.get('shipping_info_quick'),
            'Shipping_info': lot.get('shipping_info'),
            'Price': lot.get('current_bid'),
            'Image_url': lot.get('image_url')
        })

    # print(result_data)

    with open('aucs.json', 'w', encoding='utf-8') as file:
        json.dump(result_data, file, indent=4, ensure_ascii=False)


def main():
    get_aucs()


if __name__ == "__main__":
    main()
