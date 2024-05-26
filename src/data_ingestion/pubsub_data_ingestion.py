from google.cloud import pubsub_v1
import json

def publish_message(project_id, topic_name, data):
    publisher = pubsub_v1.PublisherClient()
    topic_path = publisher.topic_path(project_id, topic_name)

    # Convert data to bytes
    data = json.dumps(data).encode("utf-8")

    # Publish message
    future = publisher.publish(topic_path, data=data)
    print(f"Published message ID {future.result()} to {topic_path}")

# Example usage
if __name__ == "__main__":
    project_id = "your_project_id"
    topic_name = "your_topic_name"
    data = {"message": "Hello, Pub/Sub!"}
    publish_message(project_id, topic_name, data)
