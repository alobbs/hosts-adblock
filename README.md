# Advertisement blocking «hosts» file
Download the hosts file form the following URL:

```
https://github.com/alobbs/hosts-adblock/raw/master/hosts-adblock-alobbs
```

### Dnsmasq configuration
If you run a instance of dnsmasq, you can improve dramatically the quality of your everyday Internet experience in two easy steps:
1. Add a `addn-hosts` entry to your `dnsmasq.conf` file, so it reads to hosts file:
   ```
   addn-hosts=/path/to/hosts-adblock-alobbs
   ```
2. Restart dnsmasq
