from fetch_data import Fetch
from web_server import Server

def main():
    fetch = Fetch()
    data = fetch.get_device_list()
    server = Server(data)
    server.start_server()

main()
