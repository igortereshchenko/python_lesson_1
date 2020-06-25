class Human:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

        self.__travels = dict()
    #                             {
    #                                 'IT': {
    #                                        '10.08.2000': 'IBIS',
    #                                        '10.08.2010': 'HILTON',
    #                                       },
    #
    #                                 'DE': {
    #                                        '10.08.2019': 'IBIS',
    #                                       }
    #
    #                              }


    def getName(self):
        """

        :return: user name
        """
        return self.__name

    def getAge(self):
        """

        :return: user age
        """
        return self.__age


    def addHotel(self,country,data,hotel_name):
        """

        :param country: code two capital letters
        :param data: time of visiting
        :param hotel_name: name
        :return: None
        """

        if country in self.__travels.keys():
            self.__travels[country].update({data: hotel_name})
        else:
            self.__travels[country] = {data: hotel_name}


    def travelInfo(self):
        """

        :return: None, Print user travel info
        """
        print(self.__travels)


    def toList(self):

        list= []

        for country in self.__travels:

            for data, hotel in self.__travels[country].items():

                list.append([self.__name, self.__age, country, data, hotel])

        return list



print('Hello from human.py')


if __name__ == "__main__":
    # test class
    human = Human('igor', 32)
    human.travelInfo()
    print('Hello from test')