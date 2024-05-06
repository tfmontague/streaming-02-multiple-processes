import csv
import time
import logging
import random

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Declare program constants
INPUT_FILE_NAME = "nutrient.csv"
OUTPUT_FILE_NAME = "out9.txt"

def prepare_message_from_row(row):
    """Prepare a string message from a given row."""
    # Assuming CSV structure: id, name, unit_name, nutrient_nbr, rank, time
    id, name, unit_name, nutrient_nbr, rank, timestamp = row
    # Format the message as a string
    message = f"[{id}, {name}, {unit_name}, {nutrient_nbr}, {rank}, {timestamp}]"
    logging.debug(f"Prepared message: {message}")
    return message

def stream_row(input_file_name, output_file_name):
    """Read from input file and write data to output file."""
    logging.info(f"Starting to stream data from {input_file_name} to {output_file_name}.")
    
    with open(input_file_name, 'r') as input_file, open(output_file_name, 'w') as output_file:
        logging.info(f"Opened {input_file_name} for reading and {output_file_name} for writing.")
        
        reader = csv.reader(input_file)
        header = next(reader)  # Skip header row
        logging.info(f"Skipped header row: {header}")

        # Reverse the list of rows to ensure oldest data is processed first
        rows = list(reader)
        for row in reversed(rows):
            message = prepare_message_from_row(row)
            output_file.write(message + "\n")
            output_file.flush()  # Ensure message is written to file
            logging.info(f"Written: {message} to {output_file_name}.")
            time.sleep(random.randint(1, 3))  # Sleep between 1 and 3 seconds

if __name__ == "__main__":
    try:
        logging.info("===============================================")
        logging.info("Starting fake streaming process.")
        stream_row(INPUT_FILE_NAME, OUTPUT_FILE_NAME)
        logging.info("Streaming complete!")
        logging.info("===============================================")
    except Exception as e:
        logging.error(f"An error occurred: {e}")
