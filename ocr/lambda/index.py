import json
import boto3
import os
from easyocr import Reader

# Initialize the reader object outside of the handler to leverage Lambda's container reuse
reader = Reader(['fr'])

def lambda_handler(event, context):
    # Assumes that the event contains the S3 bucket name and image key
    s3_bucket = event['s3_bucket']
    s3_key = event['s3_key']
    result_txt = '/tmp/result_bultin.txt'  # Use /tmp directory for Lambda write permissions

    # Download the image from S3 to the local filesystem
    s3_client = boto3.client('s3')
    s3_client.download_file(s3_bucket, s3_key, '/tmp/bultin.jpg')
    
    # Perform OCR on the downloaded image
    result = reader.readtext('/tmp/bultin.jpg')
    
    # Write the OCR results to a file
    with open(result_txt, 'w', encoding='utf-8') as f:
        for res in result:
            f.write(res[1] + '\n')
    
    # Upload the result file back to S3 (or you can return the results)
    # For this example, we'll assume the output should go to the same bucket but with a different key
    output_key = s3_key + '_result.txt'
    s3_client.upload_file(result_txt, s3_bucket, output_key)

    # Return a response
    return {
        'statusCode': 200,
        'body': json.dumps('OCR results written to: ' + output_key)
    }
