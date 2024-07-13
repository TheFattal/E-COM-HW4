iq_num1: int = int(input("Please insert an IQ number:"))
iq_sum1: int = 0
iq_count1: int = 0
iq_avg1: int = 0

while 30 <= iq_num1 <= 300:
    iq_sum1 += iq_num1
    iq_count1 = iq_count1 + 1
    iq_num1: int = int(input("Please insert another IQ number:"))

# I'm checking for inputs, Because I don't want to divide with 0 (DIVISION-ERROR):
if iq_count1 != 0:
    iq_avg1: float = iq_sum1 / iq_count1
    print(f"The group IQ average is: {iq_avg1}")
else:
    print("You haven't provide any correct IQ grade sir.")

print("one year of python training has been completed...")

iq_num2: int = int(input("Please insert an IQ number:"))
iq_sum2: int = 0
iq_count2: int = 0
iq_avg2: int = 0

while 30 <= iq_num2 <= 300:
    iq_sum2 += iq_num2
    iq_count2 = iq_count2 + 1
    iq_num2: int = int(input("Please insert another IQ number:"))

# I'm checking for inputs, Because I don't want to divide with 0 (DIVISION-ERROR):
if iq_count2 != 0:
    iq_avg2: float = iq_sum2 / iq_count2
    print(f"The group IQ NEW average is: {iq_avg2}")
else:
    print("You haven't provide any correct IQ grade sir...")

print(f"The IQ average has improved by {iq_avg2 - iq_avg1} Points!")
