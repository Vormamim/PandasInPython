"""
Main entry point for the Weather Data Analysis tutorial.
Simple console menu for students.
"""

import pandas as pd
from src import api_handler, data_cleaner, data_filter, visualizations, session


def show_menu():
    """Display main menu options."""
    print("\n" + "="*60)
    print("WEATHER DATA ANALYSIS")
    print("="*60)
    print("1. Fetch weather data")
    print("2. Clean and prepare data")
    print("3. Filter data")
    print("4. Visualize data")
    print("5. Save session")
    print("6. Load session")
    print("7. List sessions")
    print("0. Exit")
    print("-"*60)


def main():
    """Main menu loop."""
    df = None  # current working dataframe
    
    while True:
        show_menu()
        choice = input("Select option: ").strip()
        
        if choice == "1":
            # Fetch weather
            print("\nEnter coordinates (default: Sydney)")
            lat = input("Latitude [-33.86]: ").strip() or "-33.86"
            lon = input("Longitude [151.20]: ").strip() or "151.20"
            
            data = api_handler.fetch_weather(float(lat), float(lon))
            df = pd.DataFrame(data['hourly'])
            print(f"✓ Loaded {len(df)} rows")
            
        elif choice == "2":
            # Clean data
            if df is None:
                print("No data loaded. Fetch data first.")
                continue
            
            print("\nCleaning options:")
            print("1. Ensure datetime")
            print("2. Drop missing values")
            print("3. Convert column to numeric")
            clean_choice = input("Select: ").strip()
            
            if clean_choice == "1":
                df = data_cleaner.ensure_datetime(df)
                print("✓ Converted 'time' to datetime")
            elif clean_choice == "2":
                df = data_cleaner.drop_missing(df)
                print(f"✓ Dropped missing values. {len(df)} rows remain")
            elif clean_choice == "3":
                col = input("Column name: ").strip()
                df = data_cleaner.to_numeric(df, col)
                print(f"✓ Converted '{col}' to numeric")
                
        elif choice == "3":
            # Filter data
            if df is None:
                print("No data loaded. Fetch data first.")
                continue
            
            print("\nFilter options:")
            print("1. Filter by time range")
            print("2. Filter by temperature range")
            filter_choice = input("Select: ").strip()
            
            if filter_choice == "1":
                start = input("Start date (e.g. 2026-03-02): ").strip()
                end = input("End date: ").strip()
                df = data_filter.filter_by_time_range(df, start, end)
                print(f"✓ Filtered to {len(df)} rows")
            elif filter_choice == "2":
                low = float(input("Min temp: ").strip())
                high = float(input("Max temp: ").strip())
                df = data_filter.filter_by_temp_range(df, low, high)
                print(f"✓ Filtered to {len(df)} rows")
                
        elif choice == "4":
            # Visualize
            if df is None:
                print("No data loaded. Fetch data first.")
                continue
            
            print("\nColumns available:", ", ".join(df.columns[:5]))
            x_col = input("X column: ").strip()
            y_col = input("Y column: ").strip()
            filename = input("Save to file? (leave blank to show): ").strip()
            
            visualizations.plot_line(df, x_col, y_col, filename=filename if filename else None)
            
        elif choice == "5":
            # Save session
            if df is None:
                print("No data to save.")
                continue
            
            name = input("Session name: ").strip()
            notes = input("Notes (optional): ").strip()
            
            session.save_session(name, {'df': df, 'notes': notes})
            
        elif choice == "6":
            # Load session
            name = input("Session name: ").strip()
            data = session.load_session(name)
            
            # Handle dataframe reconstruction
            if 'df' in data and isinstance(data['df'], list):
                df = pd.DataFrame(data['df'])
            else:
                df = data.get('df')
            
            print(f"✓ Loaded session. {len(df)} rows")
            if 'notes' in data:
                print(f"  Notes: {data['notes']}")
                
        elif choice == "7":
            # List sessions
            session.list_sessions()
            
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
