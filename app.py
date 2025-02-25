from flask import *
import os
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Directory where files are stored
FILES_DIRECTORY = "./files"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# Helper function to get file info
def get_files(search_query=None):
    files = []
    if not os.path.exists(FILES_DIRECTORY):
        return files

    for file_name in os.listdir(FILES_DIRECTORY):
        if search_query and search_query.lower() not in file_name.lower():
            continue

        file_path = os.path.join(FILES_DIRECTORY, file_name)
        if os.path.isfile(file_path):
            file_info = {
                "name": file_name,
                "size": f"{os.path.getsize(file_path) / 1024:.2f} KB",
                "modified": datetime.fromtimestamp(os.path.getmtime(file_path)).strftime('%Y-%m-%d %H:%M:%S')
            }
            files.append(file_info)

    return files

@app.route('/files', methods=['GET'])
def list_files():
    search_query = request.args.get('search')
    files = get_files(search_query)
    return jsonify(files)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)