def load_rules() -> list:
    return [
        "third party dependencies",
        "public access endpoints",
        "not secured ports (tls lack)",
        "open redirection",
        "session id in headers",
        "open ports for file"
    ]