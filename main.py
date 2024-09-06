import gui
import data_processing
import google_sheets_api


def main():
    use_gui = True  # Define use_gui
    user_input = None  # Placeholder for user input

    try:
        if use_gui:
            gui.start_gui()
        else:
            # Command-line input and processing
            user_input = input("Enter data: ")
            data = data_processing.process_data(user_input)
            google_sheets_api.append_data_to_sheet(data)
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
