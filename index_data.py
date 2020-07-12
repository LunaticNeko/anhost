'''
original query



'''

def index_data(df):
    '''
    Given a data frame, perform indexing on it.
    '''
    # if index, index.year, and index.sec are not present, add them.
    # select each year
    #   select each sec
    #       sort by time ascending
    #     index students in sec
    #   sort by time ascending
    #   index students in year
    # sort by time ascending
    # index students (globally)
    pass

'''
the following lines HGT'd from load_originals.py
        df_sub["index.year"] = 0
        df_sub = df_sub.sort_values(by="timestamp", ascending="true")
        df_sub["index.sec"] = np.arange(len(df_sub))+1
        df_sub = df_sub.drop_duplicates(subset=[cn["userid"]], keep="first")
'''
