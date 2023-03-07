pages_per_book = int(input())
pages_per_hour = int(input())
days_per_book = int(input())
hours_per_day = (pages_per_book // pages_per_hour) // days_per_book
print(hours_per_day)