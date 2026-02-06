import sys

ALLOWED_ENCODINGS = {
    "utf-8",
    "utf-16-be",
    "utf-16-le",
    "utf-32-be",
    "utf-32-le",
    "latin-1",
}


def read_text(file_name: str, encoding: str) -> str:
    with open(file_name, "r", encoding=encoding) as f:
        return f.read()


def main() -> None:
    if len(sys.argv) < 3:
        print("Needs <file_name> and <encoding> arguments")
        return

    file_name = sys.argv[1]
    encoding = sys.argv[2].lower()

    if encoding not in ALLOWED_ENCODINGS:
        print(
            "Unsupported encoding. Use one of: " + ", ".join(sorted(ALLOWED_ENCODINGS))
        )
        return

    try:
        content = read_text(file_name, encoding)
    except FileNotFoundError:
        print(f"File '{file_name}' not found.")
        return

    print(content)


if __name__ == "__main__":
    main()
