

def download(): 
    import urllib.request
    import os

    print('Beginning file download with urllib2...')
    path = os.path.join(os.getcwd(), 'catalogs') 
    os.mkdir(path)

    url = 'https://archive.stsci.edu/pub/hlsp/stisngsl/v2/stis_ngsl_v2.zip'
    urllib.request.urlretrieve(url, './catalogs/stis_ngsl_v2.zip')
    print('... download complete.')

    for root, dirs, files in os.walk("."):
        for filename in files:
            print(filename)
        for dir in dirs:
            print(dir)