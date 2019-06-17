import pandas as pd

from data import datasets_location

# Removes all rows which are completely empty
def remove_empty_rows(df):
    rows = df.shape[0]
    cols = df.shape[1]

    drop_list = []

    nans = df.isna()

    for i in range(rows):
        remove = True
        for j in range(cols):
            if(j == 0):
                pass
            elif not nans.iloc[i,j]:
                remove = False
                break
        if remove:
            drop_list.append(i)

    print("Dropping {} elements from {}. {} entries remain.".format(
        len(drop_list), len(df), len(df) - len(drop_list)))

    return df.drop(drop_list)

# Removes the entries that are completely empty and then saves it as a new file
def remove_completely_empty():
    for key in datasets_location:
        data = pd.read_csv(datasets_location[key] + ".csv")
        print(datasets_location[key] + ".csv")
        print("Shape {}".format(data.shape))
        data = remove_empty_rows(data)

        new_name = datasets_location[key] + "_1.csv"
        print(new_name)
        data.to_csv(new_name)
        print()

remove_completely_empty()