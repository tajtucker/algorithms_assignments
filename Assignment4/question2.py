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
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return "Stack is empty"
        removed_data = self.top.data
        self.top = self.top.next
        return removed_data

    def peek(self):
        if self.top is None:
            return "Stack is empty"
        return self.top.data

    def is_empty(self):
        return self.top is None

    def print_stack(self):
        if self.top is None:
            print("Stack is empty")
        else:
            current = self.top
            while current:
                print(current.data)
                current = current.next

    def search(self, car_id):
        current = self.top
        while current:
            if current.data["id"] == car_id:
                return "Found"
            current = current.next
        return "Not Found"


stack = Stack()

stack.push(car1)
stack.push(car2)
stack.push(car3)
stack.push(car4)
stack.push(car5)
stack.push(car6)
stack.push(car7)
stack.push(car8)
stack.push(car9)


num = 0
while num != 9:
    print()
    print("Pick a method:\n"
          "1: Push\n"
          "2: Pop\n"
          "3: Peek\n"
          "4: Search by ID\n"
          "5: Check if Empty\n"
          "6: Print Stack\n"
          "9: Exit")
    print()

    num = int(input())

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

        stack.push(data)
        print("Pushed onto stack")

    elif num == 2:
        print(stack.pop())

    elif num == 3:
        print(stack.peek())

    elif num == 4:
        print("Enter ID:")
        car_id = int(input())
        print(stack.search(car_id))

    elif num == 5:
        print(stack.is_empty())

    elif num == 6:
        stack.print_stack()

    elif num == 9:
        print("Exiting...")

    else:
        print("Invalid choice")