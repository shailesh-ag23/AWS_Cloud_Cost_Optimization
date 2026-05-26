import json
import boto3
from datetime import datetime, timedelta
import uuid
from decimal import Decimal

# AWS Clients

ec2 = boto3.client("ec2")
cloudwatch = boto3.client("cloudwatch")
dynamodb = boto3.resource("dynamodb")
lambda_client = boto3.client("lambda")


table = dynamodb.Table("scan-results")
scan_id = str(uuid.uuid4())

# Estimated Monthly Pricing (Approximate)

INSTANCE_PRICING = {
    "t2.micro": 8,
    "t2.small": 15,
    "t3.micro": 9,
    "t3.small": 16,
    "t3.medium": 30,
    "t3.large": 60
}


# ---------------------------------------------------
# Get Average CPU Utilization from CloudWatch
# ---------------------------------------------------
def convert_floats(obj):

    if isinstance(obj, float):

        return Decimal(str(obj))

    elif isinstance(obj, list):

        return [

            convert_floats(item)

            for item in obj
        ]

    elif isinstance(obj, dict):

        return {

            key: convert_floats(value)

            for key, value in obj.items()
        }

    return obj
def get_average_cpu(instance_id):

    end_time = datetime.utcnow()
    start_time = end_time - timedelta(days=7)

    metrics = cloudwatch.get_metric_statistics(

        Namespace="AWS/EC2",

        MetricName="CPUUtilization",

        Dimensions=[
            {
                "Name": "InstanceId",
                "Value": instance_id
            }
        ],

        StartTime=start_time,
        EndTime=end_time,

        Period=86400,

        Statistics=["Average"]
    )

    datapoints = metrics["Datapoints"]

    if not datapoints:
        return 0

    total_cpu = sum(point["Average"] for point in datapoints)

    average_cpu = total_cpu / len(datapoints)

    return round(average_cpu, 2)


# ---------------------------------------------------
# Main Lambda Handler
# ---------------------------------------------------

def lambda_handler(event, context):

    findings = []

    total_savings = 0

    print("Starting EC2 optimization scan...")

    # Get EC2 Instances

    response = ec2.describe_instances()

    reservations = response["Reservations"]

    for reservation in reservations:

        for instance in reservation["Instances"]:

            instance_id = instance["InstanceId"]

            instance_type = instance["InstanceType"]

            instance_state = instance["State"]["Name"]

            print(f"Analyzing Instance: {instance_id}")

            # Get CPU Metrics

            average_cpu = get_average_cpu(instance_id)

            print(f"Average CPU: {average_cpu}")

            # Estimated Monthly Cost

            monthly_cost = INSTANCE_PRICING.get(
                instance_type,
                25
            )

            recommendation = "Healthy"

            potential_savings = 0

            severity = "LOW"

            # ---------------------------------------------------
            # Optimization Rules
            # ---------------------------------------------------

            # Rule 1 — Stopped Instances

            if instance_state == "stopped":

                recommendation = (
                    "Terminate unused stopped instance"
                )

                potential_savings = monthly_cost

                severity = "HIGH"

            # Rule 2 — Low CPU Utilization

            elif average_cpu < 5:

                recommendation = (
                    "Downsize instance to smaller type"
                )

                potential_savings = round(
                    monthly_cost * 0.5,
                    2
                )

                severity = "MEDIUM"

            # Rule 3 — Moderate Utilization

            elif average_cpu < 20:

                recommendation = (
                    "Monitor for possible rightsizing"
                )

                potential_savings = round(
                    monthly_cost * 0.2,
                    2
                )

                severity = "LOW"

            # Add Savings

            total_savings += potential_savings

            # Store Finding

            findings.append({

                "instance_id": instance_id,

                "instance_type": instance_type,

                "state": instance_state,

                "average_cpu": average_cpu,

                "estimated_monthly_cost": monthly_cost,

                "recommendation": recommendation,

                "potential_savings": potential_savings,

                "severity": severity
            })

    # ---------------------------------------------------
    # Final Response
    # ---------------------------------------------------

    result = {

        "scan_summary": {

            "resources_analyzed": len(findings),

            "estimated_total_savings": round(
                total_savings,
                2
            ),

            "optimization_candidates": len(
                [
                    item for item in findings
                    if item["potential_savings"] > 0
                ]
            )
        },

        "findings": findings
    }

    print("EC2 optimization scan completed.")
    table.put_item(

    Item={

        "scan_id": scan_id,

        "timestamp": datetime.utcnow().isoformat(),

        "total_savings": str(total_savings),

        "findings": convert_floats(findings)
    }
)



    lambda_client.invoke(

    FunctionName=
        "emailHandler",

    InvocationType="Event",

    Payload=json.dumps({

        "total_savings":
            float(total_savings),

        "resources_analyzed":
            len(findings)
    }))
    return {

        "statusCode": 200,

        "headers": {

            "Content-Type": "application/json",

            "Access-Control-Allow-Origin": "*"
        },

        "body": json.dumps(result)
    }