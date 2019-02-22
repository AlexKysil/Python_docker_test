
from Just_test.python_code.class_to_accept_json import class_to_accept_json
import os
import jsonpickle

def read_json():
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../json_data/test.json")
    with open(file) as f:
        data = jsonpickle.decode(f.read())
        return data

def create_obj(readed_file):
    obj = class_to_accept_json()
    obj.parametrize(readed_file)
    return obj

def write_to_json():
    obj = class_to_accept_json((1,2,3,4,5,6),"some_value", "some_username", "some end")
    file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../json_data/write.json")
    with open(file, "w") as f:
        jsonpickle.set_encoder_options("json", indent=2)
        f.write(jsonpickle.encode(obj))

if __name__ == '__main__':
    data = read_json()
    data.print_parametrs()
    data.say()





