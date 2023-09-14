import json


class Report(object):
    """use report object in order to export scanner results

    Args:
        object (_type_): base python object
    """
    def __init__(self):
        self.vulnerabilities = []
    
    def add(self, value):
        self.vulnerabilities.append(value)
    
    def export(self):
        return json.dumps(self.vulnerabilities)
