This is a simple easy to use script for interacting with your discord account.
It requires the requests, random and json modules to work.

Example:

token = login("username","password")
status_possibilities = ["online","idle","invisible","dnd"]
current_status = "online"
while 5 > 4:
    if status_possibilities.index(current_status)+1 == 4:
        new_status = "online"
    else:
        new_status = status_possibilities[status_possibilities.index(current_status)+1]
    print(change_status(new_status,token))
    current_status = new_status
    time.sleep(0.25)
    
This script will change your status 4 times/sec. The change_status() function takes 2 inputs: the new status and the token.
Just a warning, but if you try to send requests to discord too fast, it will return 400 (meaning that your request didn't go through). For example, if you were to try to spam someone with messages, discord would stop you by blocking your requests.
