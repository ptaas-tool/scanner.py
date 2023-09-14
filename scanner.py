import argparse


parser = argparse.ArgumentParser(description="scanner script", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--host", help="target address")

args = parser.parse_args()
config = vars(args)

if __name__ == "__main__":
    print(config['host'])
