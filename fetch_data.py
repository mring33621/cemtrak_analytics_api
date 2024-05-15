from io import StringIO

import pandas as pd
import requests
from cachetools import cached, TTLCache

# Data URLs
# TODO: make these URLs configurable
organizations_url = "http://localhost:8017/cemtrakapp/organizations/datadump"
emitters_url = "http://localhost:8017/cemtrakapp/emitters/datadump"
events_url = "http://localhost:8989/events/datadump"


# Function to fetch and create dataframe from a URL
def fetch_data_into_dataframe(url: str) -> pd.DataFrame:
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes

    data = response.text
    df = pd.read_csv(StringIO(data))
    return df


@cached(cache=TTLCache(maxsize=1, ttl=300))  # Cache for 5 minutes (300 seconds)
def fetch_and_merge_all_datasets() -> pd.DataFrame:
    """Fetches and combines the three datasets into a single DataFrame,
    adding the 'measurement_amt' based on emitter state.
    """

    organizations_df = fetch_data_into_dataframe(organizations_url)
    emitters_df = fetch_data_into_dataframe(emitters_url)
    events_df = fetch_data_into_dataframe(events_url)

    merged_df = pd.merge(emitters_df, organizations_df, left_on='organization', right_on='name', how='left')
    merged_df = pd.merge(merged_df, events_df, left_on='external_id', right_on='external_id', how='left')

    # Create the 'measurement_amt' column based on state
    def get_measurement_amt(row):
        state = row['state']
        meas_amt_key = f'{state}_measurement_amt'
        meas_amt = row[meas_amt_key]
        is_compensator = row['is_compensator']
        if is_compensator:
            meas_amt = -1 * meas_amt
        return meas_amt

    merged_df['measurement_amt'] = merged_df.apply(get_measurement_amt, axis=1)

    merged_df = merged_df[['name_y', 'name_x', 'state', 'measurement_amt', 'measurement_unit', 'timestamp']]
    merged_df = merged_df.rename(columns={'name_y': 'organization_name', 'name_x': 'emitter_name'})

    merged_df['timestamp'] = pd.to_datetime(merged_df['timestamp'])
    merged_df = merged_df.sort_values(by='timestamp')

    # Convert Timestamps to strings before converting to JSON
    merged_df['timestamp'] = merged_df['timestamp'].dt.strftime('%Y-%m-%d %H:%M:%S.%f').str[:23]

    return merged_df


# Fetch data into pandas dataframes
# TODO: move this to a test script
def show_me_the_datasets():
    organizations_df = fetch_data_into_dataframe(organizations_url)
    emitters_df = fetch_data_into_dataframe(emitters_url)
    events_df = fetch_data_into_dataframe(events_url)

    # Additional processing can be performed here, e.g.,
    #  - Convert timestamp columns to datetime objects:
    #     events_df['timestamp'] = pd.to_datetime(events_df['timestamp'])

    # Dataframes are ready for further analysis
    print("Organizations Data:")
    print(organizations_df)
    print("\nEmitters Data:")
    print(emitters_df)
    print("\nEmitter State Time Series Data:")
    print(events_df)


# TODO: Move this to a test script
def show_me_the_combined_dataset():
    # Get the combined dataframe
    combined_event_df = fetch_and_merge_all_datasets()
    print("\nCombined Event Data:")
    print(combined_event_df)


if __name__ == "__main__":
    show_me_the_datasets()
    show_me_the_combined_dataset()
