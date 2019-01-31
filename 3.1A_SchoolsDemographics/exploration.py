if __name__ == "__main__":
    import pandas as pd
    
    contents = pd.read_csv('data/CRDC2013_14.csv',encoding="Latin-1")
    
    juv_justice = contents['JJ'].value_counts()
    magnet = contents['SCH_STATUS_MAGNET'].value_counts()
    
    print("Juv Justice facilities: ")
    print(juv_justice)
    print("Magnet schools:")
    print(magnet)
    
    jj_piv = pd.pivot_table(contents, values=['TOT_ENR_M', 'TOT_ENR_F'], index='JJ', aggfunc='sum')
    
    magnet_piv = pd.pivot_table(contents, values=['TOT_ENR_M', 'TOT_ENR_F'], index='SCH_STATUS_MAGNET', aggfunc='sum')
    
    print("Juv Justice facilities: ")
    print(jj_piv)
    print("Magnet schools:")
    print(magnet_piv)