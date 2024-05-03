import requests
import json
from bs4 import BeautifulSoup
import websockets
import base64
import io
url = "https://waifulabs.com"
class Waifulab:

    def __init__(self):
        session = requests.session()
        response = session.get(f'{url}/generate')
        soup = BeautifulSoup(response.text, 'html.parser').find_all('script')
        for script_tag in soup:
            if 'window.authToken' in script_tag.text:
                auth_token_script = script_tag
                break
        self.auth_token = auth_token_script.text.split('window.authToken = "')[1].split('"')[0]
        self.uri = f'wss://waifulabs.com/creator/socket/websocket?token={self.auth_token}&vsn=2.0.0'
    async def second_image(self):
        async with websockets.connect(self.uri) as websocket:
            json_dict = {}
            
            await websocket.send('["3","3","api","phx_join",{}]')
            await websocket.recv()
            await websocket.send('["3","5","api","generate",{"id":1,"params":{"step":0}}]')
            image_data = json.loads(await websocket.recv())
            c=0
            for data in image_data[4]["response"]["data"]["newGirls"]:
                c+=1
                image,seed =data["image"],data["seeds"]
                json_dict[str(c)] = {f"{image}": f"{seed}"}
            return json_dict