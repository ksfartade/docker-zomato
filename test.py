import time

def cal(a, b):
    print("Calculating...")
    time.sleep(2)
    return a + b

def main():
    print("Starting the calculation...")
    result = cal(5, 3)
    print(f"The result is: {result}")