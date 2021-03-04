from PartyAttender import PartyAttender, AttenderMentor, AttenderStudent, SuperBoss

party_attenders = []

party_attenders.append(AttenderMentor("Иван Петров", "Москва"))
party_attenders.append(AttenderMentor("Виктор Куницин", "Киев"))

party_attenders.append(AttenderStudent("Виктория Коняхина", "Санкт Петербург"))
party_attenders.append(AttenderStudent("Виктор Гацуло", "Днепр"))
party_attenders.append(AttenderStudent("Дарья Шейко", "Магадан"))
party_attenders.append(AttenderStudent("Василий Стус", "Харьков"))
party_attenders.append(AttenderStudent("Майкл Щур", "Киев"))

party_attenders.append(SuperBoss("Incognito", "Washington DC"))

for party_attender in party_attenders:
    print("{}, {}, статус {}".format(party_attender.name, party_attender.city_from, party_attender.type))