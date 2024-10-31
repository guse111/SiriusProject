#video_downloader.py
import requests

def download_from_yandex_disk(public_url, save_path):
    # Получаем ссылку для скачивания
    response = requests.get('https://cloud-api.yandex.net/v1/disk/public/resources/download', params={'public_key': public_url})
    download_url = response.json()['href']
    
    # Скачиваем файл и сохраняем
    with requests.get(download_url, stream=True) as r:
        r.raise_for_status()
        with open(save_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=2048):
                f.write(chunk)
                
public_url = 'https://disk.yandex.ru/i/rr6dnUFrok8Qiw'
save_path = 'video.mp4'
download_from_yandex_disk(public_url, save_path)
