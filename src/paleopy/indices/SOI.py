def get_BOM_MSLP(station='tahiti'):
    """
    get the 'raw' MSLP for Tahiti or Darwin from the Australian BoM 
    """
    
    import urllib
    import subprocess
    import pandas as pd

    url = "ftp://ftp.bom.gov.au/anon/home/ncc/www/sco/soi/{}mslp.html".format(station)
    
    req = urllib.request.Request(url)

    r = urllib.request.urlopen(req)

    data = r.read()

    data = data.splitlines()

    fout = open('./{}_text'.format(station), 'w')
    if station == 'tahiti':
        data = data[15:-1]
    else:
        data = data[14:-1]
    data = [x.decode('utf-8') for x in data]
    data = [x+'\n' for x in data]
    fout.writelines(data)
    fout.close()
    data = pd.read_table('./{}_text'.format(station),sep='\s+', engine='python', na_values='*', index_col=['Year'])
    subprocess.Popen(["rm {}*".format(station)], shell=True, stdout=True).communicate()
    return(data)