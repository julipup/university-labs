import types
from typing import Tuple, Callable

class Date:
    # Class variables
    # format: Tuple[month name (str), days in month (int)]
    months: list[Tuple[str, int | Callable]] = [
        ("January", 31),
        # Checking if this year is a leap year or no
        # February has 29 days in leap year and 28 in normal year
        ("February", lambda year: 29 if (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0) else 28),
        ("March", 31),
        ("April", 30),
        ("May", 31),
        ("June", 30),
        ("July", 31),
        ("August", 31),
        ("September", 30),
        ("October", 31),
        ("November", 30),
        ("December", 31)
    ]

    # Instance-specific variables/methods
    def __init__(self, day: int, month: int, year: int):
        self.__day = day
        self.__month = month
        self.__year = year

        # Running checks
        self.__check_date()

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, new_day: int):
        if self.__is_day_correct(new_day):
            self.__day = new_day
        else:
            month_info = self.__get_month_info(month_index=self.__month)
            raise ValueError(f'Day value must be between 1 and { month_info[1] }')

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, new_month: int):
        if self.__is_month_correct(new_month):
            self.__month = new_month
        else:
            raise ValueError("Month value must be between 1 and 12")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year: int):
        self.__year = new_year

    def __get_month_info(self, month_index: int = None, month_name: str = None, year: int = None):
        if year is None:
            year = self.__year

        if not month_index and not month_name:
            raise AttributeError("You must pass either month_index or month_name variable to __get_month_info function")

        for index in range(0, len(Date.months)):
            # Helper function
            def transform_month(return_month: Tuple[str, int | Callable]):
                if isinstance(return_month[1], Callable):
                    # Days value are dynamically generated
                    return_month = (return_month[0], return_month[1](year))

                return return_month

            # Finding
            month = Date.months[index]

            if month_index == index + 1:
                return transform_month(month)
            elif month_name and month_name.lower() == month[0].lower():
                return transform_month(month)

    def __check_date(self):
        # Checking month info
        if not self.__is_month_correct(self.__month):
            raise ValueError("Month value must be between 1 and 12")

        if not self.__is_day_correct(self.__day):
            month_info = self.__get_month_info(month_index=self.__month)
            raise ValueError(f'Day value must be between 1 and { month_info[1] }')

    def __is_month_correct(self, month: int) -> bool:
        if 0 < month <= 12:
            return True

        return False

    def __is_day_correct(self, day: int, month: int = None) -> bool:
        if month is None:
            month = self.__month

        # Getting month info
        month_info = self.__get_month_info(month_index=month)

        # Checking
        if 0 < day <= month_info[1]:
            return True

        return False

    def __str__(self):
        return f'Date <day: { self.__day }, month: { self.__month }, year: { self.__year }>'