import argparse

def main():
    parser = argparse.ArgumentParser(description="A console-based application.")
    parser.add_argument("command", help="The command to execute.")
    args = parser.parse_args()

    print(f"Executing command: {args.command}")

if __name__ == "__main__":
    main()
