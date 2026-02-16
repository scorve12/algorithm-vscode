import sys
import math

case = 1
for line in sys.stdin:
    data = list(map(float, line.split()))
    if data[1] == 0:
        break

    # 지름, 회전수, 시간(초단위 실수)
    diameter, rotaion, seconds = data

    distance = (diameter * math.pi * rotaion) / (12*5280)

    MPH = distance / (seconds / 3600)

    print(f"Trip #{case}: {distance:.2f} {MPH:.2f}")

    case += 1