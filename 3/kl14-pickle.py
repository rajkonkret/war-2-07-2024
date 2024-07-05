import pickle

# serializacja i deserializacja

lista = [1, 2, 3, 4, 5]
print(type(lista))  # <class 'list'>

# with - kontekst manager  - ułatwia bezpieczną prace np.: z plikami
with open('lista.txt', 'w') as f:
    f.writelines(str(lista))

with open('lista.txt', "r") as fh:
    lines = fh.read()

print(lines)  # [1, 2, 3, 4, 5]
print(lines[0])  # [
print(type(lines))  # <class 'str'>

# serializacja - zamiana obiektu na bajty
# wb  - zapis bajtowy
with open('lista.pickle', 'wb') as fh:
    pickle.dump(lista, fh)

# deserializacja
with open('lista.pickle', 'rb') as f:
    p = pickle.load(f)

print(p)  # [1, 2, 3, 4, 5]
print(type(p))  # <class 'list'>

print(p[0])  # 1

lista_ser = pickle.dumps(lista)
print(lista_ser)
# b'\x80\x04\x95\x0f\x00\x00\x00\x00\x00\x00\x00]\x94(K\x01K\x02K\x03K\x04K\x05e.'
print(pickle.loads(lista_ser))  # [1, 2, 3, 4, 5]
