import argparse

def main():
    parser = argparse.ArgumentParser(description="Basic CLI example")
    parser.add_argument("--name", default="World", help="Name to greet")
    parser.add_argument("--repeat", type=int, default=1, help="Times to repeat")

    args = parser.parse_args()

    for i in range(args.repeat):
        print(f"Hello, {args.name}!")

if __name__ == "__main__":
    main()
