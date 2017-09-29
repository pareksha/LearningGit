import time
import webbrowser

a = time.ctime()
num = 1
print "This program started on " +a
while num<=3:
    webbrowser.open("https://www.youtube.com/watch?v=CdqYGVP_D6I")
    time.sleep(60)     
    num +=1
