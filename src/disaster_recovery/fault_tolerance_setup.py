from google.cloud import compute_v1

def create_health_check(project_id, health_check_name):
    client = compute_v1.HealthChecksClient()
    project = f"projects/{project_id}"
    name = health_check_name
    request_body = {
        "name": name,
        "type": "HTTP",
        # Add more configuration as needed
    }

    operation = client.insert(request={"project": project, "healthCheckResource": request_body})
    operation.result()

    print(f"Health check {health_check_name} created successfully.")

# Example usage
if __name__ == "__main__":
    project_id = "your_project_id"
    health_check_name = "your_health_check_name"
    create_health_check(project_id, health_check_name)
