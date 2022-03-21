def main():
    a=3
    for _ in range(1):
        try:
            a+=1
            if a > 5:
                print('成功',str(a))
                return
            else:           
                print('失败',str(a))
                continue
        except:
            continue

def retry():
    attempts = 0
    success = False
    while attempts < 3 and not success:
        try:
            #运行函数
            success =True

        except:
            attempts += 1
            if attempts == 3:
                break

if __name__ == '__main__':
    main()
