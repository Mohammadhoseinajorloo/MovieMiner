class UpdateTime:
    def __init__(self, string):
        self.days = ["شنبه", "یکشنبه", "دوشنبه", "سه شنبه", "چهارشنبه", "پنج", "جمعه"]
        self.month = {
            "فروردین": 1,
            "اردیبهشت": 2,
            "خرداد": 3,
            "تیر": 4,
            "مرداد": 5,
            "شهریور": 6,
            "مهر": 7,
            "ابان": 8,
            "اذر": 9,
            "دی": 10,
            "بهمن": 11,
            "اسفند": 12,
        }
        date_list = self.covert_date(string)
        self.day = int(self.convert_farsi_to_english_numbers(date_list[0]))
        self.month = int(self.month[date_list[1]])
        self.year = int(self.convert_farsi_to_english_numbers(date_list[2]))

    def convert_farsi_to_english_numbers(self, input_str):
        farsi_digits = '۰۱۲۳۴۵۶۷۸۹'
        english_digits = '0123456789'
        translation_table = str.maketrans(farsi_digits, english_digits)
        return input_str.translate(translation_table)

    def covert_date(self, string):
        split_string = string.split(" ")
        if len(split_string) == 5:
            sliceing_string = split_string[2:]
        else:
            sliceing_string = split_string[1:]
        return sliceing_string
