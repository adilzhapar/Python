import re
import csv

handler = open("raw.data", 'r', encoding='utf8')
txt = handler.read()

BINp = r"\nБИН.*(?P<BIN>\b[0-9]+)"
NDSp = r"\nНДС.*(?P<NDS>\b[0-9]+)"
CHECKp = r"\nЧек.*(?P<CHECK>\b[0-9]+)"
CASSAp = r"\nКасса.*(?P<CASSA>\b[0-9]+-[0-9]+)"
ZNMp = r"\nЗНМ.*(?P<ZNM>\b[A-Z]+[0-9]+)"
DATEp = r"\nВремя.*(?P<DATE>\b[0-9]{2}.[0-9]{2}.[0-9]{4}.[0-9]{2}.[0-9]{2}.[0-9]{2})\n{1}(?P<ADDRESS>.*)\n{1}"


BINt = re.search(BINp, txt).group('BIN')
NDSt = re.search(NDSp, txt).group('NDS')
CHECKt = re.search(CHECKp, txt).group("CHECK")
CASSAt = re.search(CASSAp, txt).group("CASSA")
ZNMt = re.search(ZNMp, txt).group("ZNM")
DATEt = re.search(DATEp, txt).group("DATE")
ADDRESSt = re.search(DATEp, txt).group("ADDRESS")

pattern = r"(?P<name>.*)\n{1}(?P<cnt>.*)x(?P<price>.*)\n{1}(?P<sum>.*)\n{1}Стоимость\n{1}(?P<total>.*)"
patric = re.compile(pattern)

items = [["БИН","НДС","ЗНМ", "Касса", "Чек", "Наименование товара","Кол-во","Цена за единицу", "Дата и Время", "Адрес"]]

for m in re.finditer(patric, txt):
    items.append([BINt, NDSt, ZNMt, CASSAt, CHECKt, m.group("name").strip(), m.group("cnt").strip(), m.group("price").strip(), DATEt, ADDRESSt])
with open('file.csv', 'w', newline='', encoding='utf8') as f:
    writer = csv.writer(f)
    writer.writerows(items)

handler.close()