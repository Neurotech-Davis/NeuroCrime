import time
import pandas as pd
from pylsl import resolve_byprop, StreamInlet
import sys

eeg_streams = resolve_byprop('name', 'NeuroCrimeEEG', timeout=5)
marker_streams = resolve_byprop('name', 'NeuroCrimeMarkers', timeout=5)

try:
    if not eeg_streams or not marker_streams:
        raise ConnectionError("Could not connect to stream.")
    print("Connected to ", eeg_streams[0].name())
    print("Connected to ", marker_streams[0].name())
except ConnectionError as e:
    print(e, "Exiting program")
    sys.exit()

eeg_inlet = StreamInlet(eeg_streams[0])
marker_inlet = StreamInlet(marker_streams[0])

collection_duration = 10
start_time = time.time()

eeg_data = []
marker_data = []

while time.time() - start_time < collection_duration:
    eeg_sample, eeg_timestamp = eeg_inlet.pull_sample(timeout=0.0)
    if eeg_sample is not None:
        eeg_data.append({
            'timestamp': eeg_timestamp,
            'data': eeg_sample
        })

    marker_sample, marker_timestamp = marker_inlet.pull_sample(timeout=0.0)
    if marker_sample is not None:
        marker_data.append({
            'timestamp': marker_timestamp,
            'data': marker_sample[0]
        })

    time.sleep(0.0005)


eeg_df = pd.DataFrame(eeg_data)
marker_df = pd.DataFrame(marker_data)

eeg_df.to_csv("eeg_output.csv")
marker_df.to_csv("marker_output.csv")
