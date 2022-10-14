import datetime
import functools


class WeatherReport:
    # Instance methods
    def __init__(self, date: datetime.datetime, temperature: float, atmospheric_pressure: float, rainfall_level: float):
        self.__date = date
        self.__temperature = temperature
        self.__atmospheric_pressure = atmospheric_pressure
        self.__rainfall_level = rainfall_level

    def add_to_report(self, report):
        report.add_report(self)
        return self

    @property
    def date(self) -> datetime.datetime:
        return self.__date

    @property
    def temperature(self):
        return self.temperature

    @property
    def atmospheric_pressure(self):
        return self.__atmospheric_pressure

    @property
    def rainfall_level(self):
        return self.__rainfall_level

    def __str__(self):
        return f'WeatherReport <date: { self.__date }, temperature: { self.__temperature }, atmospheric_pressure: ' \
               f'{ self.__atmospheric_pressure }, rainfall_level: { self.__rainfall_level }>'


class MonthlyWeatherReport:
    def __init__(self, year: int, month: int):
        self.__year = year
        self.__month = month
        self.__days: dict[int, list[WeatherReport]] = {}

    def add_report(self, report: WeatherReport):
        year = report.date.year
        month = report.date.month
        day = report.date.day

        if year != self.__year or month != self.__month:
            raise ValueError(f'Could not add report { report } to { self } due to year/month inconsistency')

        # Checking if we have list for this day in our dict
        if day not in self.__days.keys():
            self.__days[day] = []

        # Adding this report
        self.__days[day].append(report)

    def get_average_pressure(self, from_days: int, to_days: int = None):
        if to_days is None:
            to_days = from_days + 1

        # Getting this day's reports
        days_average = []
        for day_index in range(from_days, to_days):
            if day_index not in self.__days:
                continue

            # Getting reports
            day_average = 0
            reports = self.__days[day_index]

            # Calculating average from this reports
            for report in reports:
                day_average += report.atmospheric_pressure

            day_average = day_average / len(reports)
            days_average.append(day_average)

        # Calculating average from days
        return functools.reduce(lambda a, b: a + b, days_average) / len(days_average)

    def get_average_temperature(self, from_days: int, to_days: int = None):
        # todo implement
        pass

    def get_average_rainfall_level(self, from_days: int, to_days: int = None):
        # todo implement
        pass

    @property
    def year(self):
        return self.__year

    @property
    def month(self):
        return self.__year

    def __str__(self):
        return f'MonthlyWeatherReport <year: {self.__year}, month: {self.__month}>'


# Adding test reports
monthly_report = MonthlyWeatherReport(2020, 1)
print(WeatherReport(datetime.datetime(2020, 1, 10), atmospheric_pressure=10, rainfall_level=0, temperature=36.6).add_to_report(monthly_report))
print(WeatherReport(datetime.datetime(2020, 1, 12), atmospheric_pressure=15, rainfall_level=0, temperature=36.6).add_to_report(monthly_report))
print(WeatherReport(datetime.datetime(2020, 1, 13), atmospheric_pressure=15, rainfall_level=0, temperature=36.6).add_to_report(monthly_report))
print(WeatherReport(datetime.datetime(2020, 1, 14), atmospheric_pressure=15, rainfall_level=0, temperature=36.6).add_to_report(monthly_report))
print(WeatherReport(datetime.datetime(2020, 1, 15), atmospheric_pressure=10, rainfall_level=0, temperature=36.6).add_to_report(monthly_report))

# Getting average
print("Average pressure between days 10 and 15:", monthly_report.get_average_pressure(10, 15))
