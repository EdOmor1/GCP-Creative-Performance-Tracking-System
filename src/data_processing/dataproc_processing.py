from google.cloud import dataproc_v1
from google.cloud.dataproc_v1.gapic.enums import ClusterStatus

def run_dataproc_job(project_id, region, cluster_name, job_file_uri):
    job_client = dataproc_v1.JobControllerClient()
    cluster_client = dataproc_v1.ClusterControllerClient()

    cluster_path = f"projects/{project_id}/regions/{region}/clusters/{cluster_name}"

    # Submit job to Dataproc
    job = {
        "placement": {"cluster_name": cluster_path},
        "pyspark_job": {"main_python_file_uri": job_file_uri},
    }
    operation = job_client.submit_job_as_operation(
        request={"project_id": project_id, "region": region, "job": job}
    )
    operation.result()

    # Wait for job completion
    while True:
        cluster = cluster_client.get_cluster(request={"project_id": project_id, "region": region, "cluster_name": cluster_name})
        if cluster.status.state == ClusterStatus.ERROR:
            raise RuntimeError(f"Cluster {cluster_name} encountered an error.")
        if cluster.status.state == ClusterStatus.RUNNING:
            break

    print("Dataproc job completed successfully.")

# Example usage
if __name__ == "__main__":
    project_id = "your_project_id"
    region = "your_region"
    cluster_name = "your_cluster_name"
    job_file_uri = "gs://your-bucket-name/path/to/job.py"
    run_dataproc_job(project_id, region, cluster_name, job_file_uri)
