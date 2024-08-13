#!/usr/bin/python3 

if __name__ == "__main__":
    x = input('Enter: ')
    result = []
    for i in x: 
        result.append(chr(ord(i)^13))
    result = ''.join(result)
    print(f"here your message: {result}")
