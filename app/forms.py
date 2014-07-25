#from wtforms.form import Form
#from wtforms import TextField, BooleanField
import sys
sys.path.append("D:\Users\jkathuri\projects\microblog\microblog_flask_master_kit\Lib\site-packages")
path = sys.path
from wtforms import Form
from wtforms import TextField, BooleanField
from wtforms.validators import Required


class LoginForm(Form):
	openid = TextField('openid',validators=[Required()])
	remember_me = BooleanField('Remember me!', default=False)
	