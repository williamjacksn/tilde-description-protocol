```
william@protocol:~/tilde-description-protocol$ ./tilde_server.py --help
usage: tilde_server.py [-h] [-t | -j] [-m]

Generate a server info document that conforms to the Tilde Description
Protocol

optional arguments:
  -h, --help    show this help message and exit
  -t, --text    Output plain text
  -j, --json    Output json text
  -m, --minify  Output minified JSON

See http://protocol.club/~datagrok/beta-wiki/tdp.html to learn more about the
Tilde Description Protocol
```

```
william@protocol:~/tilde-description-protocol$ ./tilde_users.py --help
usage: tilde_users.py [-h] [-m] [-t]

Generate a user list document that conforms to the Tilde Description Protocol

optional arguments:
  -h, --help    show this help message and exit
  -m, --minify  Output minified JSON
  -t, --text    Output plain text instead of JSON

See http://protocol.club/~datagrok/beta-wiki/tdp.html to learn more about the
Tilde Description Protocol
```
