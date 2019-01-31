if __name__ == "__main__":
    import pandas as pd
    batch = 20
    contents = pd.read_csv('data/CRDC2013_14content.csv')
    for i in range(0,30,batch):
        print(contents[i:i+batch])