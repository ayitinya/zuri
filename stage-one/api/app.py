from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_endpoint():
    slack_name = request.args.get('slack_name', 'Rudy Sulley')
    track = request.args.get('track', 'backend')
    github_file_url = request.args.get('github_file_url', 'https://github.com/ayitinya/zuri/blob/main/stage-one/api/app.py')
    github_repo_url = request.args.get('github_repo_url', 'https://github.com/ayitinya/zuri')

    # Get the current day of the week
    current_day = datetime.utcnow().strftime('%A')

    # Get the current UTC time in the desired format
    utc_time = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    response = {
        "slack_name": slack_name,
        "current_day": current_day,
        "track": track,
        "utc_time": utc_time,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

