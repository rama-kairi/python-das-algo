# Implement a hash map with `get`, `set`, and `delete` methods.

class HashMap:
    def __init__(self):
        self.map = [None] * 10000

    def _hash(self, key):
        hash = sum(ord(char) for char in str(key))
        return hash % len(self.map)

    def get(self, key):
        index = self._hash(key)
        if self.map[index] is not None:
            bucket = self.map[index]
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    return bucket[i][1]
        return None

    def set(self, key, value):
        index = self._hash(key)
        if self.map[index] is None:
            self.map[index] = [(key, value)]
        else:
            bucket = self.map[index]
            for i in range(len(bucket)):
                if bucket[i][0] == key:
                    bucket[i] = (key, value)
                    return
            bucket.append((key, value))

    def delete(self, key):
        index = self._hash(key)
        if self.map[index] is None:
            return
        bucket = self.map[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket.pop(i)
                return

    def print_map(self):
        map = "".join(str(item) + "\n" for item in self.map if item is not None)
        print(map)


if __name__ == "__main__":
    hm = HashMap()
    hm.set("a", 1)
    hm.set("b", 2)
    hm.set("c", 3)
    hm.set("d", 4)
    hm.set("e", 5)
    hm.set("f", 6)
    hm.set("g", 7)
    hm.set("h", 8)
    hm.set("i", 9)
    hm.set("j", 10)
    hm.set("k", 11)
    hm.set("l", 12)
    hm.set("m", 13)
    hm.set("n", 14)
    hm.set("o", 15)
    hm.set("p", 16)
    hm.set("q", 17)
    hm.set("r", 18)
    hm.set("s", 19)
    hm.set("t", 20)
    hm.set("u", 21)
    hm.set("v", 22)
    hm.set("w", 23)
    hm.set("x", 24)
    hm.set("y", 25)
    hm.set("z", 26)
    hm.set("z", 99)
    hm.print_map()
    print(hm.get("a"))
    print(hm.get("b"))
    print(hm.get("c"))
    print(hm.get("d"))
    print(hm.get("e"))
    print(hm.get("f"))
    print(hm.get("g"))
    print(hm.get("h"))
    print(hm.get("i"))
    print(hm.get("j"))
    print(hm.get("k"))
    print(hm.get("l"))
    print(hm.get("m"))
    print(hm.get("n"))
    print(hm.get("o"))
    print(hm.get("p"))
    print(hm.get("q"))
    print(hm.get("r"))
    print(hm.get("s"))
    print(hm.get("t"))
    print(hm.get("u"))
    print(hm.get("v"))
    print(hm.get("w"))
    print(hm.get("x"))
    print(hm.get("y"))
    print(hm.get("z"))
    hm.delete("a")
    hm.delete("b")
    hm.delete("c")
    hm.delete("d")
