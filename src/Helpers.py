import time

def read_input(day: int, example: bool, oneline: bool):
    with open(f"src/input/day{day}_input{'_example' if example else ''}.txt", 'r') as file:
        if oneline: 
            return file.read().replace('\n', '')
        else:
            return file.readlines()


def time_it(func): 
    start_time = time.perf_counter()
    result = func()
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    elapsed_time *= 1000
    print("=========================================")
    print(f"Result: {result}")
    print(f"Operation took {elapsed_time:.6f} ms.")
    print("=========================================")

