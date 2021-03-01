from flask  import Flask,send_file,render_template,request
from pytube import YouTube
from izlesene_downloader import get_video_links,get_video_name,download_video_izlesene

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download')
def youtube_download_file(url):
    yt = YouTube(url)
    yt = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()
    yt.download("./")
    return send_file(yt.default_filename,as_attachment=True)


@app.route('/send_data', methods = ['POST'])
def get_data_from_html():
    download_obj = request.form['download_link']
    try:
        if download_obj != "":
            if "youtube.com" in download_obj:
                youtube_download_file(download_obj)
                return "success"
            elif "izlesene.com" in download_obj:
                video_links = get_video_links(str(download_obj))
                download_video_izlesene(str(download_obj), video_links)
                return "success"
        else:
            raise Exception("url should be entered")
    except:
        return "fail"

@app.route("/success")
def success():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)