from io import StringIO

import requests
import pandas as pd

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


def fetch_and_merge_all_datasets() -> pd.DataFrame:
    """Fetches and combines the three datasets into a single DataFrame."""

    organizations_df = fetch_data_into_dataframe(organizations_url)
    emitters_df = fetch_data_into_dataframe(emitters_url)
    events_df = fetch_data_into_dataframe(events_url)

    # Merge emitters with organizations on organization name
    merged_df = pd.merge(emitters_df, organizations_df, left_on='organization', right_on='name', how='left')

    # Merge the result with events on external_id
    merged_df = pd.merge(merged_df, events_df, left_on='external_id', right_on='external_id', how='left')

    # Select only the required columns
    merged_df = merged_df[['name_y', 'name_x', 'state', 'timestamp']]

    # Rename the columns for clarity
    merged_df = merged_df.rename(columns={'name_y': 'organization_name', 'name_x': 'emitter_name'})

    # Convert timestamp to datetime and sort
    merged_df['timestamp'] = pd.to_datetime(merged_df['timestamp'])
    merged_df = merged_df.sort_values(by='timestamp')

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