from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# This will hold your data
entries = []

@app.route('/')
def index():
    return render_template('index.html', entries=entries)

@app.route('/add', methods=['POST'])
def add_entry():
    youtube_link = request.form['youtube_link']
    start_time = int(request.form['start_hours']) * 3600 + int(request.form['start_minutes']) * 60 + int(request.form['start_seconds'])
    end_time = int(request.form['end_hours']) * 3600 + int(request.form['end_minutes']) * 60 + int(request.form['end_seconds'])

    if end_time <= start_time:
        return jsonify({'error': 'Ending time should come after starting time'}), 400

    entry = {
        'youtube_link': youtube_link,
        'start_time': start_time,
        'end_time': end_time
    }
    entries.append(entry)
    return jsonify(entry)

@app.route('/remove', methods=['POST'])
def remove_entry():
    index = int(request.form['index'])
    if 0 <= index < len(entries):
        del entries[index]
        return jsonify({'success': True})
    return jsonify({'error': 'Invalid index'}), 400

if __name__ == '__main__':
    #app.run(debug=True) this was original, following is to uplaod to github and run on zeet
    app.run(debug=False, host = '0.0.0.0') #i.e. visible publicly
