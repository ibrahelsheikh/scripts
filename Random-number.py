# Generate random numbers 0 to 200

import random
import time


def main():
    for i in range(10):
        print(random.randint(0, 200))
        time.sleep(1)


if __name__ == "__main__":
    main()
