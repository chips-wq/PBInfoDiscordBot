import json
config_json = None
with open("B:\Orice Legat de Programare\github search for exercise\config.json" , 'r') as cfg:
    json_cfg_str = cfg.read()
    config_json = json.loads(json_cfg_str)

auth = (config_json['username_github'] , config_json['token_github'])
BASE_DIR = config_json['base_dir_github']
token = config_json['token_bot']