from diaries.AbstractDiary import AbstractDiary


class OkazawaDiary(AbstractDiary):
    def get_date(self):
        return "2025-10-16"

    def get_summary(self):
        return "今日はバイトだった"

    def get_author(self):
        return "Okazawa"
