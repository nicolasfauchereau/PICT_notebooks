def get_CPC_SAM(url='https://www.cpc.ncep.noaa.gov/products/precip/CWlink/daily_ao_index/aao/monthly.aao.index.b79.current.ascii.table'):

    import pandas as pd

    sam = pd.read_table(url, sep=r"\s+") 

    sam = sam.stack()

    sam.index = pd.date_range(start='1979-01-31', freq='M', periods=len(sam))

    sam = sam.to_frame(name='CPC SAM')

    return sam 
