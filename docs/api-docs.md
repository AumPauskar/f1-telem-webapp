# API documentation

- `index`
    - Route: `/`
    - Methods: N/A
    - Arguments: N/A
    - Description: Renders the index page.
    - Returns: HTML page.

- `get_session_data`
    - Route: `/get_session_data`
    - Methods: GET
    - Arguments: 
        - `year`: int - The year of the session
        - `event`: str - The event name (Bahrain Grand Prix, Saudi Arabian Grand Prix, etc.). Accepts the first name of the event. Example: Bahrain, Saudi Arabian, for Bahrain Grand Prix, Saudi Arabian Grand Prix etc.
        - `session`: str - The session type (FP1, FP2, FP3, Q1, Q2, Q3, R). Accepts the first name of the session. Example: 1, 2, 3, Q, R for Free Practice 1, Free Practice 2, Free Practice 3, Qualifying and Race.
        - `driver`: str - The driver name. Accepts the first name of the driver. Example: VER and PER becomes the arguments for Max Verstappen and Sergio Perez respectively etc.
    - Description: Returns the telemetry data for the given session id.
    - Returns: JSON object. Status code 200 if successful, 404 if the session data is not found.