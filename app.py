import os
from flask import Flask, render_template, request, jsonify, url_for
from werkzeug.utils import secure_filename
from rembg import remove, new_session
from PIL import Image

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Reuse a single model session to avoid reload cost; default to the small/fast model.
MODEL_NAME = os.getenv('REMBG_MODEL', 'u2netp')  # options: u2netp (fast), u2net (quality), u2net_human_seg, etc.
SESSION = new_session(MODEL_NAME)


def _is_ajax(req):
    """Return True when the request is coming from fetch/XHR."""
    return req.headers.get('X-Requested-With') == 'XMLHttpRequest' or req.accept_mimetypes['application/json']


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return ('No file uploaded', 400)
        
        file = request.files['file']
        if file.filename == '':
            return ('No file selected', 400)

        if file:
            safe_name = secure_filename(file.filename)
            # 1. Save the original file
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], safe_name)
            file.save(input_path)

            # 2. Process with rembg (AI Magic) using the preloaded session for speed
            input_image = Image.open(input_path).convert('RGBA')
            output_image = remove(input_image, session=SESSION)

            # 3. Save the result
            output_filename = 'no_bg_' + safe_name
            output_path = os.path.join(app.config['UPLOAD_FOLDER'], output_filename)
            output_image.save(output_path)

            original_url = url_for('static', filename=f"uploads/{safe_name}")
            result_url = url_for('static', filename=f"uploads/{output_filename}")

            # 4. Show the page with the result
            if _is_ajax(request):
                return jsonify({"original_image": original_url, "result_image": result_url})

            return render_template('index.html', 
                                   original_image=original_url, 
                                   result_image=result_url)

    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.getenv('PORT', '5000'))
    app.run(debug=True, host='0.0.0.0', port=port)