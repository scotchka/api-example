"""
The main module. It launches the threads to populate and process
the queue of events, and also starts the Flask server.
"""

import threading
from src.services import get_events, process_events
from src.views import app


if __name__ == "__main__":
    t_fetch_events = threading.Thread(target=get_events)
    t_process_vents = threading.Thread(target=process_events)

    t_fetch_events.start()
    t_process_vents.start()

    app.run(debug=True)  # don't use debug mode in production
