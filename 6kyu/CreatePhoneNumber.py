def create_phone_number(n):
    phone = '('
    for i in n[:3]:
        phone += str(i)
    phone += ') '
    for i in n[3:6]:
        phone += str(i)
    phone += '-'
    for i in n[6:]:
        phone += str(i)
    return str(phone)

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))