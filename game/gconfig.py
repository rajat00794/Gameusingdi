from pprint import pprint
import os
import json


class Config:
    def get_config(self, type_=None):
        if type_ is None:
            return (Exception("ARGERROR", "type_ should not be None"), False)
        BASE_CONFIG_PATH = f"game/config/"
        config_list = os.listdir(BASE_CONFIG_PATH)
        config_by_type = map(
            lambda x: [x if x.startswith(type_) else False], config_list
        )
        config_by_type = [x[0] for x in list(config_by_type) for i in x if i]
        os.chdir(BASE_CONFIG_PATH)
        try:
            with open(*config_by_type, "rb") as fs:
                data = json.loads(fs.read())
                fs.close()
        except Exception as e:
            return (e, False)
        reversedpath = BASE_CONFIG_PATH.split("/")[:-1]
        for i in range(len(reversedpath)):
            os.chdir("../")
        print(os.getcwd())
        return (dict(type_=type_, data=data), True)
