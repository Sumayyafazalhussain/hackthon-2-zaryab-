import argparse
from utils.file_util import read_file, write_file
import os

def _handle_read(args):
    try:
        content = read_file(args.file_path)
        print(content)
    except FileNotFoundError:
        print(f"Error: File not found at {args.file_path}")
    except PermissionError:
        print(f"Error: Permission denied for file at {args.file_path}")

def _handle_write(args):
    try:
        write_file(args.file_path, args.content)
        print(f"Successfully wrote to file: {args.file_path}")
    except FileNotFoundError:
        print(f"Error: File not found at {args.file_path}")
    except PermissionError:
        print(f"Error: Permission denied for file at {args.file_path}")

def _handle_delete(args):
    try:
        os.remove(args.file_path)
        print(f"Successfully deleted file: {args.file_path}")
    except FileNotFoundError:
        print(f"Error: File not found at {args.file_path}")
    except PermissionError:
        print(f"Error: Permission denied for file at {args.file_path}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def main():
    parser = argparse.ArgumentParser(description="A console-based application.")
    subparsers = parser.add_subparsers(dest="command", help="The command to execute.")

    # Read command
    parser_read = subparsers.add_parser("read", help="Reads the content of a file.")
    parser_read.add_argument("file_path", help="The path to the file to read.")

    # Write command
    parser_write = subparsers.add_parser("write", help="Writes content to a file.")
    parser_write.add_argument("file_path", help="The path to the file to write to.")
    parser_write.add_argument("content", help="The content to write to the file.")

    # Delete command
    parser_delete = subparsers.add_parser("delete", help="Deletes a file.")
    parser_delete.add_argument("file_path", help="The path to the file to delete.")

    args = parser.parse_args()

    if args.command == "read":
        _handle_read(args)
    elif args.command == "write":
        _handle_write(args)
    elif args.command == "delete":
        _handle_delete(args)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
