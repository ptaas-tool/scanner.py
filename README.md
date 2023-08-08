# APT Scanner

![](https://img.shields.io/badge/Language-Golang-blue)
![](https://img.shields.io/badge/Platform-APT-blue)
![](https://img.shields.io/badge/App-Security_Scanner-blue)
![](https://img.shields.io/badge/Version-v0.1-blue)

This is our ```automated penetration testing``` (aka APT) application scanner component.
Used from [GoTestWAF](https://github.com/wallarm/gotestwaf).
GoTestWAF is a tool for API and OWASP attack simulation that supports a wide range of API protocols including
REST, GraphQL, gRPC, WebSockets, SOAP, XMLRPC, and others.

It was designed to evaluate web application security solutions, such as API security proxies, Web Application Firewalls,
IPS, API gateways, and others.

---
* [How it works](#how-it-works)
* [Requirements](#requirements)
* [Configuration options](#configuration-options)
---

## How it works

GoTestWAF generates malicious requests using encoded payloads placed in different parts of HTTP requests: its body, headers,
URL parameters, etc. Generated requests are sent to the application security solution URL specified during GoTestWAF launch.
The results of the security solution evaluation are recorded in the report file created on your machine.

Default conditions for request generation are defined in the `testcases` folder in the YAML files of the following format:

```yaml
---
payload:
  - '"union select -7431.1, name, @aaa from u_base--w-'
  - "'or 123.22=123.22"
  - "' waitfor delay '00:00:10'--"
  - "')) or pg_sleep(5)--"
encoder:
  - Base64Flat
  - URL
placeholder:
  - UrlPath
  - UrlParam
  - JSUnicode
  - Header
type: "SQL Injection"
...
```

* `payload` is a malicious attack sample (e.g XSS payload like ```<script>alert(111)</script>``` or something more sophisticated).
Since the format of the YAML string is required for payloads, they must be [encoded as binary data](https://yaml.org/type/binary.html).

* `encoder` is an encoder to be applied to the payload before placing it to the HTTP request. Possible encoders are:

    * Base64
    * Base64Flat
    * JSUnicode
    * URL
    * Plain (to keep the payload string as-is)
    * XML Entity

* `placeholder` is a place inside HTTP request where encoded payload should be. Possible placeholders are:

    * gRPC
    * Header
    * UserAgent
    * RequestBody
    * JSONRequest
    * JSONBody
    * HTMLForm
    * HTMLMultipartForm
    * SOAPBody
    * XMLBody
    * URLParam
    * URLPath
    * NonCrudUrlPath
    * NonCrudUrlParam
    * NonCRUDHeader
    * NonCRUDRequestBody
    * RawRequest

    The `RawRequest` placeholder will allow you to do an arbitrary HTTP request. The payload is substituted by replacing the string `{{payload}}` in the URL path, Headers or body. Fields of `RawRequest` placeholder:

    * `method`
    * `path`
    * `headers`
    * `body`

    Required fields for `RawRequest` placeholder:
    
    * `method` field

    Example:
    
    ```yaml
    ---
    payload:
      - test
    encoder:
      - Plain
    placeholder:
      - RawRequest:
          method: "POST"
          path: "/"
          headers:
            Content-Type: "multipart/form-data; boundary=boundary"
          body: |
            --boundary
            Content-disposition: form-data; name="field1"
            
            Test
            --boundary
            Content-disposition: form-data; name="field2"
            Content-Type: text/plain; charset=utf-7
            
            Knock knock.
            {{payload}}
            --boundary--
    type: "RawRequest test"
    ...
    ```

* `type` is a name of entire group of the payloads in file. It can be arbitrary, but should reflect the type of attacks in the file.

Request generation is a three-step process involving the multiplication of payload amount by encoder and placeholder amounts.
Let's say you defined 2 **payloads**, 3 **encoders** (Base64, JSUnicode, and URL) and 1 **placeholder** (URLParameter - HTTP GET parameter).
In this case, GoTestWAF will send 2x3x1 = 6 requests in a test case.

During GoTestWAF launch, you can also choose test cases between two embedded: OWASP Top-10, OWASP-API,
or your own (by using the [configuration option](#configuration-options) `testCasePath`).

## Requirements

* GoTestwaf supports all the popular operating systems (Linux, Windows, macOS), and can be built natively
if [Go](https://golang.org/doc/install) is installed in the system. If you want to run GoTestWaf natively,
make sure you have the Chrome web browser to be able to generate PDF reports. In case you don't have Chrome,
you can create a report in HTML format.
* If running GoTestWAF as the Docker container, please ensure you have [installed and configured Docker](https://docs.docker.com/get-docker/),
and GoTestWAF and evaluated application security solution are connected to the same [Docker network](https://docs.docker.com/network/).
* For GoTestWAF to be successfully started, please ensure the IP address of the machine running GoTestWAF is whitelisted
on the machine running the application security solution.

## Configuration options

```
Usage: ./gotestwaf [OPTIONS] --url <URL>

Options:
      --addDebugHeader          Add header with a hash of the test information in each request
      --addHeader string        An HTTP header to add to requests
      --blockConnReset          If true, connection resets will be considered as block
      --blockRegex string       Regex to detect a blocking page with the same HTTP response status code as a not blocked request
      --blockStatusCodes ints   HTTP status code that WAF uses while blocking requests (default [403])
      --configPath string       Path to the config file (default "config.yaml")
      --email string            E-mail to which the report will be sent
      --followCookies           If true, use cookies sent by the server. May work only with --maxIdleConns=1
      --grpcPort uint16         gRPC port to check
      --idleConnTimeout int     The maximum amount of time a keep-alive connection will live (default 2)
      --ignoreUnresolved        If true, unresolved test cases will be considered as bypassed (affect score and results)
      --logFormat string        Set logging format: text, json (default "text")
      --logLevel string         Logging level: panic, fatal, error, warn, info, debug, trace (default "info")
      --maxIdleConns int        The maximum number of keep-alive connections (default 2)
      --maxRedirects int        The maximum number of handling redirects (default 50)
      --noEmailReport           Save report locally
      --nonBlockedAsPassed      If true, count requests that weren't blocked as passed. If false, requests that don't satisfy to PassStatusCodes/PassRegExp as blocked
      --openapiFile string      Path to openAPI file
      --passRegex string        Regex to a detect normal (not blocked) web page with the same HTTP status code as a blocked request
      --passStatusCodes ints    HTTP response status code that WAF uses while passing requests (default [200,404])
      --proxy string            Proxy URL to use
      --quiet                   If true, disable verbose logging
      --randomDelay int         Random delay in ms in addition to the delay between requests (default 400)
      --renewSession            Renew cookies before each test. Should be used with --followCookies flag
      --reportFormat string     Export report to one of the following formats: none, pdf, html, json (default "pdf")
      --reportName string       Report file name. Supports `time' package template format (default "waf-evaluation-report-2006-January-02-15-04-05")
      --reportPath string       A directory to store reports (default "reports")
      --sendDelay int           Delay in ms between requests (default 400)
      --skipWAFBlockCheck       If true, WAF detection tests will be skipped
      --skipWAFIdentification   Skip WAF identification
      --testCase string         If set then only this test case will be run
      --testCasesPath string    Path to a folder with test cases (default "testcases")
      --testSet string          If set then only this test set's cases will be run
      --tlsVerify               If true, the received TLS certificate will be verified
      --url string              URL to check
      --version                 Show GoTestWAF version and exit
      --wafName string          Name of the WAF product (default "generic")
      --workers int             The number of workers to scan (default 5)
      --wsURL string            WebSocket URL to check
```

## example

A simple scanning on a localhost will be executed with following command:

```shell
./main --url=http://127.0.0.1:9091 --blockRegex true --reportFormat json --reportName localhost --skipWAFIdentification true --skipWAFBlockCheck true --no
EmailReport true
```