import argparse
from internal.analysis import Analysis
from internal.report import Report
from internal.rules import load_rules

import sys


# parse input arguments
parser = argparse.ArgumentParser(description="scanner script", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--host", help="target address")
parser.add_argument("--ports", help="target port")
parser.add_argument("--protocols", help="target protocol")
parser.add_argument("--type", help="target type (service type)")
parser.add_argument("--deps", help="target address (dependency services)")
parser.add_argument("--token", help="target access token for authentication")
parser.add_argument("--host", help="target address")
parser.add_argument("--endpoints", help="target special endpoints")
parser.add_argument("--fast-scan", help="scanner fast mode")


args = parser.parse_args()
config = vars(args)


# execute scanner
if __name__ == "__main__":
    r = Report()
    
    # create analysis class
    an = Analysis(config['host'])
    
    
    if config["fast-scan"]:
        for item in load_rules():
            r.add(item)
        
        print(r.export())
        sys.exit(1)
    
    
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
