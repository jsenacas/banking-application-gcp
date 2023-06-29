import requests
import json

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    response = requests.get("https://randomuser.me/api/")
    data = response.json()

    if response.status_code == 200:
        results = data["results"]

        if results:
            user = results[0]
            name = user["name"]
            title = name["title"]
            first_name = name["first"]
            last_name = name["last"]


    print(title)
    print(first_name)
    print(last_name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
