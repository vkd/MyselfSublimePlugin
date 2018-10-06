import json
import http.client


def run_cmd(cmd, data):
    data = {"cmd": cmd, "data": data}
    out = str(json.dumps(data)).encode('utf-8')
    conn = http.client.HTTPConnection("localhost:8601")

    try:
        conn.request("POST", "/cmd", body=out)
    except ConnectionRefusedError:
        raise CommandFailed("connection refused")

    r1 = conn.getresponse()
    data = json.loads(r1.read().decode())
    conn.close()
    if r1.status != 200:
        raise CommandFailed(data)
    return data


class CommandFailed(Exception):
    pass
