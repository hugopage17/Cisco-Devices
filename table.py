from tabulate import tabulate

class Table:
    def __init__(self):
        pass

    def sort_data(self, devices):
        full_data = []
        for d in devices:
            arr = []
            arr.append(d['type'])
            arr.append(d['family'])
            arr.append(d['managementIpAddress'])
            arr.append(d['macAddress'])
            arr.append(d['serialNumber'])
            arr.append(d['upTime'])
            full_data.append(arr)
        return full_data

    def create_table(self, devices):
        full_data = self.sort_data(devices)
        table = tabulate(full_data, headers=["Type", "Family", "IP Address", "MAC Address", "Serial Number", "Uptime"])
        return table
