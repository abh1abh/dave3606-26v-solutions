FILE_NAME = "example.txt"


def write(file_name: str, content: str):
    with open(file_name, "w") as f:
        f.write(content)


def read(file_name) -> str:
    with open(file_name, "r") as f:
        return f.read()


def main():
    text = input("Enter text to store: ").strip()
    if text == "":
        print("Please enter some text.")
        return

    write(FILE_NAME, text)

    print("Saved content:\n" + read(FILE_NAME))


if __name__ == "__main__":
    main()
