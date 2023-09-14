import argparse
from internal.analysis import Analysis
from internal.report import Report


# parse input arguments
parser = argparse.ArgumentParser(description="scanner script", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--host", help="target address")

args = parser.parse_args()
config = vars(args)

# execute scanner
if __name__ == "__main__":
    r = Report()
    
    # create analysis class
    an = Analysis(config['host'])
    
    # start scanning stages
    print(an.port_scan()) # add vulens results to report
    
    # pring output
    print(r.export())
