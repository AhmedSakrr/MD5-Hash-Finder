from hashlib import md5


def find(what):
    md = md5(what).hexdigest()

    with open('hash/' + md[:1] + '.txt', 'r',
              encoding='utf-8', errors='ignore') as lines:
        for line in lines:
            if md in line:
                print(line)
                break


if __name__ == "__main__":
    query = input('Hash: ').encode('utf-8')
    find(query)
