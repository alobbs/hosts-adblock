import requests

AGENT = 'Mozilla/5.0 (X11; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0'
HEADERS = {'Referer': 'http://forum.xda-developers.com/', 'User-Agent': AGENT}
YOYO_DATA = {"mimetype": "plaintext", "hostformat": "unixhosts"}

HOST_LIKE_LISTS = [
    ('http://www.malwaredomainlist.com/hostslist/hosts.txt', None),
    ('http://adblock.gjtech.net/?format=unix-hosts', None),
    ('http://someonewhocares.org/hosts/hosts', None),
    ('http://winhelp2002.mvps.org/hosts.txt', None),
    ('http://adaway.org/hosts.txt', None),
    ('http://adblock.mahakala.is/', HEADERS),
]

HOST = "0.0.0.0"
OUTPUT_FILE = 'hosts-adblock-alobbs'
COMMENT = ("alobbs hosts adblock", "https://github.com/alobbs/host-adblock")


def bad_domain(d):
    if not d or not d.strip():
        return True
    if any([n in d for n in ['127.0.0.1', '::1', '#', ' ', '\\', '$']]):
        return True


def hosts_entry(d):
    d = (d or "").strip().replace('\t', ' ')
    if not d or d[0] == '#':
        return
    d = ' '.join([w for w in d.split(' ') if w])
    return d.split(' ')[1]


def get(url, **kw):
    if 'data' in kw:
        print("[POST] {}".format(url))
        return requests.post(url, **kw)
    print("[GET] {}".format(url))
    return requests.get(url, **kw)


def get_hosts(url, **kw):
    tmp = [hosts_entry(l) for l in get(url, **kw).text.split('\n')]
    return [e for e in tmp if not bad_domain(e)]


r = get('http://pgl.yoyo.org/adservers/serverlist.php?', data=YOYO_DATA)
domains = set([l.strip() for l in r.text.split('\n') if not bad_domain(l)])

for (url, headers) in HOST_LIKE_LISTS:
    domains |= set(get_hosts(url, headers=headers))

with open(OUTPUT_FILE, 'w+') as f:
    f.write(''.join(['# {}\n'.format(l) for l in COMMENT]))
    f.write(''.join(['{} {}\n'.format(HOST, n) for n in domains]))

print("{} creater with {} entries".format(OUTPUT_FILE, len(domains)))
