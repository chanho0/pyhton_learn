import os

def main():
    print(get_cookie())

def get_cookie():
    pin_list=[]
    cookie_list= os.environ['JD_COOKIE'].split('&')
    for ck in cookie_list:
        pin=ck.split(';')[0]
        pin_list.append(pin)
    return pin_list


if __name__ == '__main__':
    main()

