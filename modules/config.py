import web, yaml, os.path
f = open(os.path.dirname(__file__) + '/../webconfig.yaml')
doc = yaml.load(f)
	
DB = web.database(dbn=doc["db_config"]["dbtype"], db=doc["db_config"]["db"], user=doc["db_config"]["user"], pw=doc["db_config"]["pw"])
cache = False
