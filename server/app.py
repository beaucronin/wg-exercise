import os
import pwd
import sys

from flask import Flask, redirect, url_for

app = Flask(__name__)

root_dir = os.getenv("ROOT_DIR", "/tmp")
print(f"Using root folder {root_dir}")

@app.route("/")
def list_root():
    """
    This route handles just the root of the local filesystem, since the
    subpath route below will not match for an empty path.
    """
    return process_path("")

@app.route("/<path:subpath>", methods=["GET"])
def list_path(subpath):
    """
    The main route, which uses Flask's path functionality to match the 
    subpath to use.
    """
    return process_path(subpath)

def process_path(subpath):
    if subpath == "":
        local_path = root_dir
    else:
        local_path = os.path.join(root_dir, subpath)
    
    if os.path.exists(local_path) and os.path.isdir(local_path):
        return {
            "message": "success",
            "local_path": local_path,
            "contents": path_contents(local_path)
        }
    elif os.path.exists(local_path):
        return {
            "message": f"{local_path} exists, but is not a directory"
        }, 400
    else:
        return {
            "message": f"{local_path} not found"
        }, 400
        
def path_contents(path):
    resp = []
    for el in os.listdir(path):
        abs_name = os.path.join(path, el)
        if os.path.isfile(abs_name):
            file_stat = os.stat(abs_name)
            file_owner = pwd.getpwuid(file_stat.st_uid).pw_name
            file_size = os.path.getsize(abs_name)
            file_perms = oct(file_stat.st_mode)[-3:]
            resp.append({
                "name": el,
                "owner": file_owner,
                "size": file_size,
                "perms": file_perms
            })
    return resp
            