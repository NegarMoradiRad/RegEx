import re
from datetime import datetime
from khayyam import JalaliDate

# تابع برای تبدیل تاریخ میلادی به هجری شمسی
def convert_to_jalali(date_str):
    formats = ['%d-%m-%Y', '%d/%m/%Y', '%d-%m-%y', '%d/%m/%y']
    for fmt in formats:
        try:
            date_obj = datetime.strptime(date_str, fmt)
            jalali_date = JalaliDate(date_obj)
            return jalali_date.strftime('%d-%m-%Y')
        except ValueError:
            continue
    return None

# تابع برای پیدا کردن تاریخ‌ها در متن و تبدیل آن‌ها
def find_and_convert_dates(text):
    # regex برای پیدا کردن تاریخ‌ها
    date_pattern = r'(\b\d{1,2}[-/]\d{1,2}[-/]\d{2,4}\b)'
    matches = re.findall(date_pattern, text)
    
    # تبدیل تاریخ‌های پیدا شده
    converted_dates = {}
    for date in matches:
        jalali_date = convert_to_jalali(date)
        if jalali_date:
            converted_dates[date] = jalali_date
    
    return converted_dates

# متن نمونه
text = "This is a sample text with dates: 11-07-2024, 9-7-2024, 9/7/204, and 9/7/24."

# پیدا کردن و تبدیل تاریخ‌ها
converted_dates = find_and_convert_dates(text)
for original_date, jalali_date in converted_dates.items():
    print(f"{original_date} -> {jalali_date}")
