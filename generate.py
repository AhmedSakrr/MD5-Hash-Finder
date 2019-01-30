from hashlib import md5


dictionary = {
    '1': open('hash/1.txt', 'a', encoding='utf-8', errors='ignore'),
    '2': open('hash/2.txt', 'a', encoding='utf-8', errors='ignore'),
    '3': open('hash/3.txt', 'a', encoding='utf-8', errors='ignore'),
    '4': open('hash/4.txt', 'a', encoding='utf-8', errors='ignore'),
    '5': open('hash/5.txt', 'a', encoding='utf-8', errors='ignore'),
    '6': open('hash/6.txt', 'a', encoding='utf-8', errors='ignore'),
    '7': open('hash/7.txt', 'a', encoding='utf-8', errors='ignore'),
    '8': open('hash/8.txt', 'a', encoding='utf-8', errors='ignore'),
    '9': open('hash/9.txt', 'a', encoding='utf-8', errors='ignore'),
    '0': open('hash/0.txt', 'a', encoding='utf-8', errors='ignore'),
    'a': open('hash/a.txt', 'a', encoding='utf-8', errors='ignore'),
    'b': open('hash/b.txt', 'a', encoding='utf-8', errors='ignore'),
    'c': open('hash/c.txt', 'a', encoding='utf-8', errors='ignore'),
    'd': open('hash/d.txt', 'a', encoding='utf-8', errors='ignore'),
    'e': open('hash/e.txt', 'a', encoding='utf-8', errors='ignore'),
    'f': open('hash/f.txt', 'a', encoding='utf-8', errors='ignore')
}


if __name__ == "__main__":
    name = input('Password file: ')

    with open(name, 'r', encoding='utf-8',
              errors='ignore') as lines:
        for line in lines:
            md = md5(line.strip().encode('utf-8')).hexdigest()
            dictionary[md[:1]].write(md + ':' + line.strip() + '\n')
