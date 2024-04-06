from flask import Flask, request, send_file
import fastf1
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/get_session_data/<int:year>/<event>/<session>/<driver>', methods=['GET'])
def get_session_data(year, event, session, driver):
    try:
        print(year, event, session, driver)
        event = event + " Grand Prix"
        data = fastf1.get_session(year, event, session)
        data.load()
        driver_data = data.laps.pick_driver(driver)
        telem = driver_data.telemetry
        print(telem)

        # Save telemetry data to a CSV file
        csv_file = f'{driver}_telemetry_{year}_{event}_{session}.csv'
        telem.to_csv(csv_file, index=False)

        # Return the CSV file for download
        return send_file(csv_file, as_attachment=True, download_name=csv_file)
    except Exception as e:
        # returning 400 Bad Request response
        return str(e), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)