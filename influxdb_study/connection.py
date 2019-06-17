from influxdb import InfluxDBClient
from util import *

import pandas as pd
import urllib3


# Class to handle the connection
class Connection:

    # Stores if the connection is valid or not. Do not use this for checking the status.
    # Use connection.validate()
    valid = False

    # Create the connection
    def __init__(self):
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

        print_with_time("Connecting to InfluxDB")

        host = 'influx-hpc.qarnot.net'
        port = 58086
        username = 'greco'
        password = '6ZBIaoQeKNK4SnOuuRLv'
        database = 'hpc'

        self.client = InfluxDBClient(host, port, username, password, database, ssl=True)

        if self.validate():
            print_with_time("Connection complete")
        else:
            print_with_time("Connection failed")

    # Checks if the connection is valid. Returns the validity status
    def validate(self):
        if self.client.ping() != "":
            self.valid = True
        else:
            self.valid = False
        return self.valid

    # Close the current connection
    def close(self):
        print_with_time("Closing InfluxDB connection")

        if self.valid:
            self.client.close()
        self.valid = False

        print_with_time("InfluxDB client closed")

    # Execute a query
    def query(self, query):
        query_result = ""

        if self.valid:
            query_result = self.client.query(query)

        query_result = pd.DataFrame(query_result.get_points())
        print_with_time(query_result, nl=1)
        return 0


