# scanner.py

![GitHub top language](https://img.shields.io/github/languages/top/apt-tool/apt-scanner)
![GitHub release (with filter)](https://img.shields.io/github/v/release/apt-tool/apt-scanner)

Open source tool to perform API security scan in ```PTaaS```. This scanner uses ```nmap``` in order
to get some details about our target. In this app, we get system information, critical issues, system vulnerabilities,
and system dependencies. After that we return a list of possible vulnerabilities that might be used in a penetrating testing
for that target.

## use

Install dependencies first:

```shell
pip install -r requirements.txt
```

Run the scanner by following command:

```shell
python scanner.py --host webmail.aut.ac.ir
```

### flags

A list of the flags that you can set when executing the scanner:

| Flag     | Description | Value |
| -------- | ----------- | :---: |
| ```--host``` | target address | string |
| ```--ports``` | target port | int |
| ```--protocols``` | target protocols | list |
| ```--type``` | target type (service type) | string |
| ```--deps``` | target deps addresses (dependency services) | list |
| ```--token``` | target access token for authentication | string |
| ```--endpoints``` | target special endpoints | list |
| ```--fastscan``` | scanner fast mode | bool |

## output

```json
[
  {
    "vuln": "injection",
    "attacks": [ "sql injection", "graphql injection" ]
    "path": [
      "/docs/{doc-name}",
      "/docs?sort_by={sorting-field}",
    ],
    "host" : {
      "ip": "127.0.0.2",
      "port": 8080
    }
  }
]
```
