# APT Scanner

![GitHub release (with filter)](https://img.shields.io/github/v/release/apt-tool/apt-scanner)
![GitHub top language](https://img.shields.io/github/languages/top/apt-tool/apt-scanner)

Open source tool to perform API security scan in ```APT```. This scanner uses ```nmap``` in order
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
