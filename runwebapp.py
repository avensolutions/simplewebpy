# simplewebpy - Python Web Programming Made Simple

#
# add pages as follows
#

class index:							#url_mappings class 
    def GET(self):
		return renderpage("homepage")	#renders main content in templates/homepage.html


#		
# no need to modify code below this line...		
#
		
import web, yaml, sys

# read in config from webconfig.yaml
with open('webconfig.yaml', 'r') as f:
    doc = yaml.load(f)

site_title = doc["site_title"]
footer_text = doc["footer_text"]
urls = doc["url_mappings"]	
menus = doc["menus"]	
internalerrmsg = doc["errors"]["internalerror"]["error_text"]
notfounderrmsg = doc["errors"]["notfounderror"]["error_text"] 

# view.py, config.py
sys.path.insert(0, 'modules')
import view, config
from view import render, render_user

app =  web.application(urls, globals())

if doc["logSessions2db"]:
	# CREATE TABLE sessions (session_id character(128) NOT NULL,atime timestamp without time zone NOT NULL DEFAULT now(),data text,CONSTRAINT sessions_session_id_key UNIQUE (session_id));
	db = web.database(dbn=doc["db_config"]["dbtype"], db=doc["db_config"]["db"], user=doc["db_config"]["user"], pw=doc["db_config"]["pw"])
	store = web.session.DBStore(db, 'sessions')
	session = web.session.Session(app, store, initializer={'count': 0})

def internalerror():
	return web.internalerror(render.base(render.head(site_title)
		, render.navbar(menus)
		, render.internalerror(internalerrmsg, render.footer(footer_text))))

def notfound(): 
	return web.notfound(render.base(render.head(site_title)
		, render.navbar(menus)
		, render.notfound(notfounderrmsg, render.footer(footer_text)))) 	
	
app.internalerror = internalerror
app.notfound = notfound	

def renderpage(page):
	renderobj = getattr(render_user, page)
	return render.base(render.head(site_title)
		, render.navbar(menus)
		, renderobj(render.footer(footer_text)))		

if __name__ == "__main__": app.run()