def FizzBuzz(num):
    for x in range(1, num+1):
        if x % 6 == 0 and x % 4 == 0:
            print("FizzBuzz")
        elif x % 4 == 0:
            print("Fizz")
        elif x % 6 == 0:
            print("Buzz")

        else:
            print(x)


def sumOfTwo(a, b, v):
    for num1 in a:
        for num2 in b:
            if num1 + num2 == v:
                return True
    return False

def sumOfInt(string):
    x = string.split()
    digits = []
    for word in x:
        if word.isdigit() == True:
            digits.append(int(word))
    print("Nuber of digits: " , len(digits))
    print(sum(digits))

def starTriangle(rows):
    y = 1
    z = 1
    for _ in range(rows):
        print(" " * (rows - z) +"*" * y)
        y += 2
        z += 1



class Hash_map:
    def __init__(self):
        self.size = 64
        self.map = [None] * self.size

    def hashFunction(self, key):
        hash = 0
        for char in str(key):
            hash += ord(char)
        return hash % self.size

    def add(self, key, value):
        key_hash = self.hashFunction(key)
        key_value = [key, value]

        if self.map[key_hash] is None:
            self.map[key_hash] = list([key_value])
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] =  value
                    return True
            self.map[key_hash].append(key_value)
            return True

    def get(self, key):
        key_hash = self.hashFunction(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        key_hash = self.hashFunction(key)
        if self.map[key_hash] is None:
            return False
        for i in range(0, len(self.map[key_hash])):
            if self.map[key_hash][i][0] == key:
                self.map[key_hash].pop(i)
                return True

    def printHash(self):
        for item in self.map:
            if item is not None:
                print(str(item))

h = Hash_map()
h.add("henol", "steve")
h.printHash()
