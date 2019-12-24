import json
import http.server
import socketserver
import webbrowser as wb

class Server:
    def __init__(self, devices):
        json_data = []
        for d in devices:
            x = {
                "type":d['type'],
                "family":d['family'],
                "managementIpAddress":d['managementIpAddress'],
                "macAddress":d['macAddress'],
                "Serial Number":d['serialNumber'],
                "Uptime":d['upTime']
            }
            y = json.dumps(x)
            json_data.append(y)
            y = json.dumps(y)
        with open('cisco_devices.json', 'w') as outfile:
            json.dump(json_data, outfile)

    def start_server(self):
        PORT = 5000
        Handler = http.server.SimpleHTTPRequestHandler
        try:
            with socketserver.TCPServer(("", PORT), Handler) as httpd:
                print("serving at port", PORT)
                wb.open_new_tab('http://localhost:5000/')
                httpd.serve_forever()
        except HTTPError as e:
            print(e)
