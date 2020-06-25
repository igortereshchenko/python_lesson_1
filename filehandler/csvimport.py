import csv
from human.Human import Human


def importHumans(path):
    """

    :param path: path to csv file
    :return: list of Humans
    """

    persons = dict()

    with open(path,'r') as file:
        reader = csv.reader(file)
        next(reader, None)

        for line in reader:

            if line[0] not in persons.keys():
                persons[line[0]] = Human(line[0], line[1])


            current_person = persons[line[0]]
            current_person.addHotel(line[2], line[3], line[4])




    return persons
