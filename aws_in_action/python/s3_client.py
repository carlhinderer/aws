import boto3
import logging
import pathlib
import uuid

from botocore.exceptions import ClientError

# Current working directory
BASE_DIR = pathlib.Path(__file__).parent.resolve()

BUCKET_PREFIX = 'awsinaction-carlhinderer-'


class S3Client:
    def __init__(self):
        self.client = boto3.client('s3')

    def list_buckets(self):
        response = self.client.list_buckets()
        print('Existing Buckets:')
        for bucket in response['Buckets']:
            print(f'  {bucket["Name"]}')

    def create_bucket_name(self, bucket_prefix):
        return ''.join([bucket_prefix, str(uuid.uuid4())])

    def create_bucket(self, bucket_name):
        try:
            self.client.create_bucket(Bucket=bucket_name)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    def delete_bucket(self, bucket_name):
        self.client.delete_bucket(Bucket=bucket_name)

    def upload_file(self, bucket_name, filename, object_name=None):
        if object_name is None:
            object_name = filename

        self.client.upload_file(filename, bucket_name, object_name)


if __name__ == '__main__':
    client = S3Client()
    client.list_buckets()

    bucket_name = client.create_bucket_name(BUCKET_PREFIX)
    new_bucket = client.create_bucket(bucket_name)

    # client.delete_bucket(bucket_name)

    filename = f"{BASE_DIR}/demo.txt"
    client.upload_file(bucket_name, filename)
