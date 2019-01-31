if __name__ == "__main__":
    import pandas as pd
    
    dat = pd.read_csv('data/CRDC2013_14.csv',encoding="Latin-1")
    dat['total_enrollment'] = dat['TOT_ENR_M']+dat['TOT_ENR_F']
    all_enrollment = dat['total_enrollment'].sum()
        
    cols_m = ['SCH_ENR_HI_M',
            'SCH_ENR_AM_M',
            'SCH_ENR_AS_M',
            'SCH_ENR_HP_M',
            'SCH_ENR_BL_M',
            'SCH_ENR_WH_M',
            'SCH_ENR_TR_M',
           ]
    
    cols_f = [
            'SCH_ENR_HI_F',
            'SCH_ENR_AM_F',
            'SCH_ENR_AS_F',
            'SCH_ENR_HP_F',
            'SCH_ENR_BL_F',
            'SCH_ENR_WH_F',
            'SCH_ENR_TR_F',
           ]
    
    totals_dic_m = {}
    for c in cols_m:
        totals_dic_m[c[:-2]] = dat[c].sum()
        
    totals_dic_f = {}
    for c in cols_f:
        totals_dic_f[c[:-2]] = dat[c].sum()

    tot_m = pd.Series(totals_dic_m, name='Male')
    tot_f = pd.Series(totals_dic_f, name='Female')

    totals = pd.concat([tot_m, tot_f], axis=1)
    totals['Total'] = totals['Male'] + totals['Female']
       
    totals['Percent'] = totals['Total']/all_enrollment * 100.0
    
    totals.sort_values(by='Percent', inplace=True, ascending=False)
    
    hundred = totals['Percent'].sum()
    all_races = totals['Total'].sum()
    
    print("All enrollment = "+str(all_enrollment)+", all races = "+str(all_races)+", 100% = "+str(hundred))
    
    print("Total boys = "+str(tot_m.sum())+", total girls = "+str(tot_f.sum()))
    
    print(totals)
    
    