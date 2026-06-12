#program for Vehicle Registration Verification System 
vehicle_numbers = [
    "MH12AB4589", "DL05XY9988", "KA03PQ1234", "UP14CD5678",
    "MH20EF9876", "DL08GH4567", "KA09IJ2345", "UP32KL7890",
    "MH11MN1122", "DL07OP3344", "KA05QR5566", "UP16ST7788",
    "MH18UV9900", "DL09WX2233", "KA01YZ4455", "UP21AA6677",
    "MH22BB8899", "KA07CC1010", "UP30DD2020", "DL10EE3030"
]

state_count = {}

for reg in vehicle_numbers:
    print("\nRegistration Number:", reg)

    # Extract Parts
    state_code = reg[:2]
    district_code = reg[2:4]
    series = reg[4:6]
    vehicle_no = reg[6:]

    # Count Letters and Digits
    letters = 0
    digits = 0

    for ch in reg:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digits += 1

    # Validation
    valid = (
        len(reg) == 10 and
        reg[:2].isalpha() and
        reg[2:4].isdigit() and
        reg[4:6].isalpha() and
        reg[6:].isdigit()
    )

    print("State Code:", state_code)
    print("District Code:", district_code)
    print("Series:", series)
    print("Vehicle Number:", vehicle_no)
    print("Letters:", letters)
    print("Digits:", digits)

    if valid:
        print("Valid Registration")
    else:
        print("Invalid Registration")

    # State-wise Count
    if state_code in state_count:
        state_count[state_code] += 1
    else:
        state_count[state_code] = 1

print("\n========== STATE-WISE REPORT ==========")

for state, count in state_count.items():
    print(state, "->", count, "Vehicles")