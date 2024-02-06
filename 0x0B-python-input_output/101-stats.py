#!/usr/bin/python3
import sys


def print_stats(total_size, status_counts):
    """print states"""
    print("File size:", total_size)
    for code in sorted(status_counts.keys()):
        print("{}: {}".format(code, status_counts[code]))


def parse_line(line):
    """parse lines"""
    parts = line.split()
    size = int(parts[-1])
    code = parts[-2]
    return size, code


def main():
    """main function"""
    total_size = 0
    status_counts = {}

    try:
        for i, line in enumerate(sys.stdin, start=1):
            size, code = parse_line(line)
            total_size += size
            status_counts[code] = status_counts.get(code, 0) + 1

            if i % 10 == 0:
                print_stats(total_size, status_counts)

    except KeyboardInterrupt:
        print_stats(total_size, status_counts)
        raise


if __name__ == "__main__":
    main()
