def time_convert(time):
    hours = (time//60)
    minutes = (time%60) 
    if time ==0:
        print("0 Hours, 0 Minutes")
    elif time ==1:
        print("%02d Minute" % (minutes))
    elif time <60 and time >=2:
        print("%02d Minutes" % (minutes))
    elif time >=120:
        print("%d Hours, %02d Minutes" % (hours, minutes))
    elif time < 120 and time >= 60:
        print("%d Hour, %02d Minutes" % (hours, minutes))

time_convert(0)