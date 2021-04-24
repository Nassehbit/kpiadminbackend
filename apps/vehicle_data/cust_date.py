import pytz
from django.conf import settings
from datetime import date,datetime,timedelta

def filtDate():
    date_str=str(date.today() )
    print(date_str)
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    first_mon = ( date_obj- timedelta(days=date_obj.weekday())).replace(tzinfo=pytz.timezone(settings.TIME_ZONE))#TO START FROM MONDAY
    # first_mon = ( date_obj- timedelta(days=date_obj.isoweekday())).replace(tzinfo=pytz.timezone(settings.TIME_ZONE)) #TO START FROM SUNDAY
    print(first_mon)
    # today = datetime.datetime.today().replace(tzinfo=pytz.timezone(settings.TIME_ZONE))
    return {'first':first_mon,'today':datetime.now().replace(tzinfo=pytz.timezone(settings.TIME_ZONE))}