import requests

URL = 'https://cloud-api.yandex.net/v1/disk/resources'
TOKEN = ""
headers = {'Content-Type': 'application/json', 'Authorization': f'OAuth {TOKEN}'}

def create_folder(path):
    return requests.put(f'{URL}?path={path}', headers=headers)

if __name__ == '__main__':
    path = 'New'
    create_folder(path)