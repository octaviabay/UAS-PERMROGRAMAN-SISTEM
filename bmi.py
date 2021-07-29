def hitung_BMI(berat,tinggi):
    BMI = berat/tinggi*tinggi

    if BMI > 22.9:
        return "OVERWEIGHT"
    elif BMI < 18.5:
        return "UNDERWEIGHT"
    else:
        return "NORMAL"

berat = float(input("Masukkan berat badan (kg) : "))
tinggi = float(input("Masukkan tinggi badan (cm) : "))

result = hitung_BMI(berat,tinggi)
print("BMI anda adalah : ",result)