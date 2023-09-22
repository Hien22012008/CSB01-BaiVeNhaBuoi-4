n = int(input("Nhập số n:"));

def totalDigitsOfNumber(n):
    result = 0;
    while (n > 0):
        result = result + n % 10;
        n = int(n / 10);
    return result;
print("Sum of digits of", n , "=", totalDigitsOfNumber(n));