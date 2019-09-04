class NativeDictionary:
    def __init__(self, sz):
        self.size = sz
        self.slots = [None] * self.size # массив для значений
        self.values = [None] * self.size # массив для ключей

    def hash_fun(self, key):
        if self.is_key(key) is False:
            if self.values.count(None) != 0:
                return self.values.index(None)
            else:
                return None 
        else:
            return True
        # в качестве key поступают строки!
        # всегда возвращает корректный индекс слота

    def is_key(self, key):
         # возвращает True если ключ имеется,
        for i in range(self.size):
            if self.values[i] == key:
                return True
        return False # иначе False

    def put(self, key, value):
        slot = self.hash_fun(key)
        if slot is not None and slot is not True:
            self.values[slot] = key
            self.slots[slot] = value
        else:
            return None
        pass
         # гарантированно записываем 
         # значение value по ключу key

    def get(self, key):
        for i in range(self.size):
            if self.values[i] == key:
                return self.slots[i]
         # возвращает value для key, 
         # или None если ключ не найден
        return None