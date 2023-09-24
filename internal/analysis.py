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
        
        try:
            res = self.nmap.scan_top_ports(self.host)
            
            item = next(iter(res))
            
            # check os of the target (if any information received, it is a vulen)
            if item['osmatch']:
                v.append("os version")
            
            # check to see if we have ports enable
            if len(item['ports']) > 0:
                # if any ports where available we can dos
                v.append("dos")
                v.append("ddos")
                v.append("buffer overflow")
                
                for port in item['ports']:
                    # check to see if port available on tcp
                    if port['protocol'] == "tcp":
                        v.append("tpc")
                
                    # for high ports we can make deep attacks
                    if port['portid'] > 3000:
                        v.append("soap")
                        v.append("cross site scripting")
                        v.append("csrf")
                        v.append("xml external entity")
                    
                    # if service name is ssh then new vulens can have
                    if port['service']:
                        if port['service']['name'] == "ssh":
                            v.append("broken object level authorization")
                            v.append("broken authentication")
                            v.append("broken object property level authorization")
                            v.append("broken function level authorization")
                            v.append("broken access control")
                            v.append("lack of two factor authentication")
        except:
            return []
        
        return v
    
    def dns_scan(self):
        v = []
        
        try:
            res = self.nmap.nmap_dns_brute_script(self.host)
            
            # third party vulens
            if len(res) > 0:
                v.append("insecure third party dependencies")
                v.append("remote file inclusion")
                v.append("man in the middle")
                v.append("phishing")
                v.append("dns spoofing")
                v.append("third party dependency")
                v.append("side channel")
            
            # mail and other injections
            for item in res:
                if "mail" in item['hostname']:
                    v.append("email header injection")
                if "database" in item['hostname']:
                    v.append("sql injection")
                    v.append("nosql injection")
                    v.append("mysql server")
        except:
            return []
        
        return v
    
    def os_scan(self):
        v = []
        
        try:
            res = self.nmap.nmap_os_detection(self.host)
            
            if not res['error']:
                v.append("os version")
                v.append("vm version")
                v.append("on container image")
                v.append("docker image")
        except:
            return []
        
        return v
    
    def version_scan(self):
        v = []
        
        try:
            res = self.nmap.nmap_version_detection(self.host)
            
            item = next(iter(res))
            
            if len(item['task_results']) > 0:
                v.append("authentication lack")
                v.append("fingerprinting")
        except:
            return []
        
        return v
    
    def vulen_scan(self):
        v = []
        
        try:
            res = self.nmap.nmap_version_detection(self.host, args="--script vulners --script-args mincvss+5.0")
            
            if res:
                v.append("input fields")
                v.append("html form")
                v.append("http parameter pollution")
                v.append("logical errors")
                v.append("unsafe consumption of apis")
                v.append("huge payload")
                v.append("xss-scripting")
        except:
            return []
        
        return v
    
    def ping_scan(self):
        v = []
        
        try:
            res = self.nmap2.nmap_ping_scan(self.host)
            
            with open("ping_scan.json", "w") as file:
                file.write(json.dumps(res, indent=4))
        except:
            return []
        
        return v
        
    def syn_scan(self):
        v = []
        
        try:
            res = self.nmap2.nmap_syn_scan(self.host)
            
            with open("syn_scan.json", "w") as file:
                file.write(json.dumps(res, indent=4))
        except:
            return []
        
        return v

    def tcp_scan(self):
        v = []
        
        try:
            res = self.nmap2.nmap_tcp_scan(self.host)
            
            with open("tcp_scan.json", "w") as file:
                file.write(json.dumps(res, indent=4))
        except:
            return []
            
        return v
    
    def udp_scan(self):
        v = []
        
        try:
            res = self.nmap2.nmap_udp_scan(self.host)
            
            with open("udp_scan.json", "w") as file:
                file.write(json.dumps(res, indent=4))
        except:
            return []
        
        return v
