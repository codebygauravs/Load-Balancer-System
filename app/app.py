from flask import Flask
import socket
import time

app = Flask(__name__)

start_time = time.time()

@app.route("/")
def home():
    uptime = int(time.time() - start_time)
    hostname = socket.gethostname()

    return f"""
    <html>
    <head>
        <title>DevOps App</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background: #0f172a;
                color: #e2e8f0;
                text-align: center;
                padding-top: 50px;
            }}
            .card {{
                background: #1e293b;
                padding: 30px;
                border-radius: 15px;
                display: inline-block;
                box-shadow: 0px 0px 20px rgba(0,0,0,0.5);
            }}
            h1 {{
                color: #38bdf8;
            }}
            .highlight {{
                color: #22c55e;
                font-weight: bold;
            }}
        </style>
    </head>
    <body>
        <div class="card">
            <h1>DevOps Load Balanced App</h1>
            <p><b>Container:</b> <span class="highlight">{hostname}</span></p>
            <p><b>Status:</b> Healthy</p>
            <p><b>Uptime:</b> {uptime} seconds</p>
            <br>
            <p>Refresh to see load balancing in action</p>
        </div>
    </body>
    </html>
    """

@app.route("/health")
def health():
    uptime = int(time.time() - start_time)
    return {
        "status": "healthy",
        "container": socket.gethostname(),
        "uptime_seconds": uptime
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
