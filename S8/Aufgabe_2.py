# class Raum:
#     def __init__(self, id, raumnummer, plaetze):
#         self.raumnummer = raumnummer
#         self.plaetze = plaetze
#         self.id = id #unique
#
#     def __str__(self):
#         return f'Raum(nummer={self.raumnummer}, sp={self.plaetze})'
#
#     """
#     def __eq__(self, other):
#         return self.id == other.id
#     """
#
#     def __eq__(self, other):
#         return self.raumnummer == other.raumnummer
#
#     def plaetzee(self):
#         return self.plaetze
#
#
# """
# PUNKT B)
# """
# class Rechnerraum(Raum):
#     def __init__(self, id, raumnummer, plaetze, betriebssystem):
#         super().__init__(id, raumnummer, plaetze)
#
#         self.betriebssystem = betriebssystem
#
#     def __str__(self):
#         return f'Rechnerraum(betriebssystem={self.betriebssystem})'
#
#     # def plaezte(self):
#     #     return self.plaetze
#
#
# class Gebaude:
#     def __init__(self, klassenraume):
#         self.klassenraume = klassenraume
#
#     def wievielPlatz(self):
#         for klassenraum in self.klassenraume:
#             print(klassenraum.plaetzee())
#
#     def read_data(self):
#         rooms_list = []
#         for klassenraum in self.klassenraume:
#             rooms_list.append(klassenraum)
#         print(rooms_list)
#     def write_data(self):
#         with open("rooms.txt", "w") as f:
#             pass
# def main():
#     discovery = Raum(1, 'discovery', 25)
#     saturn = Raum(2, 'saturn', 30)
#     socrate = Rechnerraum(1, 'socrate', 60, 'windows')
#     #print(discovery)
#
#     #print(saturn == discovery)
#
#     #print(socrate)
#
#     gebaude = Gebaude([discovery, saturn, socrate])
#     gebaude.wievielPlatz()
#
#     gebaude.read_data()
#
# main()


class Room:
    def __init__(self, number : str, places : int):
        self.number = number
        self.places = places

    def __eq__(self, other):
        return self.number == other.number and self.places == other.places

    def __str__(self):
        return f"Number: {self.number}, Places: {self.places}"

class ComputerRoom(Room):
    os = ("Unix", "Linux", "MacOS", "Windows")

    def __init__(self, number: str, places: int, operatingSystem: str):
        super().__init__(number, places)
        self.operatingSystem = operatingSystem

        if operatingSystem not in ComputerRoom.os:
            raise AttributeError("Operating system does not exist!")


    def __eq__(self, other):
        return self.number == other.number and self.places == other.places and self.operatingSystem == self.operatingSyste

    def __str__(self):
        return f"Number: {self.number}, Places: {self.places}, OS: {self.operatingSystem}"



class Building:
    def __init__(self, roomList: list):
        self.roomList = roomList

    def numberOfPlaces(self, roomNumber: int):
        for r in self.roomList:
            if r.number == roomNumber: #aici este vizibil number si places pentru ca iterezi cu for-ul prin r care este
                                        #un obiect de tip ROOM care are attributele number si places
                return r.places

    def readData(self):
        with(open("rooms.txt") as f):
            for line in f:
                self.roomList.append(line)

    def writeData(self):
        f = open("rooms.txt", "w")

        for r in self.roomList:
            f.write(str(r) + "\n")

        f.close()



def main():
    l = [Room("12", 3), Room("123", 6), Room("121", 9), Room("1215", 7), ComputerRoom("1", 7, "Linux")]
    b = Building(l)


    b.writeData()

    b2 = Building([])
    b2.readData()

    for e in b2.roomList:
        print(e, end="")
main()