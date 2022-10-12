import requests
import json

URL = "http://127.0.0.1:8000/Studentapi/"


##read method (get)
def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.get(url = URL,headers=headers, data = json_data)
    data = r.json()
    print(data)
#get_data()


##create data (post)
def post_data():
    data = {
    'name':'palak',
    'roll':33,
    'city':'harda'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url = URL,headers=headers, data = json_data)
    data = r.json()
    print(data)
#post_data()

#update data (put)
def update_data():
    data = {
    'id':2,
    'name':'rohit',
    'city':'uk'
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.put(url = URL,headers=headers, data = json_data)
    data = r.json()
    print(data)


#update_data()


#delet data (delete)
def delete_data():
    data = {
    'id':2
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.delete(url = URL,headers=headers, data = json_data)
    data = r.json()
    print(data)
delete_data()