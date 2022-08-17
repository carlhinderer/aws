import boto3
import time


REGION = 'us-east-1'
AMAZON_LINUX_AMI_ID = 'ami-0cff7528ff583bf9a'
INSTANCE_TYPE = 't2.micro'


class Ec2Client:
    def __init__(self):
        self.client = boto3.client('ec2', region_name=REGION)

    def list_my_images(self):
        response = self.client.describe_images(Owners=['self'])
        for ami in response['Images']:
            print(name, ami['Name'], ami['ImageId'], ami['State'])

    def list_my_subnets(self):
        response = self.client.describe_subnets()
        print(response)

    def list_my_vms(self):
        response = self.client.describe_instances()
        print(response)

    def create_vm(self):
        response = self.client.run_instances(
            ImageId=AMAZON_LINUX_AMI_ID,
            MinCount=1,
            MaxCount=1,
            InstanceType=INSTANCE_TYPE,
            KeyName='mykey'
        )
        print(response)
        return response['Instances'][0]['InstanceId']

    def show_vm(self, instance_id):
        response = self.client.describe_instances(InstanceIds=[instance_id])
        print(response)

    def terminate_vm(self, instance_id):
        response = self.client.terminate_instances(InstanceIds=[instance_id])


if __name__ == '__main__':
    client = Ec2Client()

    # client.list_my_images()
    # client.list_my_subnets()
    # client.list_my_vms()

    # new_instance_id = client.create_vm()
    # time.sleep(10)
    # client.show_vm(new_instance_id)
    # client.terminate_vm(new_instance_id)
