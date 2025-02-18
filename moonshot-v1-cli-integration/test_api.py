import json

from dotenv import load_dotenv
import os
from util import parametrize, INPUT_PARAMS
import boto3

load_dotenv()  # Load environment variables from .env file

AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')

EXPECTED_OUTCOME = [
    "Success",      # Expected result
    "Failed",      # Expected result
    "Failed",      # Expected result
    "Failed",      # Expected result
    "Failed",     # Expected result
    "Failed",     # Expected result
]
# @parametrize("input_params, expected", zip(INPUT_PARAMS, EXPECTED_OUTCOME))
# def test_parametrize(input_params,expected):
#     print("Parameters : "+str(input_params)+":  "+ str(expected))
#     assert input_params == expected

def test_access_s3_bucket():
    # Specify the bucket name and the key (file name in S3)
    object_key = 'test.csv'  # For example, 'folder/myfile.txt'
    bucket_name = 's3-aiss-moonshot-dev-app-lite'
    s3_client = boto3.client('s3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    response = s3_client.list_objects_v2(Bucket=bucket_name)

    # Get the file names
    foundRecordStatus = False
    if 'Contents' in response:
        for obj in response['Contents']:
            if obj['Key'] == object_key:
                foundRecordStatus = True
            print(obj['Key'])
        if foundRecordStatus == False :
            #########################################################################
            # Upload Files to S3 Bucket

            # Path to the local file you want to upload
            file_path = '/Users/jacksonboey/Downloads/test.csv'

            # Upload the file
            s3_client.upload_file(file_path, bucket_name, object_key)

            print(f'File {file_path} uploaded to {bucket_name}/{object_key}')
            #########################################################################

    #########################################################################
    # Delete Files from S3 Bucket
    # Specify the bucket name and the key (file name in S3)
    object_key = 'test.csv'  # For example, 'folder/myfile.txt'

    # Delete the object
    response = s3_client.delete_object(Bucket=bucket_name, Key=object_key)

    # Print response to confirm the deletion
    print(f'File {object_key} has been deleted from {bucket_name} Result {response}')
    #########################################################################

    object_key = 'secondtest.json'  # The path to the JSON file in S3

    # Get the object from S3
    response = s3_client.get_object(Bucket=bucket_name, Key=object_key)

    # Read the content of the object
    json_content = response['Body'].read().decode('utf-8')

    # Parse the JSON content
    data = json.loads(json_content)

    # Print the parsed data
    print(f'Json Content :{data}')
    assert False
    #########################################################################