from flask import Flask, render_template, redirect, request
import os

class Desktop:
    def __init__(self, path=None):
        self.user = os.popen("whoami").readline().replace("\n", "")
        self.desktop_path = f"/home/{self.user}/Desktop"
        self.path = path

    def check_folder(self, path):
        try:
            os.chdir(path)
        except:
            return False
        return True

    def get_files(self, path):
        files_dict = dict()
        test = os.popen(f"cd {path}").read()
        try: os.chdir(path)
        except: raise KeyError("folder not found")
        files = os.listdir()
        return files

app = Flask("")
dsk = Desktop()
dsk.path = dsk.desktop_path

@app.route("/")
def index():
    try: path = request.args['path']
    except KeyError: return redirect(f"/?path=/")

    if path.startswith("//"):
        path = path[1:]
        return redirect(f"/?path={path}")

    folder = dsk.check_folder(path)
    if folder:
        files = dsk.get_files(path)
        return render_template("folder.html", files=files, user=dsk.user, path=path)

    else:
        f = open(path)
        text = f.read()
        f.close()
        return render_template("file.html", text=text, user=dsk.user, path=path)

app.run("0.0.0.0", port=3000, debug=True)
