# Cisco Devnet Sandbox API

Using the cisco devnet api at sandboxapicem.cisco.com, this app makes a post request to get an access token that it can then use to pull about
all the nodes on this sandbox. Once the request has completed you can either view the data over CLI in a formatted table or you can launch a web server that will display the data over web GUI

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install libraries.

```bash
pip install -r requirements.txt
```

## Usage

The following command will render a table in your command prompt displaying node information
```bash
python main.py showtable

Token: ST-28602-gyQxKViEbPebtNlccI3h-cas
Accessing device list
Type                                            Family             IP Address    MAC Address        Serial Number    Uptime
----------------------------------------------  -----------------  ------------  -----------------  ---------------  ---------------------
Cisco Catalyst 29xx Stack-able Ethernet Switch  Switches and Hubs  10.2.1.17     64:a0:e7:d4:9b:c1  FOC1537W1ZY      219 days, 21:09:28.84
Cisco Catalyst 3850-48U-E Switch                Switches and Hubs  10.1.12.1     f0:29:29:5c:30:e2  FOC1703V36B      175 days, 0:00:54.84
Cisco Catalyst 6503 Switch                      Switches and Hubs  10.1.7.1      24:e9:b3:3f:b1:80  FXS1825Q1PA      109 days, 8:08:47.24
Cisco Catalyst 4507R plus E Switch              Switches and Hubs  10.1.11.1     30:e4:db:25:75:3f  FOX1525G5S1      367 days, 9:12:46.03
Cisco 4451 Series Integrated Services Router    Routers            10.1.2.1      f4:4e:05:cf:2e:30  FTX1842AHM2      220 days, 0:03:46.17
Cisco 4451 Series Integrated Services Router    Routers            10.1.4.2      f4:4e:05:cf:2f:e0  FTX1842AHM1      445 days, 18:58:51.74
```
The following will launch a web server and display the data over web GUI
```bash
python main.py serve
```
