import os
def main():
    print(get_cookie())

def get_cookie():
    cookie_list= os.environ['JD_COOKIE'].split('&')
    return cookie_list


if __name__ == '__main__':
    main()

