from flask import Flask, request, jsonify, render_template
import sqlite3
import pandas as pd

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('integration.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS survey
                 (id INTEGER PRIMARY KEY, postcode TEXT, integration TEXT)''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    postcode = request.form['postcode']
    integration = request.form['integration']
    conn = sqlite3.connect('integration.db')
    c = conn.cursor()
    c.execute("INSERT INTO survey (postcode, integration) VALUES (?, ?)", (postcode, integration))
    conn.commit()
    conn.close()
    return jsonify({'message': 'Survey response recorded'})

@app.route('/results')
def results():
    conn = sqlite3.connect('integration.db')
    df = pd.read_sql_query("SELECT * FROM survey", conn)
    conn.close()
    
    # Aggregate data
    summary = df.groupby('postcode').integration.value_counts(normalize=True).unstack().fillna(0)
    summary = summary.reset_index()
    
    return render_template('results.html', tables=[summary.to_html(classes='data', header="true")])

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
