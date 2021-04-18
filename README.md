# requests-anonym
Anonim Requests With Tor


Preparations:

1)  brew install tor
2)  brew services start tor
Check if tor works well
```bash
curl --socks5 localhost:9050 --socks5-hostname localhost:9050 -s https://check.torproject.org/ | cat | grep -m 1 Congratulations | xargs
```
3) pip install requests pysocks stem fake_useragent
