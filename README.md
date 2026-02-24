# Temperature-Monitoring_ChetnaSingh_202501100700061_B
Problem Statement:
Build a Python code to display messages according to the temperature received from an assumed IoT system.
Accept max and min limit temperature.
Generate random values for temperature at every 2 second interval.
Compare with the limits to display appropriate value.
<img width="2736" height="423" alt="image" src="https://github.com/user-attachments/assets/5b36a4dc-d5cb-40e5-bd6b-5917dc8a8941" />

Approach : 
The program accepts minimum and maximum temperature values from the user.

It uses the random module to generate random temperature values between 0 and 100.

The program runs in a loop and generates a new temperature every 2 seconds using time.sleep(2).

Each generated temperature is compared with the minimum and maximum limits.

If the temperature exceeds the maximum limit, an alert message is displayed indicating the temperature is too high.

If the temperature is below the minimum limit, an alert message is displayed indicating the temperature is too low.

If the temperature is within the limits, a message is displayed indicating it is within the acceptable range.


Sample Output :
Enter minimum temperature: 10
Enter maximum temperature: 87

Current Temperature: 84
Temperature is within acceptable limit

Current Temperature: 3
Alert: Temperature is too low

Current Temperature: 53
Temperature is within acceptable limit

Current Temperature: 34
Temperature is within acceptable limit

Current Temperature: 28

