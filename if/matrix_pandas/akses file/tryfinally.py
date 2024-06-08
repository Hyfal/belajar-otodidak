f = None
try:
    f = open('data.txt')
    data = f.read()
    print(data)
finally:
    if f is not None:
        f.close()