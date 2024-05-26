from google.cloud import compute_v1

def create_instance_template(project_id, zone, instance_template_name):
    client = compute_v1.InstanceTemplatesClient()
    project = f"projects/{project_id}"
    name = instance_template_name
    zone = zone
    machine_type = f"zones/{zone}/machineTypes/n1-standard-1"

    config = {
        "name": name,
        "properties": {
            "machineType": machine_type,
            # Add more configuration as needed
        },
    }

    operation = client.insert(request={"project": project, "zone": zone, "instanceTemplateResource": config})
    operation.result()

    print(f"Instance template {instance_template_name} created successfully.")

# Example usage
if __name__ == "__main__":
    project_id = "your_project_id"
    zone = "your_zone"
    instance_template_name = "your_instance_template_name"
    create_instance_template(project_id, zone, instance_template_name)
