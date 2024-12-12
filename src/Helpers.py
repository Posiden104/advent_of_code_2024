import time

def read_input(day: int, example: bool, oneline: bool):
    with open(f"src/input/day{day}_input{'_example' if example else ''}.txt", 'r') as file:
        if oneline: 
            return file.read().replace('\n', '')
        else:
            return [line.strip() for line in file.readlines()]

def time_it(func): 
    start_time = time.perf_counter()
    result = func()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    time_format = ''
    if elapsed_time < 1:
        elapsed_time *= 1000
        time_format = f"{elapsed_time:.6f} ms"
    elif elapsed_time > 60:
        elapsed_time /= 60
        time_format = f"{elapsed_time:.6f} mins"
    else:
        time_format = f"{elapsed_time:.6f} sec"
    return result, time_format

def execute(func, title):
    result, time = time_it(func)
    print("=========================================")
    print(f"{title}") if title else print('')
    print(f"Result: {result}")
    print(f"Operation took {time}.")
    print("=========================================")




class TrinaryNumber:
    def __init__(self, value):
        if isinstance(value, str):
            self.value = int(value, 3)
        elif isinstance(value, int):
            self.value = value
        else:
            raise ValueError("Value must be a trinary string or an integer")

    def __str__(self):
        return self.to_trinary()

    def to_trinary(self):
        if self.value == 0:
            return '0'
        num = self.value
        trinary = ''
        while num > 0:
            trinary = str(num % 3) + trinary
            num //= 3
        return trinary

    def trin(self):
        return '0t' + self.to_trinary()

    def to_int(self):
        return self.value

    def lsb(self):
        return int(self.to_trinary()[-1])

    def __add__(self, other):
        if isinstance(other, TrinaryNumber):
            return TrinaryNumber(self.value + other.value)
        elif isinstance(other, int):
            return TrinaryNumber(self.value + other)
        else:
            raise ValueError("Can only add TrinaryNumber or integer")

    def __iadd__(self, other):
        if isinstance(other, TrinaryNumber):
            self.value += other.value
        elif isinstance(other, int):
            self.value += other
        else:
            raise ValueError("Can only add TrinaryNumber or integer")
        return self

    def __sub__(self, other):
        if isinstance(other, TrinaryNumber):
            return TrinaryNumber(self.value - other.value)
        elif isinstance(other, int):
            return TrinaryNumber(self.value - other)
        else:
            raise ValueError("Can only subtract TrinaryNumber or integer")
        
    def __mul__(self, other):
        if isinstance(other, TrinaryNumber):
            return TrinaryNumber(self.value * other.value)
        elif isinstance(other, int):
            return TrinaryNumber(self.value * other)
        else:
            raise ValueError("Can only multiply TrinaryNumber or integer")

    def __eq__(self, other):
        if isinstance(other, TrinaryNumber):
            return self.value == other.value
        elif isinstance(other, int):
            return self.value == other
        else:
            return False

    def __le__(self, other):
        if isinstance(other, TrinaryNumber):
            return self.value <= other.value
        elif isinstance(other, int):
            return self.value <= other
        else:
            raise ValueError("Can only compare TrinaryNumber or integer")

    def __lshift__(self, other):
        if isinstance(other, int):
            return TrinaryNumber(self.value * (3 ** other))
        else:
            raise ValueError("Can only left shift by an integer")

    def __rshift__(self, other):
        if isinstance(other, int):
            return TrinaryNumber(self.value // (3 ** other))
        else:
            raise ValueError("Can only right shift by an integer")
        
    def __and__(self, other):
        if isinstance(other, TrinaryNumber):
            trinary1 = self.to_trinary()
            trinary2 = other.to_trinary()
        elif isinstance(other, int):
            trinary1 = self.to_trinary()
            trinary2 = TrinaryNumber(other).to_trinary()
        else:
            raise ValueError("Can only AND with TrinaryNumber or integer")

        # Pad the shorter trinary number with leading zeros
        max_len = max(len(trinary1), len(trinary2))
        trinary1 = trinary1.zfill(max_len)
        trinary2 = trinary2.zfill(max_len)

        # Perform the AND operation digit by digit
        result = ''
        for digit1, digit2 in zip(trinary1, trinary2):
            result += str(min(int(digit1), int(digit2)))

        return TrinaryNumber(result)