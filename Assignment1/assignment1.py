class Set:
    def __init__(self, arr=None):
        self.elements = []

        if arr is not None:
            for x in arr:
                self.addElement(x)
    
    def isElement(self, x): 
        return x in self.elements
    
    def addElement(self, x):
        if not self.isElement(x):
            self.elements.append(x)
    
    def union(self, other):
        result = Set()
        for x in self.elements:
            result.addElement(x)
        for x in other.elements:
            result.addElement(x)
        return result
    
    def intersection(self, other):
        result = Set()
        for x in self.elements:
            if other.isElement(x):
                result.addElement(x)
        return result
    
    def difference(self, other):
        result = Set()
        for x in self.elements:
            if not other.isElement(x):
                result.addElement(x)
        return result
    
    def subset(self, other):
        for x in self.elements:
            if not other.isElement(x):
                return False
        return True
    
    def isEmpty(self):
        if len(self.elements) == 0:
            return True
        return False
    
    def isEqual(self, other):
        for x in self.elements:
            if not other.isElement(x):
                return False
        for x in other.elements:
            if not self.isElement(x):
                return False
        return True

    def getCardinality(self):
        num = 0
        for x in self.elements:
            num += 1
        return num
    
    def removeElement(self, x):
        if self.isElement(x):
            self.elements.remove(x)
    
    def clear(self):
        self.elements = []
    
    def toArray(self):
        return self.elements[:]
    
    def print(self):
        print(self.elements)

A = Set([1, 2, 3])
B = Set([3, 4, 5])

while True:
    print("\nMENU")
    print("1. Print sets")
    print("2. Union")
    print("3. Intersection")
    print("4. Difference (A - B)")
    print("5. Check if A is subset of B")
    print("6. isEmpty")
    print("7. isElement")
    print("8. isEqual")
    print("9. getCardinality")
    print("10. addElement to A")
    print("11. removeElement from A")
    print("12. clear A")
    print("13. toArray A")
    print("0. Exit")

    choice = input("Choose: ")

    if choice == "0":
        break

    elif choice == "1":
        print("A:", A.elements)
        print("B:", B.elements)

    elif choice == "2":
        C = A.union(B)
        print("Union:", C.elements)

    elif choice == "3":
        C = A.intersection(B)
        print("Intersection:", C.elements)

    elif choice == "4":
        C = A.difference(B)
        print("Difference:", C.elements)

    elif choice == "5":
        print(A.subset(B))

    elif choice == "6":
        print(A.isEmpty())

    elif choice == "7":
        print(A.isElement(2))

    elif choice == "8":
        print(A.isEqual(B))

    elif choice == "9":
        print(A.getCardinality())

    elif choice == "10":
        A.addElement(4)
        print("Updated A:", A.elements)

    elif choice == "11":
        A.removeElement(2)
        print("Updated A:", A.elements)

    elif choice == "12":
        A.clear()
        print("A cleared")

    elif choice == "13":
        print(A.toArray())

    else:
        print("Invalid option")