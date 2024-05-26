# GCP-Creative-Performance-Tracking-System

## Objective

Develop a system to track and analyze the performance of ad creatives across multiple platforms using Google Cloud Platform (GCP) services.

## Components and GCP Services

### Data Ingestion
- **Cloud Pub/Sub**: Real-time data streaming from DV360 and other ad platforms.

### Data Storage
- **Cloud Storage**: Scalable and cost-effective storage for raw data.

### Data Processing
- **Cloud Functions**: Serverless data processing.
- **Cloud Dataproc**: ETL and analytics processing.

### Database
- **Cloud SQL**: Store structured data.

### Analytics and Reporting
- **Data Studio**: Data visualization and performance tracking.

### High Availability
- **Google Compute Engine (GCE) Multi-Region Deployments**: Deploy services across multiple regions to ensure redundancy.

### Scalability
- **Managed Instance Groups**: Automatically adjust the number of VMs based on load.

### Fault Tolerance
- **Disaster Recovery**: Implement fault tolerance and backup strategies using Google Cloud's built-in features.

## Project Structure

Creative-Performance-Tracking-System
│
├── data_ingestion
│   └── pubsub_data_ingestion.py
│
├── data_storage
│   └── cloud_storage.py
│
├── data_processing
│   ├── cloud_functions_processing.py
│   └── dataproc_processing.py
│
├── database
│   └── cloud_sql_setup.py
│
├── analytics_reporting
│   └── data_studio_visualization.py
│
├── infrastructure
│   ├── high_availability_setup.py
│   └── scalability_setup.py
│
└── disaster_recovery
    ├── fault_tolerance_setup.py
    └── backup_setup.py

## How to Run

1. **Set up GCP Credentials**:
   Ensure you have the necessary GCP credentials configured. You can use the gcloud command-line tool to configure your credentials:
   ```sh
   gcloud auth login

2. **Install Dependencies:**
Install the necessary Python packages:
```sh
pip install google-cloud-pubsub google-cloud-storage google-auth

3. Run Data Ingestion:
Start collecting data from ad platforms using Cloud Pub/Sub:
```sh
python data_ingestion/pubsub_data_ingestion.py

4. Store Data:
Store raw data in Cloud Storage:
```sh
python data_storage/cloud_storage.py

5. Process Data:
Process data using Cloud Functions and Cloud Dataproc:
```sh
python data_processing/cloud_functions_processing.py
```sh
python data_processing/dataproc_processing.py

6. Set Up Database:
Configure Cloud SQL:
```sh
python database/cloud_sql_setup.py

7. Analyze and Visualize Data:
Use Data Studio for visualization and reporting:
```sh
python analytics_reporting/data_studio_visualization.py

8. Set up High Availability:
Ensure high availability for services:
```sh
python infrastructure/high_availability_setup.py

9. Set up Scalability:
Automatically scale resources based on load:
```sh
python infrastructure/scalability_setup.py

10. Set up Disaster Recovery:
Implement fault tolerance and backup strategies:
```sh
python disaster_recovery/fault_tolerance_setup.py
```sh
python disaster_recovery/backup_setup.py
