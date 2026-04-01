car1 = {"id": 55, "make": "BMW", "model": "228i", "year": 2008, "mileage": 122510, "price": 7800}
car2 = {"id": 65, "make": "Honda", "model": "Accord", "year": 2011, "mileage": 93200, "price": 9850}
car3 = {"id": 45, "make": "Toyota", "model": "Camry", "year": 2010, "mileage": 85300, "price": 9500}
car4 = {"id": 25, "make": "Honda", "model": "Civic", "year": 2010, "mileage": 86400, "price": 9100}
car5 = {"id": 15, "make": "Mazda", "model": "Zoom 3", "year": 2013, "mileage": 72450, "price": 8950}
car6 = {"id": 35, "make": "Mazda", "model": "Cx7", "year": 2009, "mileage": 102200, "price": 7300}
car7 = {"id": 5, "make": "Toyota", "model": "Corolla", "year": 2013, "mileage": 68900, "price": 10100}
car8 = {"id": 75, "make": "Ford", "model": "Mustang", "year": 2008, "mileage": 112500, "price": 13200}
car9 = {"id": 95, "make": "Mercedes Benz", "model": "C250", "year": 2012, "mileage": 65300, "price": 17300}

class Node:
    def __init__(self, data):
        self.next = None
        self.prev = None
        self.data = data

class DoubleLinkedList: 
    def __init__(self): 
        self.head = None 
        self.tail = None
    
    def append_head(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
    
    def append_tail(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
    
    def remove_head(self):
        if self.head == None:
            pass
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
    
    def remove_tail(self):
        if self.tail == None:
            pass
        elif self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
    
    def search(self, data):
        current = self.head
        while current:
            if current.data["id"] == data:
                return "Found"
            else:
                current = current.next
        return "Not Found"
    
    def delete(self, data):
        current = self.head
        while current:
            if self.head == self.tail and current.data["id"] == data: #  Single Node Case
                self.head = None
                self.tail = None
                return "Deleted"
            elif current == self.head: #  Head = Data Case
                if current.data["id"] == data:
                    self.head = current.next
                    self.head.prev = None
                    return "Deleted"
                else:
                    current = current.next
            elif current == self.tail: #  Tail = Data Case 
                if current.data["id"] == data:
                    self.tail = current.prev
                    self.tail.next = None
                    return "Deleted"
                else:
                    current = current.next
            elif current.data["id"] == data:  #  Middle = Data Case
                current.next.prev = current.prev
                current.prev.next = current.next
                return "Deleted"
            else: #  Move Forward
                current = current.next
        return "Not Found"
    
    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
    

dll = DoubleLinkedList()
dll.append_tail(car1)
dll.append_tail(car2)
dll.append_tail(car3)
dll.append_tail(car4)
dll.append_tail(car5)
dll.append_tail(car6)
dll.append_tail(car7)
dll.append_tail(car8)
dll.append_tail(car9)

num = 0
while num != 9:
    print()
    print("Pick a method:\n" 
    "1: Append Head\n"
    "2: Append Tail\n"
    "3: Remove Head\n"
    "4: Remove Tail\n"
    "5: Search\n"
    "6: Delete\n"
    "7: Print List\n"
    "9: To Exit")
    print()
    num = int(input())
    print()

    if num == 1:
        print("Enter ID:")
        car_id = int(input())

        print("Enter Make:")
        make = input()

        print("Enter Model:")
        model = input()

        print("Enter Year:")
        year = int(input())

        print("Enter Mileage:")
        mileage = int(input())

        print("Enter Price:")
        price = int(input())

        data = {
            "id": car_id,
            "make": make,
            "model": model,
            "year": year,
            "mileage": mileage,
            "price": price
        }

        dll.append_head(data)
        print("Done")

    elif num == 2:
        print("Enter ID:")
        car_id = int(input())

        print("Enter Make:")
        make = input()

        print("Enter Model:")
        model = input()

        print("Enter Year:")
        year = int(input())

        print("Enter Mileage:")
        mileage = int(input())

        print("Enter Price:")
        price = int(input())

        data = {
            "id": car_id,
            "make": make,
            "model": model,
            "year": year,
            "mileage": mileage,
            "price": price
        }

        dll.append_tail(data)
        print("Done")
    
    elif num == 3:
        dll.remove_head()
        print("Done")
    
    elif num == 4:
        dll.remove_tail()
        print("Done")
    
    elif num == 5:
        print("Enter ID:")
        data = int(input())
        print()
        print(dll.search(data))
    
    elif num == 6:
        print("Enter ID:")
        data = int(input())
        print(dll.delete(data))
    
    elif num == 7:
        dll.print_list()