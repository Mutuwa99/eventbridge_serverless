import os
import boto3

ec2 = boto3.client('ec2')

def start_instances(event, context):
    instance_ids = os.environ['INSTANCE_IDS'].split(',')
    ec2.start_instances(InstanceIds=instance_ids)
    print(f"Started instances: {instance_ids}")
    
    return {
        'statusCode': 200,
        'body': f"Started instances: {instance_ids}"
    }

def stop_instances(event, context):
    instance_ids = os.environ['INSTANCE_IDS'].split(',')
    ec2.stop_instances(InstanceIds=instance_ids)
    print(f"Stopped instances: {instance_ids}")
    
    return {
        'statusCode': 200,
        'body': f"Stopped instances: {instance_ids}"
    }
