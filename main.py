from diaries.DiarySample import DiarySample
from diaries.OkazawaDiary import OkazawaDiary
from diaries.sunsunDiary import sunsunDiary

# ↓のリストには、メンバーの各日記が格納されます。
diaries = [
    DiarySample(),
    sunsunDiary(),
    OkazawaDiary(),
 main
]

for d in diaries:
    print("---------------------------------")
    print(d.get_date())
    print(d.get_summary())
    print(d.get_author())
    print()
