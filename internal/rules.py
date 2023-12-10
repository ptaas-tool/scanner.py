import random
import time


DOMAIN = [
    "Third party dependencies",
    "Public access endpoints",
    "Not secured ports (tls lack)",
    "Open redirection",
    "Session id in headers",
    "Open ports for file",
    "Insecure Interfaces and APIs",
    "Misconfigured Access Controls",
    "Inadequate Authentication and Identity Management",
    "Data Breaches and Data Loss",
    "Shared Technology Vulnerabilities",
    "Account Hijacking",
    "Insufficient Logging and Monitoring",
    "Insecure Configurations",
    "Denial of Service (DoS) Attacks",
    "Physical Security Risks",
    "Supply Chain Vulnerabilities",
    "Data Interception and Man-in-the-Middle Attacks",
    "Insufficient Incident Response Planning",
    "Weak Encryption Practices",
    "Insufficient Data Segregation",
    "Insecure Orchestration of Containers",
    "Insecure Serverless Implementations",
    "API Gateway Vulnerabilities",
    "Insufficient Network Security",
    "Security Misconfiguration of Serverless Functions",
    "Lack of Compliance Controls",
    "Data Residency and Compliance Issues",
    "Insufficient Disaster Recovery and Backup"
]


def load_rules() -> list:
    time.sleep(random.randint(10, 20))
    
    return random.sample(DOMAIN, random.randint(0, len(DOMAIN) - 1))
