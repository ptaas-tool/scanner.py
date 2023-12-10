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
    
    # result array
    res = []
    
    # start scanning stages
    res = res + an.port_scan()
    res = res + an.dns_scan()
    res = res + an.os_scan()
    res = res + an.version_scan()
    res = res + an.vulen_scan()
    res = res + an.ping_scan() #deprecated
    res = res + an.syn_scan() #deprecated
    res = res + an.tcp_scan() #deprecated
    res = res + an.udp_scan() #deprecated
    
    # add items to report
    for item in res:
        r.add(item)
    
    # pring output
    print(r.export())
