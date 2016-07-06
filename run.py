#!flask/bin/python
import os
from flask import Flask, request, render_template

music_dir = '/vagrant/flaskmedia/static/music'
video_dir = '/vagrant/flaskmedia/static/video'
image_dir = '/vagrant/flaskmedia/static/image'

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def index():
    video_files = [f for f in os.listdir(video_dir) if f.endswith('mp4')]
    video_files_number = len(video_files)
    return render_template("index.html",
                        title = 'Home',
                        video_files_number = video_files_number,
                        video_files = video_files)

if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug = True)

@app.route('/<filename>')
def movie(filename):
    return render_template('play.html',
                        title = filename,
                        video_file = filename)
