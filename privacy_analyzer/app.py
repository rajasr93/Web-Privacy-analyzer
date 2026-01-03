import logging
from flask import Flask, render_template, request
import json

app = Flask(__name__)

# DISABLING LOGS (Privacy-First Mode)
# This prevents IP addresses from being written to your server's console or files.
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

@app.route('/')
def home():
    # 1. Capture IP Address
    # If behind a proxy (like Cloudflare or Nginx), use X-Forwarded-For
    if request.headers.getlist("X-Forwarded-For"):
        ip_address = request.headers.getlist("X-Forwarded-For")[0]
    else:
        ip_address = request.remote_addr

    # 2. Capture Browser Headers (The "Browser Request Params" section)
    headers_info = {
        "User-Agent": request.headers.get('User-Agent'),
        "Accept-Language": request.headers.get('Accept-Language'),
        "Referer": request.headers.get('Referer', 'Direct Entry'),
        "Sec-Ch-Ua": request.headers.get('Sec-Ch-Ua'),
        "Sec-Ch-Ua-Platform": request.headers.get('Sec-Ch-Ua-Platform'),
        "Host": request.headers.get('Host'),
        "Connection": request.headers.get('Connection'),
        "X-Requested-With": request.headers.get('X-Requested-With'),
        "Accept": request.headers.get('Accept'),
        "Accept-Encoding": request.headers.get('Accept-Encoding'),
        # Adding a few more from the user's snippet for completeness
        "Sec-Ch-Ua-Mobile": request.headers.get('Sec-Ch-Ua-Mobile'),
        "Sec-Fetch-Site": request.headers.get('Sec-Fetch-Site'),
        "Sec-Fetch-Mode": request.headers.get('Sec-Fetch-Mode'),
        "Sec-Fetch-Dest": request.headers.get('Sec-Fetch-Dest'),
        "Priority": request.headers.get('Priority'),
    }

    # 3. Check for specific Privacy Headers (Do Not Track)
    dnt_status = "Enabled" if request.headers.get('DNT') == '1' else "Disabled"

    # Pass all headers for potential "raw" display if needed, but headers_info is cleaner
    return render_template('index.html', 
                           ip=ip_address, 
                           headers=headers_info, 
                           dnt=dnt_status)

if __name__ == '__main__':
    # Run on 0.0.0.0 so you can test it from other devices on your network
    app.run(host='0.0.0.0', port=5000, debug=True)
