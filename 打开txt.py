with open("cookie.txt", "r") as fp:
    wslist = fp.readlines()
    for ws in wslist:
        wspin = ws.split("\n")[0]        
        print(wspin)