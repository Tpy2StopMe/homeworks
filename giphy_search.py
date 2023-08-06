import json
from urllib import parse, request


def giphy_search(search_obj:str, max_num_of_output:str) -> str:
    url = "http://api.giphy.com/v1/gifs/search"

    params = parse.urlencode({
    "q": search_obj,
    "api_key": "Dket0TnHxkA1Wv3lxvaj8C6j3wQPgczj",
    "limit": max_num_of_output
    })

    with request.urlopen("".join((url, "?", params))) as response:
        data = json.loads(response.read())
        # for elem in data["data"]:
        #     for key,value in elem.items():
        #         if key == "url":
        #             print(value)
    return([value for dict in data["data"] for key,value in dict.items() if key == "url"])
    
# When we need to get right url for next pasting

def giphy_search_2(search_obj:str, max_num_of_output:str) -> str:
    url = "http://api.giphy.com/v1/gifs/search"

    params = parse.urlencode({
    "q": search_obj,
    "api_key": "Dket0TnHxkA1Wv3lxvaj8C6j3wQPgczj",
    "limit": max_num_of_output
    })

    with request.urlopen("".join((url, "?", params))) as response:
        data = json.loads(response.read())
        first_step_parse = [value for dict in data["data"] for key,value in dict.items() if key == "images"]
        list_of_urls = [value for elem in first_step_parse for key,value in elem["original"].items() if key == "mp4"]
        # for elem in first_step_parse:
        #     for k, v in elem["original"].items():
        #         if k =="mp4":
        #             list_of_urls.append(v)
        # for elem in list_of_urls:
        #     print(parse.urlparse(elem))
    return list_of_urls

# print(giphy_search("lion", 2))
# print(giphy_search_2("lion", 2))