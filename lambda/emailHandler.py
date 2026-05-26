import boto3


ses = boto3.client("ses")


def lambda_handler(event, context):

    total_savings = event.get(
        "total_savings",
        "Unknown"
    )

    resources = event.get(
        "resources_analyzed",
        "Unknown"
    )

    response = ses.send_email(

        Source="kavithagandhiraj27@gmail.com",

        Destination={
            "ToAddresses": [
                "kavithagandhiraj27@gmail.com"
            ]
        },

        Message={

            "Subject": {
                "Data":
                    "AWS Optimization Report"
            },

            "Body": {

                "Text": {

                    "Data": f'''

Optimization Scan Completed

Resources Analyzed: {resources}

Potential Savings:
₹{total_savings}

Your AWS infrastructure
has been analyzed successfully.
'''
                }
            }
        }
    )

    return {

        "statusCode": 200,

        "messageId":
            response["MessageId"]
    }