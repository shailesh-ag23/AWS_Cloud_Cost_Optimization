AWS Cost Optimization & Infrastructure Analytics Platform  

✨ Introduction  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Cloud infrastructure gives organizations incredible scalability and flexibility, but it also introduces one of the biggest operational challenges in modern engineering:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;⚠️ Uncontrolled cloud spending  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Many companies unknowingly pay for:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🚩 underutilized EC2 instances  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🚩 idle infrastructure  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🚩 oversized workloads  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🚩 inefficient resource allocation  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🚩 unused cloud resources  


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Without proper monitoring and optimization, these inefficiencies can significantly increase operational costs over time.  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🟢 To solve this real-world problem, I built a fully serverless:  AWS Cost Optimization & Infrastructure Analytics Platform . This platform automatically scans AWS infrastructure, analyzes EC2 utilization using CloudWatch metrics, identifies optimization opportunities, estimates potential savings, stores historical analytics, and generates automated reports using a scalable event-driven architecture.

✨ Architecture Diagram  

<img width="1177" height="799" alt="Screenshot 2026-05-26 223532" src="https://github.com/user-attachments/assets/deaba6e4-6fb7-48d4-ab42-1fabc3b75c5f" />  

The system continuously:  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ scans AWS infrastructure  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ analyzes CPU utilization  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ identifies optimization candidates  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ estimates potential savings  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ stores historical reports  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ sends automated optimization notifications  

✨ Services Used  

🌨️ Amazon S3 (Static Website Hosting)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Amazon S3 is used to host your frontend files:  
  	&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index.html  
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;index.css  
		&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;script.js  

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It acts as a static file server.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✔ Stores files  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;✔ Serves website content

🌨️ CloudFront (CDN)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;CloudFront is a Content Delivery Network (CDN).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Purpose:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Speeds up website globally  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Caches static content  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Reduces latency  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Instead of loading from one region, users get content from nearest edge location.  

🌨️ API Gateway  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;API Gateway acts as a bridge between frontend and backend.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Exposes HTTP endpoint (/visits)  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Routes requests to Lambda  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Handles request/response formatting  

🌨️ AWS Lambda  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Lambda is a serverless backend compute.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Runs code only when triggered  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Handles visitor count logic  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Connects to DynamoDB, Event Bridge

🌨️ DynamoDB  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;DynamoDB is a NoSQL database used here to store : EC2 optimization details  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Attributes:    
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;scan_id, timestamp, total_savings, findings  

🌨️ EventBridge  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Amazon EventBridge is used to automate infrastructure scanning workflows. Triggers daily EC2 optimization scans using scheduled rules.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It acts as an event-driven scheduler.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Automates scan execution  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Triggers Lambda functions  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Enables event-driven workflows   

🌨️ SES  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Amazon SES is used to send automated optimization reports and notifications. Sends infrastructure optimization reports directly to email.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It acts as a cloud-based email delivery service.   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Sends automated email alerts  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Delivers optimization reports  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Supports scalable email delivery  

🌨️ SNS  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Amazon SNS is used for real-time operational alerting and notifications. Sends alerts when failures or operational issues occur.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It acts as a distributed notification service.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Sends real-time alerts  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Integrates with CloudWatch alarms  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Supports email notifications  

🌨️ CloudWatch  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Amazon CloudWatch is used for monitoring, logging, and observability. Monitors Lambda executions, metrics, logs, and alarms.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It acts as a centralized monitoring platform.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Stores execution logs  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Tracks infrastructure metrics  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Monitors Lambda performance  

🌨️ IAM  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;AWS IAM is used to securely manage permissions and access control between AWS services. Controls secure access between Lambda, DynamoDB, SES, and APIs.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It acts as the security and authorization layer of AWS.  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Manages service permissions  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Implements least privilege access  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ✔ Secures AWS resources  

✨ Step-by-Step Deployment Guide  

Step 1: Upload Website to S3  

Create S3 bucket   
Allow public access for website files:  

<img width="1899" height="871" alt="Screenshot 2026-05-25 163305" src="https://github.com/user-attachments/assets/afc08003-4e8d-49c5-8832-45ded67292fb" />  

Removing Amazon S3 Block Public Access is generally not recommended. It should only be done if your specific use case explicitly requires making files or buckets available to the public over the internet  
Enable static website hosting  

Upload:  
index.html  
index.css  
script.js  

<img width="1919" height="869" alt="Screenshot 2026-05-26 190455" src="https://github.com/user-attachments/assets/25cee57b-3995-4bed-ac7b-82c2b38f72a6" />  

Step 2: Configure Bucket Policy  

Allow public access for website files:  
Enable public read access  
Add bucket policy for s3:GetObject  

<img width="1906" height="869" alt="Screenshot 2026-05-26 190700" src="https://github.com/user-attachments/assets/7c2f23b7-5a9c-44ce-80dd-ac889f130b3c" />  

Resource is your bucket ARN and it should end with /* which allows access to the objects inside your bucket  
Principal contains * signifies that anyone can access the bucket  

Step 3: Set up CloudFront CDN  

Create CloudFront distribution  
Set S3 bucket as origin  
Enable caching  

<img width="1907" height="868" alt="Screenshot 2026-05-26 191420" src="https://github.com/user-attachments/assets/3e6cfa62-4d2f-45dc-8136-c78992f59bd5" />

Step 4: Create DynamoDB Table  

Table name: scan-results  
Partition key: scan_id  
Add Attributes timestamp, total_savings, findings  

<img width="1902" height="871" alt="Screenshot 2026-05-26 192026" src="https://github.com/user-attachments/assets/12af5584-ffb1-454d-9095-40f39fb97893" />  

Step 5: Launch 2 EC2 instances  

AMI: Amazon Linux 2023 Kernel-6.1 AMI  
Instance Type: t3.micro  
Storage: 8 GiB General Purpose SSD ( gp3 )  
Instances: 2  

<img width="1916" height="871" alt="Screenshot 2026-05-26 192638" src="https://github.com/user-attachments/assets/e7658974-2c1d-410f-bb28-192f3e085228" />  

Step 5: ec2ScanLambda Function Creation  

The Lambda detects:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🔍 stopped instances  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🔍 low CPU utilization instances  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 🔍 underutilized workloads  

Main Components:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⚙️ ec2.describe_instances() - Get EC2 resources  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⚙️ cloudwatch.get_metric_statistics() - Pull CPU metrics  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⚙️ get_average_cpu() -	Calculate average utilization  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⚙️ Optimization logic -	Detects waste  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⚙️ Savings estimation -	Estimate monthly savings   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⚙️ table.put_item() - Updates the database with the obtained result  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⚙️ JSON response -	Returns API output  

Runtime: Python 3.14  
Attach policies ( AmazonDynamoDBFullAccess, CloudWatchFullAccess, AmazonEC2ReadOnlyAccess )  
Deploy and test  

Step 6: Set up API Gateway  

Create HTTP API  
Routes: /dashboard , /report  

<img width="1916" height="871" alt="Screenshot 2026-05-26 194957" src="https://github.com/user-attachments/assets/9dc291ae-d13e-43e0-ad4e-89460cdf070d" />  

In script.js set the DASHBOARD_API and REPORT_API with your api endpoints 

<img width="734" height="186" alt="Screenshot 2026-05-26 195340" src="https://github.com/user-attachments/assets/407f2af9-1b00-4cf1-a11a-b1e0b37ce907" />  

Reupload the script.js file in your s3 bucket  

⚠️ Note: Browsers block cross-origin requests.  
CORS -> configure -> Access-Control-Allow-Origin ( Add * )  
CORS allows resources from different domains to be loaded by browsers

Step 7: Create dashboardHandler and reportHandler lambda functions  

dashboardHandler Lambda Purpose:  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⚙️ reads historical scans from dynamodb  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⚙️ calculates trends based on it  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⚙️ returns dashboard analytics  

reportHandler Lambda Purpose:   
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⚙️ Returns optimization report when the user clicks the view report button  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ⚙️ Reads the details of the latest EC2 scan stored in dynamodb

Runtime: Python 3.14   
Attach policies ( AmazonDynamoDBFullAccess )  
Deploy and test  

In API Gateway,  attach the lambda functions to the API in the integrations section  

<img width="1904" height="871" alt="Screenshot 2026-05-26 201946" src="https://github.com/user-attachments/assets/8b1a5c35-37ba-4235-9ca6-e69585c8c7f9" />  

When the user clicks the view report button, reloads or visits the page, the script.js calls the api which further triggers the respective lambda function  

Step 8: Create EventBridge  

⚙️ EventBridge automatically triggers the ec2ScanLambda every 24 hrs   
⚙️ So that the Scanning of the resources occurs daily  

<img width="1901" height="870" alt="Screenshot 2026-05-26 203846" src="https://github.com/user-attachments/assets/7d52f327-14bd-402d-9f53-430c48a97367" />  

<img width="1899" height="865" alt="Screenshot 2026-05-26 203802" src="https://github.com/user-attachments/assets/f5f12bdf-ea3e-4e08-99d4-a412b2673899" />  

Step 9: Create SES  

⚙️ Send optimization reports automatically  
⚙️ Can send emails only between verified emails  

Create an identity ->  Enter the email address to verify ->  Verify the email  

<img width="1905" height="868" alt="Screenshot 2026-05-26 204642" src="https://github.com/user-attachments/assets/d39fd69c-33d3-4242-a3e4-66b3d91fc0e5" />  

Create an emailHandler lambda function  
emailHandler function is invoked by ec2ScanLambda  

⚙️ So the email is sent to the recipient every day  

Runtime: Python 3.14  
Attach policies ( AmazonSESFullAccess )  
Deploy and test  

⚠️ Note: ec2ScanLambda contains some code that invokes the emailHandler function  
Attach policy to ec2ScanLambda ( AWSLambda_FullAccess )  

<img width="1226" height="291" alt="Screenshot 2026-05-26 210212" src="https://github.com/user-attachments/assets/20d26a0a-ed97-4e17-a572-bbcd294ae426" />  

Step 10: Setting CloudWatch Alarms  

SNS -> Create Topic -> Create Subscription  

<img width="1905" height="869" alt="Screenshot 2026-05-26 210817" src="https://github.com/user-attachments/assets/219a36a6-a271-4c22-9d14-5ade2ed5e2c8" />  

⚙️ To Email When the lambda errors exceed the threshold  

CloudWatch -> Create alarm -> Select metric  

<img width="1916" height="875" alt="Screenshot 2026-05-26 211159" src="https://github.com/user-attachments/assets/0b889380-1c4a-47b0-a0d1-74599f69bebe" />  

Choose the SNS topic, so whenever the threshold is exceeded, an email is sent automatically  

<img width="1896" height="865" alt="Screenshot 2026-05-26 211356" src="https://github.com/user-attachments/assets/4dbe4eee-1d2a-4957-a95a-581b6a946a24" />

Lambda failure -> CloudWatch detects an error -> Alarm triggers -> SNS email alert sent  

✨ Future Improvements  

✅ multi-account AWS scanning  
✅ AWS Organizations integration  
✅ Kubernetes optimization  
✅ AI-powered recommendations  
✅ Amazon Bedrock integration  
✅ memory utilization analysis  
✅ advanced rightsizing engine  
✅ PDF report generation  
✅ real-time anomaly detection  

✨ Conclusion  

This project demonstrates how cloud-native serverless architectures can be used to automate infrastructure optimization, reduce operational costs, and improve cloud visibility.  
Instead of building a basic dashboard or CRUD application, this platform focuses on solving a real operational engineering problem using scalable AWS-native services and production-style cloud workflows.  

👨‍💻 Author  
Shailesh AG  
Computer Science Student | Cloud Engineer 

 






































