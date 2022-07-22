import boto3
from tkinter import *
window=Tk()
window.geometry('700x500')
Label(window,text="*****Hello, please make a choice !!!! *****",font=('Arial','14','bold')).grid(row=0,column=0)
Label(window,text="*******************************************",font=('Arial','14','bold')).grid(row=1,column=0)
window.title('AWS manager')
ec2=boto3.resource("ec2",region_name="eu-north-1")





    
USER_DATA_Amazon = '''#!/bin/bash
sudo yum update
sudo yum install -y httpd
sudo systemctl enable httpd 
sudo systemctl start httpd  
'''
USER_DATA_Ubuntu = '''#!/bin/bash
sudo apt update
sudo apt -y install apache2
sudo systemctl start apache2
sudo systemctl enable apache2
'''
def AmazonLinux():
    
    security_group=ec2.create_security_group(
        Description='Allow inbound traffic',
        GroupName='Allow ssh for Amazon Linux')
    security_group.authorize_ingress(
        CidrIp='0.0.0.0/0',
        FromPort=22,
        ToPort=22,
        IpProtocol='tcp')
    instance = ec2.create_instances(
        
        ImageId='ami-0917076ab9780844d',
        MaxCount =1,
        MinCount=1,
        KeyName='Test',
        SecurityGroupIds=[security_group.id,],
        InstanceType='t3.micro',
        TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Amazon'
                },
            ]
        },
    ])
    instance[0].wait_until_running()
    instance[0].reload()
    ip = instance[0].public_ip_address
    Label(window,text="                                           ").grid(row=25,column=0)
    Label(window,text="Istance was successfully created with ip"+ip).grid(row=25,column=0)
    
    
def Ubuntu():
    
    security_group=ec2.create_security_group(
         Description='Allow inbound traffic',
        GroupName='Allow ssh for Ubuntu')
    security_group.authorize_ingress(
        CidrIp='0.0.0.0/0',
        FromPort=22,
        ToPort=22,
        IpProtocol='tcp')
    instance = ec2.create_instances(
       
        ImageId='ami-012ae45a4a2d92750',
        MaxCount =1,
        MinCount=1,
        KeyName='Test',
        SecurityGroupIds=[security_group.id,],
        InstanceType='t3.micro',
        TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Ubuntu 20.04.LTS'
                },
            ]
        },
    ])
    instance[0].wait_until_running()
    instance[0].reload()
    ip = instance[0].public_ip_address
    Label(window,text="                                           ").grid(row=25,column=0)
    Label(window,text="Istance was successfully created with ip"+ip).grid(row=25,column=0)
def UbuntuWeb():
    
    security_group=ec2.create_security_group(
         Description='Allow inbound traffic',
        GroupName='Allow ssh&http for Ubuntu')
    security_group.authorize_ingress(
        CidrIp='0.0.0.0/0',
        FromPort=22,
        ToPort=22,
        IpProtocol='tcp')
    security_group.authorize_ingress(
        CidrIp='0.0.0.0/0',
        FromPort=80,
        ToPort=80,
        IpProtocol='tcp')

    instance = ec2.create_instances(
        
        ImageId='ami-012ae45a4a2d92750',
        MaxCount =1,
        MinCount=1,
        KeyName='Test',
        SecurityGroupIds=[security_group.id,],
        UserData=USER_DATA_Ubuntu,
        InstanceType='t3.micro',
        TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Ubuntu WEB_Server'
                },
            ]
        },
    ])
    instance[0].wait_until_running()
    instance[0].reload()
    ip = instance[0].public_ip_address
    Label(window,text="                                           ").grid(row=25,column=0)
    Label(window,text="Istance was successfully created with ip"+ip).grid(row=25,column=0)

def AmazonLinuxWeb():
    
    security_group=ec2.create_security_group(
        Description='Allow inbound traffic',
        GroupName='Allow ssh&http for Amazon Linux')
    security_group.authorize_ingress(
        CidrIp='0.0.0.0/0',
        FromPort=22,
        ToPort=22,
        IpProtocol='tcp')
    
    security_group.authorize_ingress(
        CidrIp='0.0.0.0/0',
        FromPort=80,
        ToPort=80,
        IpProtocol='tcp')

    instance = ec2.create_instances(
        
        ImageId='ami-0917076ab9780844d',
        MaxCount =1,
        MinCount=1,
        KeyName='Test',
        SecurityGroupIds=[security_group.id,],
        UserData=USER_DATA_Amazon,
        InstanceType='t3.micro',
        TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'Amazon Linux WEB_Server'
                },
            ]
        },
    ])
    instance[0].wait_until_running()
    instance[0].reload()
    ip = instance[0].public_ip_address
    Label(window,text="                                           ").grid(row=25,column=0)
    Label(window,text="Istance was successfully created with ip"+ip,font=('Arial','14','bold')).grid(row=25,column=0)
    

Button(window,text="----      Run Ubuntu 20.04 LTS EC2 Instanse on AWS       ----",command=Ubuntu,bg="blue",fg="yellow",font=('Arial',14)).grid(row=5,column=0)
Button(window,text="----Run Ubuntu 20.04 with WEB Server (Apache2) LTS EC2 Instanse on AWS ----",command=UbuntuWeb,bg="yellow",fg="blue",font=('Arial',14)).grid(row=10,column=0)
Button(window,text="----      Run Amazon Linux 2 AMI EC2 Instanse on AWS       ----",command=AmazonLinux,bg="blue",fg="yellow",font=('Arial',14)).grid(row=15,column=0)
Button(window,text="----Run Amazon Linux 2 AMI with WEB Server (httpd) EC2 Instanse on AWS ----",command=AmazonLinuxWeb, bg="yellow",fg="blue",font=('Arial',14)).grid(row=20,column=0)

window.mainloop()




