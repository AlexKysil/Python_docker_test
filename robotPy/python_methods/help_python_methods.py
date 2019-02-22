import requests
import jsonpickle
import os
import random
import string

URL = 'http://users.bugred.ru/tasks/rest/doregister'



def read_user_data_from_json(user):
    json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/generated_json/%s.json" %(user))
    with open(json_file) as f:
        user_data = jsonpickle.decode(f.read())
        return user_data

def register_new_user(user):
    registration = requests.post(URL, user)
    print(registration)

def create_new_user_on_website(user):
    userdata = read_user_data_from_json(user)
    register_new_user(userdata)
    return userdata

def display(data):
    print(data)

def set_user_email(user_name):
    user_data= read_user_data_from_json(user_name)
    return user_data['email']

def generate_credentials():
  email= ''.join(random.choice(string.ascii_lowercase)for x in range (7))+"@yopmail.com"
  name= ''.join(random.choice(string.ascii_lowercase)for x in range (10))
  password= ''.join(str(random.randint(0,9))for x in range (5))
  dict = {'email': email, 'name': name, 'password': password}
  return dict

def generate_json(dict, file_name = None, needName=False):
    if file_name != None:
        json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "../data/generated_json/%s.json" % (file_name))
    else:
        json_file = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 "../data/generated_json/%s.json" % (dict['name']))

    with open(json_file, "w") as f:
        jsonpickle.set_encoder_options("json", indent=2)
        f.write(jsonpickle.encode(dict))
    if needName==True:
        return dict['name']

def random_users_json(count, file_name="chrome_users"):
    users_list= {}
    for x in range (count):
       generated_data = generate_credentials()
       users_list.update({'user'+str(x+1): generate_json(generated_data, needName=True)})

    generate_json(users_list, file_name)

def get_user_from_list(users_list, user):
    readed_users_list = read_user_data_from_json(users_list)
    for key in readed_users_list.keys():
        if key == user:
            return readed_users_list[key]



if __name__ == '__main__':
    random_users_json(5)
    user1 = get_user_from_list("users", "user5")
    print(user1)