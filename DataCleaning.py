import os
import re

format_pat = re.compile(
    r"(?P<host>[\d\.]+)\s"
    r"(?P<identity>\S*)\s"
    r"(?P<user>\S*)\s"
    r"\[(?P<time>.*?)\]\s"
    r'"(?P<request>.*?)"\s'
    r"(?P<status>\d+)\s"
    r"(?P<bytes>\S*)\s"
    r'"(?P<referer>.*?)"\s'
    r'"(?P<user_agent>.*?)"\s*'
)

log_path = os.getcwd() + '/data/access_log.txt'

URL_dict = {}
unuseful_agents = {'bot', 'spider', 'Bot', 'Spider', 'W3 Total Cache', '-'}
with open(log_path, 'r') as f:
    for line in (l.rstrip() for l in f):
        match = format_pat.match(line)
        if match:
            access = match.groupdict()
            request = access['request']
            agent = access['user_agent']
            if len(request.split()) == 3:
                (action, URL, protocol) = request.split()
                if URL in URL_dict and action == 'GET' and agent not in unuseful_agents:
                    URL_dict[URL] += 1
                else:
                    URL_dict[URL] = 1

results = sorted(URL_dict, key=lambda x: URL_dict[x], reverse=True)

for res in results[:20]:
    print res, URL_dict[res]
