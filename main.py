import requests, random, json

chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "`", "~", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "[", "{", "}", "]", "\\", "|", ";", ":", "'", "\"", "<", ",", ".", ">", "/", "?"]

def get_random_string(min_length, max_length):
    msg = []
    length = random.randint(min_length,max_length)
    for i in range(length):
        rand_letter = random.choice(chars)
        msg.append(rand_letter)
    return str(''.join(msg))

def send_msg(msg, chat_id, token):

    # Payload and Headers 
    payload = {
        'content': str(msg)
    }
    header = {
        'authorization': str(token)
    }

    v = requests.post("https://discord.com/api/v9/channels/"+chat_id+"/messages", data=payload, headers=header)
    return v.status_code
            
def login(username, password):
    
    header = {
        'content-type': 'application/json'
    }
    
    payload = {
        'login': str(username),
        'password': str(password)
    }
    
    v = requests.post("https://discord.com/api/v9/auth/login", json=payload, headers=header)
    return json.loads(v.content)["token"]

def call(channel, token):
    
    header = {
        "authorization": str(token)
    }
    
    m = requests.get("https://discord.com/api/v9/channels/"+str(channel)+"/call", headers=header)
    return m.status_code
    
def edit_msg(msg,chat_id,edit_id,token):
    
    # Payload and Headers 
    payload = {
        'content': str(msg)
    }
    header = {
        'authorization': str(token)
    }

    v = requests.patch("https://discord.com/api/v9/channels/"+chat_id+"/messages/"+edit_id+"", data=payload, headers=header)
    return v.status_code
    
def change_username(username,password,token):
    
    # Payload and Headers
    payload = {
        username: str(username), 
        password: str(password)
    }
    
    header = {
        'authorization': str(token)
    }
    
    v = requests.patch("https://discord.com/api/v9/users/@me",json=payload,headers=header)
    return v.status_code

def set_reaction(msg_id,chat_id,token):
    
    # Headers
    header = {
        'authorization': str(token)
    }
    
    v = requests.put("https://discord.com/api/v9/channels/"+str(chat_id)+"/messages/"+str(msg_id)+"/reactions/%F0%9F%8F%B3%EF%B8%8F%E2%80%8D%F0%9F%8C%88/%40me",headers=header)
    return v.status_code

def delete_reaction(msg_id,chat_id,token):
    
    # Headers
    header = {
        'authorization': str(token)
    }
    
    v = requests.delete("https://discord.com/api/v9/channels/"+str(chat_id)+"/messages/"+str(msg_id)+"/reactions/%F0%9F%8F%B3%EF%B8%8F%E2%80%8D%F0%9F%8C%88/%40me",headers=header)
    return v.status_code

def change_status(status,token):
    
    # Payload and Headers
    payload = {
        "status": str(status)
    }
    header = {
        'authorization': str(token)
    }
    
    v = requests.patch("https://discord.com/api/v9/users/@me/settings",json=payload,headers=header)
    return v.status_code
