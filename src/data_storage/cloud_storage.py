from google.cloud import storage

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    # Upload the file
    blob.upload_from_filename(source_file_name)

    print(f"File {source_file_name} uploaded to {destination_blob_name}.")

# Example usage
if __name__ == "__main__":
    bucket_name = "your_bucket_name"
    source_file_name = "local_file.txt"
    destination_blob_name = "uploaded_file.txt"
    upload_blob(bucket_name, source_file_name, destination_blob_name)
