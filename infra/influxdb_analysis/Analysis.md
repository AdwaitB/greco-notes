
### Load lib


```python
import pandas as pd
import numpy as np

from matplotlib import pyplot as plt
from datetime import datetime
from scipy.optimize import curve_fit

from data import datasets_location

plot_size = (15, 10)
```

### Helper Functions


```python
def fix_date(df):
    df['time'] = df['time'].apply(lambda x:datetime.strptime(x, '%Y-%m-%dT%H:%M:%S.%fZ'))

def gaussian(x, mean, amplitude, standard_deviation):
    return amplitude * np.exp( - ((x - mean) / standard_deviation) ** 2)
```

###  Read the data file


```python
data = []
data_mts = []
data_mtts = []

for i in range(0, 3):
    data.append(pd.read_csv(datasets_location[i] + "_1.csv"))
    
    data_mts.append(np.array(data[i]["transfer_history.mean_transfer_size"]))
    data_mts[i] = data_mts[i][data_mts[i] != 0.0]
    
    data_mtts.append(np.array(data[i]["transfer_history.mean_time_transfer_sec"]))
    data_mtts[i] = data_mtts[i][data_mtts[i] > 0.0]
```


```python
def plot_hist(cut, temp, bins):
    
    plt.figure(figsize=plot_size)
    plt.hist(temp, bins=bins)
    plt.axvline(np.exp(cut), color='k', linestyle='dashed')
    plt.grid(True)
    plt.xlabel('Size')
    plt.ylabel('Historgram')
    plt.show()

    temp = np.log(temp)
    
    bin_heights, bin_borders = np.histogram(temp, bins='auto')
    bin_widths = np.diff(bin_borders)
    bin_centers = bin_borders[:-1] + bin_widths / 2
    popt, _ = curve_fit(gaussian, bin_centers, bin_heights, p0=[1., 0., 1.])
    print(popt)
    
    x_interval_for_fit = np.linspace(bin_borders[0], bin_borders[-1], 10000)

    plt.figure(figsize=plot_size)
    plt.plot(x_interval_for_fit, gaussian(x_interval_for_fit, *popt), label='fit', c='red')
    plt.hist(temp, bins = np.arange(0, 20, 0.4))
    plt.axvline(cut, color='k', linestyle='dashed')
    plt.grid(True)
    plt.xlabel('Size')
    plt.ylabel('Historgram')
    plt.show()

    print("Points above the dotted line : " + str(sum(temp > cut)))
    print("Total points in the dataset : " + str(len(temp)))

    # plt.hist(temp, bins=np.arange(6000000000, 19000000000, 500000000))
    # plt.axis([6000000000, 19000000000, 0, 20])
    # plt.hist(temp, bins=np.arange(0, 18000000000, 100000000))
    # plt.axis([0, 4000000000, 0, 1500])   
```


```python
plot_hist(18.5, data_mts[0], np.arange(0, 18000000000, 400000000)) 
```


![png](output_7_0.png)


    [ 17.40975867 338.30512167   0.42844914]



![png](output_7_2.png)


    Points above the dotted line : 343
    Total points in the dataset : 905



```python
plot_hist(18.5, data_mts[1], np.arange(0, 18000000000, 400000000)) 
```


![png](output_8_0.png)


    [ 17.40381268 411.70073058   0.47421844]



![png](output_8_2.png)


    Points above the dotted line : 423
    Total points in the dataset : 1467



```python
plot_hist(18.5, data_mts[2], np.arange(0, 18000000000, 400000000)) 
```


![png](output_9_0.png)


    [1.74995175e+01 9.66126871e+02 2.80541912e-01]



![png](output_9_2.png)


    Points above the dotted line : 974
    Total points in the dataset : 3024



```python
plot_hist(1.5, data_mtts[0], np.arange(0, 400, 20)) 
```


![png](output_10_0.png)


    [ 1.44344649 95.00284371  0.48928868]



![png](output_10_2.png)


    Points above the dotted line : 507
    Total points in the dataset : 940



```python
plot_hist(1.5, data_mtts[1], np.arange(0, 400, 20))
```


![png](output_11_0.png)


    [  1.41400687 155.66548519   0.48973168]



![png](output_11_2.png)


    Points above the dotted line : 755
    Total points in the dataset : 1608



```python
plot_hist(1.5, data_mtts[2], np.arange(0, 400, 20)) 
```


![png](output_12_0.png)


    [  1.52112072 245.04944146   0.36461271]



![png](output_12_2.png)


    Points above the dotted line : 1807
    Total points in the dataset : 3092



```python

```
