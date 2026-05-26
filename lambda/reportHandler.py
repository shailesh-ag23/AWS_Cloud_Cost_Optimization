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

            "statusCode": 404,

            "headers": {
                "Content-Type": "application/json",
                "Access-Control-Allow-Origin": "*"
            },

            "body": json.dumps({
                "message": "No reports found"
            })
        }

    # Sort by timestamp descending

    sorted_items = sorted(

        items,

        key=lambda x: x["timestamp"],

        reverse=True
    )

    latest_report = sorted_items[0]

    findings = latest_report["findings"]

    total_savings = latest_report["total_savings"]

    optimization_candidates = len([

        item for item in findings

        if item["potential_savings"] > 0
    ])

    result = {

        "report_summary": {

            "scan_time": latest_report["timestamp"],

            "estimated_savings": total_savings,

            "resources_analyzed": len(findings),

            "optimization_candidates": optimization_candidates
        },

        "findings": findings
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