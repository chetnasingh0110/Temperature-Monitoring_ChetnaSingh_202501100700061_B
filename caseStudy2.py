# Temperature Monitoring System

import random
import time

# Input limits
min_temp = float(input("Enter minimum temperature: "))
max_temp = float(input("Enter maximum temperature: "))

# Generate temperature every 2 seconds (5 times)
for i in range(5):

    temp = random.randint(0, 100)

    print("\nCurrent Temperature:", temp)

    if temp > max_temp:
        print("Alert: Temperature is too high")

    elif temp < min_temp:
        print("Alert: Temperature is too low")

    else:
        print("Temperature is within acceptable limit")

    time.sleep(2)