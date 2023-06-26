# Lambda functions - in-line, (anonymous)

# syntax:

# lambda arguments: expression


add = lambda x, y, z: x + y + z

def main():
    r = add(1, 2, 3)
    print(r)

    sentence = lambda a, b: f"{a} is greater than {b}"
    result = sentence(100, 15)
    print(result)

main()