with open("pythonic", "rb") as pyf:
    py_bytes = pyf.read()

decrypt = lambda x: chr(x ^ 0x41)
py_file = ''.join([*map(decrypt,py_bytes[12353:12712])])

print(py_file)

decrypt = lambda x,y: chr(x ^ y)

exec(py_file+"\nprint(''.join([*map(decrypt,enc,[69]*len(enc))]))")
