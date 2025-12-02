import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        dt = end - start
        print(f"'{func.__name__}': {dt:.6f} sec")
        return result

    return wrapper
