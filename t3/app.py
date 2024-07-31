import os,time, requests, aiohttp, asyncio, threading,multiprocessing
from flask import Flask,request, jsonify
from concurrent.futures import ThreadPoolExecutor
from fastapi import FastAPI

app = Flask(__name__)
app_fastapi=FastAPI()

def download_image(url):
    filename = url.split("/")[-1]
    res=request.get(url)
    with open(filename, 'wb') as file:
        file.write(res.content)
    print(f"{url}")

async def async_downloaded_image(session,url):
    filename = url.split("/")[-1]
    async with session.get(url) as res:
        async with aiofiles.open(filename, 'wb') as file:
            content = await response.read()
            await file.write(content)
        print(f"{url}")


@app_flask.route('/download', methods=["POST"])
def download_images_flask():
    start_time = time.time()
    urls=request.json['urls']
    with ThreadPoolExecutor(max_workers=len(urls)) as executor:
        executor.map(download_image,urls)
    total_time=time.time()-start_time
    return jsonify({'message':'Image good'})


@app_fastapi.post('/download')


if __name__ == "__main__":
    app.flask.run(port=5000, threaded=True)