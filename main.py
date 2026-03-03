"""
Basic script demonstrating how main imports helper functions.
"""

import pandas as pd

# Importing helper modules from the src package in one line
from src import api_handler, data_filter, visualizations, session


def main():
    """Demonstrate the full workflow using a public posts API."""

    # 1. check the API is reachable
    url = "https://jsonplaceholder.typicode.com/posts"
    print("Checking API availability...")
    api_handler.check_api(url)

    # 2. fetch data and import into pandas
    print("Fetching posts...")
    posts = api_handler.fetch_posts()
    df = pd.DataFrame(posts)
    print("Loaded dataframe with", len(df), "rows")
    print(df.head())

    # 3. filter the data (e.g. keep only users 1-5)
    df = data_filter.filter_by_column_threshold(df, "userId", 5)
    print("After filtering, rows:", len(df))

    # 4. display a few records using the helper
    api_handler.display_raw_data(df.to_dict(orient="records"), max_items=3)

    # 5. turn the data into a simple graph
    print("Plotting id vs userId")
    visualizations.plot_line(df, "id", "userId")

    # 6. save the session
    session.save_session("posts_example", {"df": df, "notes": "Filtered userId<=5"})

# Run the main function when this script is executed
# this is a common Python idiom to allow the script to be imported without running the main function
if __name__ == "__main__":
    main()
