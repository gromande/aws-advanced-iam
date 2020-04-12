import boto3, sys

account_id = sys.argv[1]
role_name = sys.argv[2]
key_id = sys.argv[3]
key = sys.argv[4]

role_info = {
    'RoleArn': f"arn:aws:iam::{account_id}:role/{role_name}",
    'RoleSessionName': f"{role_name}Session"
}

client = boto3.client(
    'sts',
    aws_access_key_id=key_id,
    aws_secret_access_key=key
)

credentials = client.assume_role(**role_info)

session = boto3.session.Session(
    aws_access_key_id=credentials['Credentials']['AccessKeyId'],
    aws_secret_access_key=credentials['Credentials']['SecretAccessKey'],
    aws_session_token=credentials['Credentials']['SessionToken']
)

s3 = session.resource('s3')

# Print out bucket names
for bucket in s3.buckets.all():
    print("Bucket name: {}".format(bucket.name))