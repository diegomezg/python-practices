def fisrt_char(char):
    if char.isupper():
        return True
    return False


result = fisrt_char('C')
print(result)


def words(string):
    res = len(string.split())
    return res


result = words('Hello world')
print(result)


def reverse(x):
    return x[::-1]


result = reverse("Tengo mucho sueño me quiero morirme")
print(result)


def last_upper(text):
    reverse = text[::-1]
    words = reverse.split()
    title = []
    for i in words:
        title.append(i.title())
    result = ' '.join(title)
    final = result[::-1]
    return final


result = last_upper('como estas me llamo juan')
print(result)


def to_list(string):
    result = string.split()
    return result


result = to_list('A chuchita la boxearon')
print(result)
