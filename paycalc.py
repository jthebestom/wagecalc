print("hourly pay calculator")
running = str(input("calc?: y/n "))

while running == "y":
    
    hourly_rate = 33
    overtime_rate = 45


    hours_worked = int(input(' how many hours have you worked: '))


    overtime_hours = hours_worked - 8
    pay = hourly_rate * hours_worked
    


    s_er = ""
    if overtime_hours != 1:
        s_er = "s"

    overtime_hours = hours_worked - 8

    if overtime_hours > 0:
        overtime_pay = overtime_hours * overtime_rate
    else:
        overtime_hours = 0
        overtime_pay = 0


    if hours_worked <= 0:
        print("you have not worked")


    elif hours_worked > 8:
        pay = 8 * hourly_rate + overtime_pay
        print(f"you are eligable for overtime pay of {overtime_hours} hour{s_er}")
        print(pay)


    elif hours_worked <= 8 :
        print(f"your pay is ${pay}")
        


    running = str(input("calc?: y/n "))


