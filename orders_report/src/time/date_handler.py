from datetime import datetime
from dateutil.relativedelta import relativedelta
from zoneinfo import ZoneInfo

COLOMBIA = ZoneInfo("America/Bogota")

#Expected date format'2023-07-01T00:00:00.000-05:00' Using .isoformat() in the functions


def get_date():
    #TODO apply input validation for these fields
    #Yeah, i know they are error prone atm, i need to focus on the big picture right now

    year = int(input('Ingrese el año: '))
    month = int(input('Ingrese el mes (un numero del 1 al 12): '))
    day = int(input('Ingrese el día (un numero entre 1 y 30): '))

    return datetime(year, month, day).astimezone(COLOMBIA)


def get_time_between_dates(date_beginning, date_end):
    delta = relativedelta(date_end, date_beginning)
    return 12 * delta.years + delta.months


def get_timeframes():
    
    date_frames = []

    print(f'\n Para la fecha inicial:\n')
    date_b = get_date()

    print(f'\n Para la fecha final:\n')
    date_e = get_date()

    time_window = get_time_between_dates(date_beginning= date_b, date_end= date_e)

    upper_boundarie = date_b 
    lower_boundarie = date_e if time_window < 6 else (date_b + relativedelta(months = 6))
    

    while True:

        date_frames.append({
                "startDate" : upper_boundarie.isoformat(),
                "endDate": lower_boundarie.isoformat()
            })
        
        if(time_window <= 6):
            print(date_frames)
            return date_frames
        else:
            time_window -= 6
            upper_boundarie = lower_boundarie
            lower_boundarie = upper_boundarie + relativedelta(months= time_window if time_window < 6 else 6)



if __name__ == '__main__':
    get_timeframes()

# date1 = datetime(2022, 11, 1).astimezone(COLOMBIA)
# date2 = datetime(2023, 12, 1).astimezone(COLOMBIA) 
# print(get_time_between_dates(date_beginning=date1, date_end=date2))
# # print(date1 - relativedelta(months=6, days=1))
