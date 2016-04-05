# :shipit: Advertisement blocking «hosts» file
Download the hosts file form the following URL:

```
https://github.com/alobbs/hosts-adblock/raw/master/hosts-adblock-alobbs
```

### Dnsmasq configuration
Adding a `addn-hosts` entry to your `dnsmasq.conf` file will be enough to make dnsmasq read the ad-blocking hosts file:

```
addn-hosts=/path/to/hosts-adblock-alobbs
```
