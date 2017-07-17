from datetime import datetime
from pytz import timezone

fmt = "%Y-%m-%d %H:%M:%S %Z%z"

# Current time in UTC
now_utc = datetime.now(timezone('UTC'))
print now_utc.strftime(fmt)

# Convert to US/Pacific time zone
now_pacific = now_utc.astimezone(timezone('US/Pacific'))
print now_pacific.strftime(fmt)