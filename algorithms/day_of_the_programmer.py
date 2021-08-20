def leap_year_day(leap, year_int) -> str:

    if leap == True:
        return '12.09.'+str(year_int)

    else:
        return '13.09.'+str(year_int)
        
def calculate_day(year) -> str:

    year_int = int(year)

    # case julian calendar up until including 1917
    if year_int <= 1917:

        # leap year
        if year_int % 4 == 0:
            return leap_year_day(True, year_int)
        # no leap year
        else:
            return leap_year_day(False, year_int)

    # case 1918 with its 32nd day being february 14th, therefore move forward day +13
    elif year_int == 1918:
        return '26.09.1918'


    # case gregorian from 1919 on
    else:
        if year_int % 4 == 0 and year_int % 100 != 0 or year_int % 400 == 0:
            return leap_year_day(True, year_int)

        else:
            return leap_year_day(False, year_int)

# get output for current year, just for fun
import pandas as pd

print(f"This year's day of the programmer falls on {calculate_day(pd.Timestamp.now().year)}")