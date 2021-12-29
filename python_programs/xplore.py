class Blood:

    def __init__(self, bloodGroup, unitInHand):
        self.bloodGroup = bloodGroup
        self.unitInHand = unitInHand


class bloodBank:

    def __init__(self, bloodList):
        self.bloodList = bloodList

    def isBloodAvailable(self, bloodGroup, unitsReq):
        for i in bloodList:
            if i.bloodGroup == bloodGroup and i.unitInHand >= unitsReq:
                return True
        return False

    def findMinBlockStock(self):
        bloodl = []
        bloodmin = []
        for i in self.bloodList:
            bloodl.append(i.unitInHand)
        minstock = min(bloodl)
        for i in self.bloodList:
            if i.unitInHand == minstock:
                bloodmin.append(i.bloodGroup)
        return bloodmin


if __name__ == "__main__":
    n = int(input())
    bloodList = []
    for i in range(n):
        bloodGroup = input()
        unitInHand = int(input())
        bloodList.append(Blood(bloodGroup, unitInHand))
    x1 = input().upper()
    x2 = int(input())
    r = bloodBank(bloodList).isBloodAvailable(x1, x2)
    if r == True:
        print("Blood Available.")
    else:
        print("Blood not Available")
    w = bloodBank(bloodList).findMinBlockStock()
    for i in w:
        print(i)

'''
4
A
10
B
5
O
3
AB
8
AB
6
'''
