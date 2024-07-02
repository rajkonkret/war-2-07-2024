# wyjątki
# błedy podczas działąnia programu
try:
    # print("12" + 34)
    print("A")
except Exception as e:
    print("Błąd", e)  # Błąd can only concatenate str (not "int") to str
else:
    print("Wykonuje się gdy nie ma błedu")
finally:
    print("Wykonuje się zawsze")

# A
# Wykonuje się gdy nie ma błedu
# Wykonuje się zawsze
