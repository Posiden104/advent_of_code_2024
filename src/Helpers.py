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
        time_format = f"{elapsed_time:.6f} s"
    return result, time_format

def execute(func, title):
    result, time = time_it(func)
    print("=========================================")
    print(f"{title}") if title else print('')
    print(f"Result: {result}")
    print(f"Operation took {time}.")
    print("=========================================")