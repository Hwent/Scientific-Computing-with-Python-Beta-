weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def date_format(time):
    return f"{time:02d}"
def find_weekday_index(weekday):
    weekday_lower = weekday.lower()
    for index, day in enumerate(weekdays):
        if day.lower() == weekday_lower:
            return index
    return None
def add_time(start, duration,weekday=''):
    period=start.split()
    duration=duration.split()
    hour=int(period[0].split(':')[0])
    minutes=int(period[0].split(':')[1])
    duration_hour=int(duration[0].split(':')[0])
    duration_minutes=int(duration[0].split(':')[1])
    

    end_hour=hour+duration_hour+int((minutes+duration_minutes)/60)
    end_minutes=(minutes+duration_minutes)%60
    end_period=period[1]
    day_change=''
    day=0
    end_weekday=''
    index=-1
    if weekday:
        index=find_weekday_index(weekday)

    while end_hour>12 :
        if end_period=='AM':
            end_hour-=12
            end_period='PM'
        else:
            end_hour-=12
            end_period='AM'
            day_change=' (next day)'
            day+=1
            index=(index+1)%7
    #Expected period to change from AM to PM at 12:00
    if end_hour==12:
        if end_period=='AM': 
            end_period='PM'
        else:
            end_period='AM'
            day_change=' (next day)'
            day+=1
            index=(index+1)%7
    if day>1:
        day_change=f" ({day} days later)"    
    if weekday:
        end_weekday=', '+weekdays[index]
    new_time=str(end_hour)+':'+date_format(end_minutes)+' '+end_period +end_weekday+ day_change
    print(new_time)

    return new_time


add_time('11:43 AM', '00:20')
add_time('11:55 AM', '3:12')
add_time('10:10 PM', '3:30')
add_time('2:59 AM', '24:00')
add_time('2:59 AM', '24:00', 'saturDay')
add_time('11:59 PM', '24:05', 'Wednesday')
add_time('8:16 PM', '466:02', 'tuesday')