from app import app, render_template, login_required


@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/login', methods=["GET","POST"])
def login():
    return render_template('auth/login.html')

@app.route("/register", methods=["GET","POST"])
def register():
    return render_template('auth/register.html')


@app.route('/sistema')
def sistema():
    return render_template('sistema.html')

@app.route('/project')
@login_required
def project():
    return render_template('interno/project.html')
    