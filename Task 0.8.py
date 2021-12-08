def time_convert(time):
    hours = (time//60)
    minutes = (time%60) 
    if time <120 and time >60:
        print("%d Hour %02d Minutes" % (hours, minutes))
    elif time <60: 
        print("%02d Minutes" % (minutes))
    else:
        time >120;
        print("%d Hours %02d Minutes" % (hours, minutes))

time_convert(246)