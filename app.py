from flask import Flask, request
import fastf1

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/get_session_data/<int:year>/<event>/<session>/<driver>', methods=['GET'])
def get_session_data(year, event, session, driver):
    try:
        print(year, event, session, driver)
        event = event + "Grand Prix"
        data = fastf1.get_session(year, event, session)
        data.load()
        driver_data = data.laps.pick_driver(driver)
        telem = driver_data.telemetry
        print(telem)
        # returning 200 OK response
        return telem.to_json(), 200
    except Exception as e:
        # returning 400 Bad Request response
        return str(e), 400
    

if __name__ == '__main__':
    app.run(port=5000, debug=True)