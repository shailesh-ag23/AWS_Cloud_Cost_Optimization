import json
import boto3
from decimal import Decimal


dynamodb = boto3.resource("dynamodb")

table = dynamodb.Table("scan-results")


class DecimalEncoder(json.JSONEncoder):

    def default(self, obj):

        if isinstance(obj, Decimal):
            return float(obj)

        return json.JSONEncoder.default(self, obj)


def lambda_handler(event, context):

    response = table.scan()

    items = response["Items"]

    if not items:

        return {

            "statusCode": 200,

            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },

            "body": json.dumps({
                "message": "No scan data available"
            })
        }

    sorted_items = sorted(

        items,

        key=lambda x: x["timestamp"],

        reverse=True
    )

    latest_scan = sorted_items[0]

    total_savings = sum(

        float(item["total_savings"])

        for item in items
    )

    result = {

        "latest_scan_time": latest_scan["timestamp"],

        "latest_estimated_savings":
            latest_scan["total_savings"],

        "historical_total_savings":
            round(total_savings, 2),

        "resources_analyzed":
            len(latest_scan["findings"]),

        "optimization_candidates":

            len([

                item for item in latest_scan["findings"]

                if item["potential_savings"] > 0
            ])
    }

    return {

        "statusCode": 200,

        "headers": {

            "Content-Type": "application/json",

            "Access-Control-Allow-Origin": "*"
        },

        "body": json.dumps(
            result,
            cls=DecimalEncoder
        )
    }