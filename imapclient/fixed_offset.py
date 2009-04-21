from datetime import datetime, tzinfo, timedelta

ZERO = timedelta(0)

class FixedOffset(tzinfo):
    """
    This class describes fixed timezone offsets in hours and minutes 
    east from UTC 
    """

    def __init__(self, minutes):
        self.__offset = timedelta(minutes=minutes)

        sign = '+'
        if minutes < 0:
            sign = '-'
        hours, remaining_mins = divmod(abs(minutes), 60)
        self.__name = '%s%02d%02d' % (sign, hours, remaining_mins)

    def utcoffset(self, _):
        return self.__offset

    def tzname(self, _):
        return self.__name

    def dst(self, _):
        return ZERO