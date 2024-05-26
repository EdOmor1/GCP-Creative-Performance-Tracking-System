def process_data(event, context):
    # Process incoming data
    data = event["data"]
    # Perform data processing logic here
    print("Data processed:", data)

    # Example: Return a response
    return "Data processed successfully!"
