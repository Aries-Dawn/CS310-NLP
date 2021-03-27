while True:
    try:
        up = float(input('upper:'))
        break
    except Exception:
        continue
while True:
    try:
        low = float(input('lower:'))
        break
    except Exception:
        continue
while True:
    try:
        high = float(input('height:'))
        break
    except Exception:
        continue
print("area is : {:.2f}".format((up + low) * high / 2))
