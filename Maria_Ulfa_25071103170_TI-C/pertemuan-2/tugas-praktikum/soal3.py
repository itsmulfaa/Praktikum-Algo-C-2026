def jumlah_digit(n):
    if n < 10:
        return n
    else:
        return (n % 10) + jumlah_digit(n//10)

print(jumlah_digit (1234))
