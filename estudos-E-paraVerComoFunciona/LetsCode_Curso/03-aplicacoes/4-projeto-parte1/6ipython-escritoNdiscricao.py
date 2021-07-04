# coding: utf-8
import datetime
import datetime as dt
d = dt.date(2001, 9, 11)
d
today = dt.date.today()
today
tdelta = dt.timedelta(hours=12)
today + tdelta
bday = datetime.date(2016, 9, 24)
till_bday = bday - today
till_bday.days
dt_agora = dt.datetime.now()
dt_agora
dt_str = 'July 24, 2016'
dt = dt.datetime.strptime(dt_str, '%B %d %Y')
