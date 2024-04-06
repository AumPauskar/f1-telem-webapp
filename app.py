from flask import Flask, request, send_file, after_this_request, render_template
import fastf1
import os
import tempfile

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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

        # Save telemetry data to a temporary CSV file
        with tempfile.NamedTemporaryFile(suffix=".csv", delete=False) as temp:
            csv_file = temp.name
            telem.to_csv(csv_file, index=False)

            # Return the CSV file for download
            @after_this_request
            def remove_file(response):
                try:
                    os.remove(csv_file)
                except Exception as error:
                    app.logger.error("Error removing or closing temporary file %s: %s", csv_file, error)
                return response

            return send_file(csv_file, as_attachment=True, download_name=f'{driver}_telemetry_{year}_{event}_{session}.csv')
    except Exception as e:
        # returning 400 Bad Request response
        return str(e), 400

if __name__ == '__main__':
    app.run(port=5000, debug=True)