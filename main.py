import argparse
import sys
import time

from src.process_mp import process_mp




def get_args():
    args = sys.argv[1:]
    parser = argparse.ArgumentParser(description="Lift Form Tracker")
    parser.add_argument("-i", "--input_file", required=True, help="Path to the input file")
    parser.add_argument("-o", "--output_file", required=True, help="Path to the output file")
    return parser.parse_args(args)


def main():
    start = time.time()
    args = get_args()
    process_mp(args.input_file, args.output_file)
    end = time.time()

    elapsed = end - start
    minutes, seconds = divmod(elapsed, 60)
    print(f'Time taken: {minutes:.0f} minutes {seconds:.2f} seconds')


if __name__ == '__main__':
    print('Starting lift form tracker')
    main()
    print('Ending lift form tracker')
