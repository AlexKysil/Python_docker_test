import requests
import jsonpickle
import os

def test_rest_register():
    url = "http://users.bugred.ru/tasks/rest/doregister"
    json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../json_data/post_json.json")
    with open(json_file) as f:
        data = jsonpickle.decode(f.read())

    test = requests.post(url, data)
    print(test)

def rest_login():
    login_url = 'http://users.bugred.ru/user/login/index.html'
    json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../json_data/login_rest.json")
    with open(json_file) as f:
        data = jsonpickle.decode(f.read())

    response = requests.post(login_url, data)
    print(response)

def create_user():
    create_user_url = 'http://users.bugred.ru/tasks/rest/createuser'
    json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../json_data/user_info.json")
    with open(json_file) as f:
        user_data = jsonpickle.decode(f.read())

    response = requests.post(create_user_url, user_data)
    print(response)
    print(response.content)

if __name__ == '__main__':
    create_user()