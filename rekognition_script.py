import boto3

# Initialize the Rekognition client
rekognition = boto3.client('rekognition')

# Function to detect labels in an image
def detect_labels(bucket, photo):
    response = rekognition.detect_labels(
        Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
        MaxLabels=10
    )
    print('Detected labels for ' + photo)    
    for label in response['Labels']:
        print(label['Name'] + ' : ' + str(label['Confidence']))

# Main function
def main():
    bucket = 'myrekognitionbucket11'  # Replace with your S3 bucket name
    photo = '11.jpg'  # Replace with the name of your image in the S3 bucket
    detect_labels(bucket, photo)

if __name__ == "__main__":
    main()
