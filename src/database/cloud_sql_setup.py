from google.cloud import sql

def create_database(instance_id, database_name):
    client = sql.Client()
    instance = client.instance(instance_id)
    database = instance.database(database_name)

    # Create database
    operation = database.create()
    operation.result()

    print(f"Database {database_name} created successfully.")

# Example usage
if __name__ == "__main__":
    instance_id = "your_instance_id"
    database_name = "your_database_name"
    create_database(instance_id, database_name)
