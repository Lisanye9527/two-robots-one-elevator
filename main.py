import os

ENTRY = "\"Going up?\" \"Statistically, one of us is. Eye contact's still behind a firmware update.\""
OUTPUT_PATH = "/output/entry.txt"


def main():
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
