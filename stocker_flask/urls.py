from config import app
import views as v

@app.route("/")
def index():
    print 'routed works'
    return v.index("static/index.html")

@app.route('/api/v1.0/defaultExcoList', methods=['GET'])
def get_default_exco_list():
    return v.getDefaultExcoList()