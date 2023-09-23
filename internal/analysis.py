import nmap3
import json


class Analysis(object):
    """use analysis object to scan your hosts

    Args:
        object (_type_): python base object
    """
    def __init__(self, host):
        self.nmap = nmap3.Nmap()
        self.nmap2 = nmap3.NmapScanTechniques()
        self.host = host
    
    def port_scan(self):
        v = []
        res = self.nmap.scan_top_ports(self.host)
        
        with open("port_scan.json", "w") as file:
            file.write(json.dumps(res, indent=4))
        
        return v
    
    def dns_scan(self):
        res = self.nmap.nmap_dns_brute_script(self.host)
        
        with open("dns_scan.json", "w") as file:
            file.write(json.dumps(res, indent=4))
        
        return []
    
    def os_scan(self):
        res = self.nmap.nmap_os_detection(self.host)
        
        with open("os_scan.json", "w") as file:
            file.write(json.dumps(res, indent=4))
        
        return []
    
    def version_scan(self):
        res = self.nmap.nmap_version_detection(self.host)
        
        with open("version_scan.json", "w") as file:
            file.write(json.dumps(res, indent=4))
        
        return []
    
    def vulen_scan(self):
        res = self.nmap.nmap_version_detection(self.host, args="--script vulners --script-args mincvss+5.0")
        
        with open("vulen_scan.json", "w") as file:
            file.write(json.dumps(res, indent=4))
        
        return []
    
    def ping_scan(self):
        res = self.nmap2.nmap_ping_scan(self.host)
        
        with open("ping_scan.json", "w") as file:
            file.write(json.dumps(res, indent=4))
        
        return []
        
    def syn_scan(self):
        res = self.nmap2.nmap_syn_scan(self.host)
        
        with open("syn_scan.json", "w") as file:
            file.write(json.dumps(res, indent=4))
        
        return []

    def tcp_scan(self):
        res = self.nmap2.nmap_tcp_scan(self.host)
        
        with open("tcp_scan.json", "w") as file:
            file.write(json.dumps(res, indent=4))
            
        return []
    
    def udp_scan(self):
        res = self.nmap2.nmap_udp_scan(self.host)
        
        with open("udp_scan.json", "w") as file:
            file.write(json.dumps(res, indent=4))
        
        return []
