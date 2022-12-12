from app import app, render_template


@app.route('/')
def index():    
    return render_template('index.html')

@app.route('/login', methods=["GET","POST"])
def login():
    return render_template('auth/login.html')

@app.route("/register", methods=["GET","POST"])
def register():
    return render_template('auth/register.html', form=register)
    