
import  datetime
targettime = '18:00:00'
def main():
    countdown(targettime)

def countdown(targettime):
    nowtime = datetime.datetime.now()
    starttime =nowtime.strftime('%Y-%m-%d ')+targettime
    starttime_format = datetime.datetime.strptime(starttime,"%Y-%m-%d %H:%M:%S")
    waittime = starttime_format - nowtime
    print(waittime)

main()


