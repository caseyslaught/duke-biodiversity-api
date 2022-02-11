
from RainforestApi.common.aws import get_boto_client


def put_s3_item(body, bucket, object_key):

    client = get_boto_client('s3')
    res = client.put_object(Body=body, Bucket=bucket, Key=object_key)

