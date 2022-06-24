from sanic import Sanic
from sanic.response import json
import requests


App = Sanic('roblox-proxy', strict_slashes=True)

@App.post("/")
async def roblox_proxy(request):
    '''
    METHOD: GET
    PATH: GET /v2/users/{userId}/groups/roles
    JSON: {}
    '''
    data = request.json
    if data['METHOD'] == 'GET':
        r = requests.get(data['PATH'])
    else:
        r = requests.post(data['PATH'], data=data['JSON'])

    return json(r.json())

if __name__ == '__main__':
    App.run(host='127.0.0.1', port='9040', access_log=False, debug=False)