import base64
import requests
import random


def randomstring(_len: int):
    return "".join(str(random.randint(1, 9)) for i in range(_len))

def jwt_gen():
    _s = requests.Session()
    _res = _s.get(

        f"https://my.asos.com/identity/connect/authorize?state={str(randomstring(16))}&nonce={str(randomstring(16))}&client_id=D91F2DAA-898C-4E10-9102-D6C974AFBD59&redirect_uri=https%3A%2F%2Fwww.asos.com%2Fde%2Fherren%2F&response_type=id_token%20token&scope=openid%20sensitive%20profile&ui_locales=de-DE&acr_values=0&response_mode=json&store=DE&country=DE&keyStoreDataversion=dup0qtf-35&lang=de-DE&cgd=79418ebe2e7249448c5adcfc90239daa",
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Connection': 'keep-alive',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'Pragma': 'no-cache',
            'Cache-Control': 'no-cache',
            'Upgrade-Insecure-Requests': '1',
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
        },
        timeout = 10
    )
    if _res.ok != True:
        # Request Failed
        print(f"Failed [{_res.status_code}]")
        return False
    _sesid = _res.cookies['idsvr.session']
    _data = base64.b64encode(
        ('{"pingVersion":"1.3.0p","appId":"asos","appSessionId":"' + _sesid +'"}').encode('utf-8')
        )
    _data = str(_data).replace("b'", "").replace("'", "")
    
    _res = _s.get(
        f'https://st-static.asos.com/sdk/pong.js?body={_data}%3D'
    )
    if _res.ok != True:
        print(_res.text)
        return False
    _st = _res.text.strip().split("= '")[1].split("';")[0]
    return _st


