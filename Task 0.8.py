time = 124

hours = (time//60)

minutes = (time%60) 

if time <120 and time >60:
    print("%d Hour %02d Minutes" % (hours, minutes))
else:
    print("%02d Minutes" % (minutes))

if time >120:
    print("%d Hours %02d Minutes" % (hours, minutes))