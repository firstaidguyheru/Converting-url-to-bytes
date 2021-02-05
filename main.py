from io import BytesIO
import requests
import aiohttp

## Synchronously

def sync():
    url = 'URL_HERE'
    r = requests.get(url)
    if r.status_code in range(200, 299):
        img = BytesIO(r.content)
        b = img.getvalue()
        print(b)
    else:
        print(f'Something went wrong. Response: {r.status_code}')
    return b

## Asynchronously

async def a_sync():
    url = 'URL_HERE'
    async with aiohttp.ClientSession() as ses:
        async with ses.get(url) as r:
            if r.status in range(200, 299):
                img = BytesIO(await r.read())
                b = img.getvalue()
                print(b)
            else:
                print(f'Something went wrong. Response: {r.status}')
            return b
