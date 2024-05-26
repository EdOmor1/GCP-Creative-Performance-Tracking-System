from google.cloud import bigquery

def create_dataset(project_id, dataset_id):
    client = bigquery.Client()
    dataset_ref = client.dataset(dataset_id)
    dataset = bigquery.Dataset(dataset_ref)
    dataset.location = "US"  # Example location, adjust as needed

    dataset = client.create_dataset(dataset)  # API request

    print(f"Dataset {dataset.dataset_id} created successfully.")

# Example usage
if __name__ == "__main__":
    project_id = "your_project_id"
    dataset_id = "your_dataset_id"
    create_dataset(project_id, dataset_id)
