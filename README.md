```
openssl req -nodes -newkey rsa:2048 -keyout server.key -out server.csr -subj "/C=JP/ST=Hokkaido/L=Sapporo/O=Example INC./OU=IT Department/CN=example.com" && openssl x509 -req -days 3650 -in server.csr -signkey server.key -out server.crt
```