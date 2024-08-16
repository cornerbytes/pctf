if __name__ == "__main__":
    with open('flag.png', 'rb') as f:
        flag = f.read()
    with open('gnp.galf', 'wb') as f:
        f.write(flag[::-1])
