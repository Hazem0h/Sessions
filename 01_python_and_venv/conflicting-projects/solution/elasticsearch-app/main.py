import elasticsearch

if elasticsearch.__version__ != (0,4,1):
    raise Exception("Wrong version of elasticsearch")

pass