from flask import Flask, jsonify, request
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)

# Kreiramo konekciju na bazu (mora biti u istom folderu)
engine = create_engine('sqlite:///f1_project.db')

@app.route('/', methods=['GET'])
def index():
    return "F1 Data API is running. Use /api/data to get stats."

@app.route('/api/data', methods=['GET'])
def get_data():
    try:
        pos_filter = request.args.get('pos')
        query = "SELECT * FROM race_stats"
        if pos_filter:
            query += f" WHERE positionOrder = {pos_filter}"
        query += " LIMIT 50"
        df = pd.read_sql(query, engine)
        return jsonify(df.to_dict(orient='records'))
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000, debug=True)
