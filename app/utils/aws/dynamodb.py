import boto3


resource = boto3.resource(
    'dynamodb',
    region_name='ap-southeast-1'
)

client = boto3.client(
    'dynamodb',
    region_name='ap-southeast-1'
)

table = resource.Table("PTE")
