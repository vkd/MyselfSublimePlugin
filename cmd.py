import json


def run_cmd(cmd, data):
    data = {"cmd": cmd, "data": data}
    out = str(json.dumps(data)).encode('utf-8')
    import http.client
    conn = http.client.HTTPConnection("localhost:8601")
    conn.request("POST", "/cmd", body=out)
    r1 = conn.getresponse()
    data = json.loads(r1.read().decode())
    conn.close()
    # print(r1.status, data)
    if r1.status != 200:
        return None, data
    return data, None
    # try:
    #     global f
    #     f = urllib.request.urlopen(GOLIME_DAEMON_URL, data=out)
    # except urllib.error.HTTPError:
    #     body = f.read().decode('utf-8')
    #     print(dir(f), f.status, body)
    #     response = json.loads(body)
    #     return None, response

    # response = json.loads(f.read().decode('utf-8'))
    # return response, None
