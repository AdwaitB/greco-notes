import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from datetime import datetime
from connection import *

con = Connection()
con.query("SELECT * FROM \"hpc\".\"two_months\".\"transfer_history\" WHERE time <= '2019-03-04 01:01:00'")
con.close()
