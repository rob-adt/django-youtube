import time
from datetime import date

requestdate = date.today()
timereq = time.strftime("%H:%M:%S", time.localtime())  # Format the time as a string
stringdate = "Request on " + str(requestdate) + " " + timereq
print(stringdate)
