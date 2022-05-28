'''
Create venv
python3 -m venv venv 
.\venv\Scripts\activate
pip3 install boto3
pip3 install pyyaml
'''

import boto3
import yaml
import sys


def create_instances(env):
    #print(int(env['Total_Instance']), env['ImageId'], env['AWS_ACCESS_ID'], env['AWS_SECRET_KEY'])
    conn = boto3.client('ec2', aws_access_key_id=env['AWS_ACCESS_ID'], aws_secret_access_key=env['AWS_SECRET_KEY'])
    for i in range( int(env['Total_Instance']) ):
        reservation = conn.run_instances(ImageId=env['ImageId'],
                                        KeyName=env['KeyName'],
                                        InstanceType=env['InstanceType'],
                                        MinCount=env['MinCount'],
                                        MaxCount=env['MaxCount'],
                                        SecurityGroupIds=env['SecurityGroupIds'],                                
                                        SubnetId = env['SubnetId'],
                                        UserData=open(env['userData']).read())

if __name__ == "__main__":
    try:
        conf_data = yaml.safe_load(open("EC2\config.yaml", "r").read())
        for env in conf_data:
            create_instances(conf_data[env])
    except yaml.YAMLError as exc:
        print(exc)