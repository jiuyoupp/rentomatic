import json
from typing import Dict

class StorageRoomEncoder(json.JSONEncoder):
    # pylint不主张使用default定义函数和变量
    def default(self, o: dict): # pylint: disable=E0202
        try:
            to_serialize = {
                'code': str(o.code),
                'size': o.size,
                'price': o.price,
                "latitude": o.latitude,
                "longitude": o.longitude,
            }
            return to_serialize
        except AttributeError:
            return super().default(o)
