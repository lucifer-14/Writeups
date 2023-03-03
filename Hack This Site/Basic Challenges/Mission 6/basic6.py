def decrypt(data: str) -> str:
    res = ""
    for i, c in enumerate(data):
        res += chr(ord(c) - i)
    return res


if __name__ == "__main__":
    data = str(input("Enter the encrypted message: "))
    print(f"Result: {decrypt(data)}")