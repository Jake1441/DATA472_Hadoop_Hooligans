import selenium
import pandas as pd    #Add all imports to a libraries file


file = "trend_clean.csv" #Just here for now to have a prototype


def tempdata():
    dataset = pd.read_csv(file)
    return dataset


def main():
    return tempdata()



dataset = main()
print(dataset.head())


