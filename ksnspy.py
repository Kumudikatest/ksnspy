import boto3
sns = boto3.client("sns")

def handler(event, context):
    try:
        data = sns.publish(
            Message="test",
            TopicArn="arn:aws:sns:us-east-1:{}:knewsns".format(environ["SIGMA_AWS_ACC_ID"]),
            MessageStructure="String",
            MessageAttributes={}
        )
    except BaseException as e:
        print(e)
        raise(e)
    
    return {"message": "Successfully executed"}
