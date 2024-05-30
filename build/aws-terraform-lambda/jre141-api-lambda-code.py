import json
import urllib.request
from datetime import datetime, timedelta

# required for s3 bucket
import boto3


def lambda_handler(event, context):
    # Retrieve API key from query parameters if passed via URL
    api_key = event.get('queryStringParameters', {}).get('api_key', '')

    if api_key == "secret":
        # Parse query parameters from the event
        start_date_str = event.get('queryStringParameters', {}).get('start_date')
        end_date_str = event.get('queryStringParameters', {}).get('end_date')

        # Convert query parameters to datetime objects
        if start_date_str:
            start_date = datetime.strptime(start_date_str, '%Y-%m-%d').date()
        else:
            start_date = datetime.now().date() - timedelta(days=30)  # Default to past 30 days

        if end_date_str:
            end_date = datetime.strptime(end_date_str, '%Y-%m-%d').date()
        else:
            end_date = datetime.now().date()

        # Construct the URL for the API request
        url = f"https://api.inaturalist.org/v1/observations?place_id=40469&iconic_taxa=Fungi&order=desc&order_by=created_at&per_page=5&page=1&d1={start_date.isoformat()}&d2={end_date.isoformat()}&quality_grade=research"

        # Make the HTTP GET request
        response = urllib.request.urlopen(url)
        data = json.loads(response.read().decode())

        # Format a simple response
        result = {'observations': []}
        for obs in data.get('results', []):
            observation_details = {
                'id': obs['id'],
                'observed_on': obs.get('observed_on', ''),
                'latitude': obs.get('location', '').split(',')[0],
                'longitude': obs.get('location', '').split(',')[-1]
            }
            result['observations'].append(observation_details)

        # Prepare the JSON response
        response_body = {
            "statusCode": 200,
            "body": json.dumps(result)
        }

        """
        Configuration:
        bucket_name the name of your bucket in S3
        file_name the key that your bucket will display
        file_content the value of the key.
        
        Use S3
        put into the value the file_contnet
        use bucket bucket_name
        with the key file_name
        """
        bucket_name = 'data472-jre141-lambdabucket'
        file_name = 'results.txt'
        file_content = json.dumps(result)

        s3 = boto3.client('s3')
        s3.put_object(Body=file_content, Bucket=bucket_name, Key=file_name)

        return response_body
    else:
        return {
            "statusCode": 503,
            "body": json.dumps('Unauthorized access!')
        }
