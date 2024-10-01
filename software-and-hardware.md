## How would you like to see a real HTTP response message? 
```

telnet gaia.cs.umass.edu 80
GET /kurose_ross/interactive/index.php HTTP/1.1
Host: gaia.cs.umass.edu

```
(Press the carriage return twice after typing the last line.) This opens a TCP con-
nection to port 80 of the host gaia.cs.umass.edu and then sends the HTTP
request message. You should see a response message that includes the base HTML
file for the interactive homework problems for this textbook. If you’d rather just see
the HTTP message lines and not receive the object itself, replace GET with HEAD

---
