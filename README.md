## PS-Web-Beacon

A simple http server to transfer files from windows to any other machine. This method utilises PowerShell's IWR to send a base64 encoded file as post data to a python web server, the web server then saves the base64 decoded post data to a file

On origin machine

```
$b64 = [System.convert]::ToBase64String((Get-Content -Path '[FILE-PATH]' -Encoding Byte))
Invoke-WebRequest -Uri http://[<IP>]:[<PORT>] -Method POST -Body $b64
```

On destination

```
./server.py [<output-file>] [<port>]
./server.py [<output-file>]
```
