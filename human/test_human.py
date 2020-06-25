from human.Human import Human


human =Human('Igor',32)
human.addHotel('IT','20.20.1999','IBIS')
human.addHotel('IT','20.20.2001','IBIS')
human.addHotel('PL','20.20.2000','HILTON')
human.travelInfo()

print(human.toList())