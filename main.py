from flask import Flask, render_template, jsonify
import time

app = Flask(__name__)

video_duration = 1405
start_time = time.time()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/time')
def get_time():
    elapsed_time = time.time() - start_time
    video_time = elapsed_time % video_duration
    return jsonify({'time': video_time})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)