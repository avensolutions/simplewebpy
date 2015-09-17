import web
import config

t_globals = dict(
  datestr=web.datestr,
)

render = web.template.render('templates/system/', cache=config.cache, 
    globals=t_globals)
render._keywords['globals']['render'] = render

render_user = web.template.render('templates/user/', cache=config.cache, 
    globals=t_globals)
render_user._keywords['globals']['render_user'] = render_user