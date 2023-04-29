import os
import boto3 

ses = boto3.client('ses',
                   region_name=os.environ.get('AWS_REGION'),
                   aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
                   aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
                   )

message = {
    'Source': 'love@frankz.hu', 
    'Destination': {
        'ToAddresses': [
            'token@perprompt.com',
        ],
        'BccAddresses': [
            'zendosoul@gmail.com',
        ]
    }, 
    'Subject': { 
        'Data': 'new post just dropped from stretcht' 
    }, 
    'MessageBody': { 
        'Text': { 
            'Data': os.environ.get('event') 
        } 
    } 
}

response = ses.send_email(
    Source=message['Source'], 
    Destination=message['Destination'], 
    Message={
        'Subject': message['Subject'], 
        'Body': message['MessageBody'] 
    } 
)
