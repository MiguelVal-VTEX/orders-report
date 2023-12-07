from datetime import datetime
from dateutil.relativedelta import relativedelta
from zoneinfo import ZoneInfo

COLOMBIA = ZoneInfo("America/Bogota")

#Expected date format'2023-07-01T00:00:00.000-05:00' Using .isoformat() in the functions


def get_date() -> datetime:
    #TODO apply input validation for these fields
    #Yeah, i know they are error prone atm, i need to focus on the big picture right now

    '''Function to return a datetime object with a required date'''
    
    while True:
        try:
            year = int(input('Ingrese el año: '))
            month = int(input('Ingrese el mes (un numero del 1 al 12): '))
            day = int(input('Ingrese el día (un numero entre 1 y 30): '))
            break
        except ValueError:
            print('incorrect input. try again') 

    return datetime(year, month, day).astimezone(COLOMBIA)


def get_time_between_dates(
    date_beginning: datetime,
    date_end: datetime
    ) -> int:
    
    '''Returns the amount of months between two dates'''
    
    delta = relativedelta(date_end, date_beginning)
    return 12 * delta.years + delta.months


def get_timeframes(
    date_beginning: datetime,
    date_end: datetime,
    max_month_window: int = 6
    ) -> list[dict]:
    
    """This function generates a list with the max amount of even spaced time windows that can be generated between two dates

    date_beginning      -- The initial date
    date_end            -- The final date
    max_month_window    -- The separation between each time frame. By default it's 6 months
    
    Returns:
        The list "date_frames" that contains all of the time windows defined in the function
    """    
 
    date_frames = []
    
    time_window = get_time_between_dates(date_beginning, date_end) #how many months are between the two dates in total

    upper_boundarie = date_beginning 
    lower_boundarie = date_end if time_window < max_month_window else (date_beginning + relativedelta(months = max_month_window))
    

    while True:

        date_frames.append({
                "startDate" : upper_boundarie.isoformat(),
                "endDate": lower_boundarie.isoformat()
            })
        
        if(time_window <= max_month_window):
            print(date_frames)
            return date_frames
        else:
            time_window -= 6
            upper_boundarie = lower_boundarie
            lower_boundarie = upper_boundarie + relativedelta( months = time_window if time_window < max_month_window else max_month_window )



if __name__ == '__main__':
    get_timeframes()

# date1 = datetime(2022, 11, 1).astimezone(COLOMBIA)
# date2 = datetime(2023, 12, 1).astimezone(COLOMBIA) 
# print(get_time_between_dates(date_beginning=date1, date_end=date2))
# # print(date1 - relativedelta(months=6, days=1))
