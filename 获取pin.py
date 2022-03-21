import os
def main():
    print(get_cookie())

def get_cookie():
    cookie_list= os.environ['JD_COOKIE'].split('&')
    for ck in cookie_list:
        pin=ck.split(';')[0]
        return pin


if __name__ == '__main__':
    main()

