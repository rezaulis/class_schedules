room = {'CS101':'3004','CS102':'4501','CS103':'6755','NT110':'1244','CM241':'1411'}
instructor = {'CS101':'Haynes','CS102':'Alvarado','CS103':'Rich','NT110':'Burke','CM241':'Lee'}
time = {'CS101':'8:00 a.m.','CS102':'9:00 a.m.','CS103':'10:00 a.m.','NT110':'11:00 a.m.','CM241':'1:00 p.m.'}

A = str(input("Enter a course number: ")).upper()
if A not in room and instructor and time:
    print(A, "is an invalid course number")
else:
    print("The details for Course",A,"are:")
    print("Room: ", room[A])
    print("Instructor: ", instructor[A])
    print("Time: ", time[A])
