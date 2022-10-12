from pytz import tzinfo


class Shared:
    def set_timezone(self, date_time, tz: tzinfo):
        date_time = date_time.replace(tzinfo=None)
        return tz.localize(date_time)

    def convert_to_timezone(self, date_time, tz: tzinfo):
        return date_time.astimezone(tz)
