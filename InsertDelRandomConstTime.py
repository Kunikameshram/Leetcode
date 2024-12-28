class RandomizedSet:

    def __init__(self):
        self.random_map = {}
        self.random_list = []

    def insert(self, val: int) -> bool:

        if val in self.random_map.keys():
            return False
        length = len(self.random_list)
        self.random_map[val] = length
        self.random_list.append(val)

        return True

    def remove(self, val: int) -> bool:

        if val in self.random_map.keys(): 
            if len(self.random_map) > 1:
                index = self.random_map.pop(val)
                item = self.random_list.pop()
                if item != val:
                    self.random_list[index] = item
                    self.random_map[item] = index
            else:
                index = self.random_map.pop(val)
                item = self.random_list.pop()
            return True

        return False

    def getRandom(self) -> int:
        length = len(self.random_list) - 1
        r = random.randint(0, length)
        return self.random_list[r]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()