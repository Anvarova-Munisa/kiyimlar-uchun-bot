from aiogram.utils.keyboard import ReplyKeyboardBuilder

b_type = ReplyKeyboardBuilder()
types_list = ["Sport kiyimi","Klasic uslubdagi kiyim","Oversize kiyim","Uyga kiyish uchun"]
for t in types_list:
    b_type.button(text=t)
b_type.adjust(3)

b_sport = ReplyKeyboardBuilder()
kiyimlar = [" ochq havodagi  sport turlari uchun kiymlar ",
            "zal uchun kimlar","suzishga moljallangan kiyimlar"]
for kiyim in kiyimlar:
   b_sport.button(text=kiyim)
b_sport.adjust(3)

b_klasic = ReplyKeyboardBuilder()
klassic = ["buni ozizga moslab tanlab olasiz"]
for klasic in klassic:
    b_klasic.button(text=klasic)
b_klasic.adjust(3)

b_oversize = ReplyKeyboardBuilder()
oversizel = ["oversize uslubdagi kiyimlar ozizga moslab olishingiz mumkun"]
for oversize in oversizel:
    b_oversize.button(text=oversize)
b_oversize.adjust(3)


b_uy = ReplyKeyboardBuilder()
uykiyim = ["buni turlari juda kob ozizga yoqqanini tanlab olaverasz"]
for uy in uykiyim:
    b_uy.button(text=uy)
b_uy.adjust(3)

b_rang = ReplyKeyboardBuilder()
ranglar = ["oq","qora","havorang","qizil","yashil","sariq"]
for rang in ranglar:
    b_rang.button(text=rang)
b_rang.adjust(3)

b_razmer = ReplyKeyboardBuilder()
razmerlar = ["S","M","L","XL","XXL"]
for razmer in razmerlar:
    b_razmer.button(text=razmer)
b_razmer.adjust(3)