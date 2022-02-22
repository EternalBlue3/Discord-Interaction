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
