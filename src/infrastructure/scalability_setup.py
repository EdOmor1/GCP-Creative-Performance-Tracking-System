from google.cloud import compute_v1

def create_instance_group(project_id, zone, instance_group_name):
    client = compute_v1.InstanceGroupManagerClient()
    project = f"projects/{project_id}"
    zone = zone
    name = instance_group_name
    base_instance_name = "instance"
    target_size = 3  # Example target size, adjust as needed

    instance_template = f"projects/{project_id}/global/instanceTemplates/your_instance_template"

    config = {
        "base_instance_name": base_instance_name,
        "target_size": target_size,
        "instance_template": instance_template,
        # Add more configuration as needed
    }

    operation = client.insert(request={"project": project, "zone": zone, "instanceGroupManagerResource": config})
    operation.result()

    print(f"Instance group {instance_group_name} created successfully.")

# Example usage
if __name__ == "__main__":
    project_id = "your_project_id"
    zone = "your_zone"
    instance_group_name = "your_instance_group_name"
    create_instance_group(project_id, zone, instance_group_name)
