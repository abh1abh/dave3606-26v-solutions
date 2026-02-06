import sys

ALLOWED_ENCODINGS = {
    "utf-8",
    "utf-16-be",
    "utf-16-le",
    "utf-32-be",
    "utf-32-le",
    "latin-1",
}


def write_text(file_name: str, encoding: str, content: str) -> None:
    with open(file_name, "w", encoding=encoding, newline="") as f:
        f.write(content)


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

    text = input("Enter text to store: ")
    write_text(file_name, encoding, text)
    print(f"Wrote {len(text)} characters to '{file_name}' using {encoding}.")


if __name__ == "__main__":
    main()
