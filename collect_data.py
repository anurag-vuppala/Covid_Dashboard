import requests
import json

URL = "https://api.coronavirus.data.gov.uk/v1/data"

para = {
    "contant-type":"text/csv"
}

def get_data(url):
    
    r = requests.get(endpoint ,timeout=100)

    if r.status_code >= 400:
        raise RuntimeError(f'Request failed:{ r.text }')
    return r.json()

if __name__ == '__main__':
    endpoint = (
        'https://api.coronavirus.data.gov.uk/v1/data?'
        # 'filters=areaType=nation;areaName=england&'
        # 'structure={"data":"date",newCases":newCasesByPublishDate"}'
    )
    
    data = get_data(endpoint)
    print(data)
    with open('data.json','w') as f:
        json.dump(data, f)