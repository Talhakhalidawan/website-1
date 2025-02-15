
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, 
    static_folder='attached_assets',
    template_folder='.')

@app.route('/')
def home():
    return render_template('attached_assets/index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/pricing')
def pricing():
    return render_template('pricing.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

# Serve static files from attached_assets
@app.route('/attached_assets/<path:filename>')
def serve_static(filename):
    return send_from_directory('attached_assets', filename)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
