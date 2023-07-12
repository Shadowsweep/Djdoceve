from flask import Flask, jsonify
import subprocess
import json

app = Flask(__name__)

@app.route('/get_ids', methods=['GET'])
def get_ids():
    # Run the Python script and capture its output
    result = subprocess.run(['python', 'doceveapp/fetchideas.py'], capture_output=True, text=True)

    # Check if the Python script executed successfully
    if result.returncode == 0:
        # Parse the JSON output from the Python script
        try:
            output = json.loads(result.stdout)
        except json.JSONDecodeError as e:
            return jsonify(error='Error parsing JSON output')

        # Return the output as JSON response
        return jsonify(output)
    else:
        # Return an error message
        return jsonify(error='Python script execution failed')

if __name__ == '__main__':
    app.run()
