import datetime
current_year =datetime.date.today().year
final_year =int(input("enter the final year:"))
if final_year < current_year:
    printf("final year must be greater than or equal to current year:")
else:
        print(f"leap years from {current_year} to{final_year}")
        for year in range(current_year,final_year +1):
            if(year % 4 ==0 and year % 100 !=0)or(year % 400==0):
                print(year)
