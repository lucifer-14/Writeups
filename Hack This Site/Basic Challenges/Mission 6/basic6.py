def decrypt(data: str) -> str:
    res = ""
    for i, c in enumerate(data):
        tmp = chr(ord(c) - i)
        res += tmp
    return res


if __name__ == "__main__":
    data = str(input("Enter the encrypted message: "))
    print(f"Result: {decrypt(data)}")