import json
import boto3

rekognition = boto3.client('rekognition')

def lambda_handler(event, context):
    try:
        body = json.loads(event["body"])
        bucket = body["bucket"]
        key = body["key"]

        # Call Rekognition to detect faces
        response = rekognition.detect_faces(
            Image={'S3Object': {'Bucket': bucket, 'Name': key}},
            Attributes=['ALL']
        )

        # Check if face detected
        if not response['FaceDetails']:
            message = "No face detected in the image."
        else:
            face = response['FaceDetails'][0]
            emotions = face['Emotions']
            top_emotion = max(emotions, key=lambda e: e['Confidence'])

            message = f"Detected a face showing {top_emotion['Type']} with {round(top_emotion['Confidence'], 1)}% confidence."

        return {
            "statusCode": 200,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": message})
        }

    except Exception as e:
        return {
            "statusCode": 400,
            "headers": {"Access-Control-Allow-Origin": "*"},
            "body": json.dumps({"message": str(e)})
        }
