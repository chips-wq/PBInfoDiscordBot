import requests , json
def update_db(directory , auth , c):
    response = requests.get(directory , auth=auth)
    json_dict = json.loads(response.text)
    for file_or_dir in json_dict:
        if(file_or_dir["type"] == "dir"):
            print("Now searching for: " + directory+file_or_dir["name"] + "/")
            update_db(directory+file_or_dir["name"] + "/" , auth , c)
        if(file_or_dir["type"] == "file"):
            name_of_file = file_or_dir["name"]
            path_to_file = directory+file_or_dir["name"]
            raw_path = file_or_dir["download_url"]
            c.execute(f"INSERT INTO githubfiles (name , path , path_to_raw) VALUES (?, ?, ?)" , (name_of_file , path_to_file , raw_path))