from pickle import NONE

'''
class Fila:
    def __init__(self, cardTable = [NONE], playerTable = [NONE]):
        self._cardTable = cardTable
        self.playerTable = playerTable
    
    def removeElementTable(cls):
        cls.playerTable.pop(0)
        return cls.playerTable
    def elementoNotTable(cls):
        element = cls.playerTable.pop(0)
        cls.playerTable.append(element)
        return cls.playerTable
    def cardsTable(cls):
        element = cls._cardTable.pop(0)
        cls._cardTable.append(element)
        return cls._cardTable
'''
numberParty = int(input())
listTable = input().split(" ")

for x in range(numberParty):
    conStop = 0
    listIntegrant = []

    while conStop != '-1':
        conStop = input()
        integrant = conStop.split(" ")
        listIntegrant.append(integrant)
    for x in range (5):
        print(listIntegrant[x])
'''
    for x in range (len(listIntegrant)):
        if listTable == listIntegrant[x][0]:
            Fila.removeElementTable(listIntegrant[x][0])
        elif listTable != listIntegrant[x][0]:
            Fila.elementoNotTable(listIntegrant[x][0])

    for x in range (len(listIntegrant)):
        if len(listIntegrant[x]) > 0:
            print(x)
'''
  
    

    

    




    