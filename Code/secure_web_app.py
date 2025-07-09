from flask import Flask, make_response

app = Flask(__name__)

@app.route('/')
def home():
    response = make_response("<h1>Welcome to My Secure Web App</h1>")
    
    # Adding security headers
    response.headers['Content-Security-Policy'] = "default-src 'self'; script-src 'self'"
    response.headers['Strict-Transport-Security'] = 'max-age=31536000; includeSubDomains'
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    return response

@app.route('/xss')
def xss_demo():
    # Simulated user input (normally you would get this from query parameters)
    user_input = "<script>alert('XSS')</script>"
    
    # Sanitizing input to prevent XSS
    safe_output = user_input.replace("<", "&lt;").replace(">", "&gt;")
    
    return f"<h2>Input sanitized: {safe_output}</h2>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
