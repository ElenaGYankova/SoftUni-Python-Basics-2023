degrees = float(input())
if degrees >= 26.00 and degrees <= 35.00:
    print("Hot")
else:
    if degrees >= 20.10 and degrees <= 25.9:
        print("Warm")
    else:
        if degrees >= 15 and degrees <= 20:
            print("Mild")
        else:
            if degrees >= 12 and degrees <= 14.9:
                print("Cool")
            else:
                if degrees >= 5 and degrees <= 11.9:
                    print("Cold")
                else:
                    print("unknown")