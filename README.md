

# AWS Serverless Data Pipeline

This project is an event-driven, serverless data pipeline on AWS. 

When a `.txt` file is uploaded to an S3 input bucket, an S3 event notification triggers a Python Lambda function. The function analyzes the text file to count words, lines, and characters, then saves this analysis as a new `.json` file in a separate S3 output bucket.

## 🏛️ Architecture

[Upload File] -> [S3 Input Bucket] -> [S3 Event Trigger] -> [Lambda Function] -> [S3 Output Bucket] -> [Analysis.json]

## 🛠️ Services Used
* **AWS S3:** Used for object storage. Two buckets were created: one for input and one for output.
* **AWS Lambda:** Used for serverless compute. The Python function contains all the logic for processing the file.
* **AWS IAM:** Used to create a secure, least-privilege policy to ensure the Lambda function could *only* read from the input bucket and write to the output bucket.

## 🚀 How to Recreate This Project

1.  **Create S3 Buckets:** Create two S3 buckets: `[your-input-bucket]` and `[your-output-bucket]`.
2.  **Create IAM Policy:** Create a new IAM policy using the code in `iam_policy.json`. Remember to replace the bucket names in the policy with your own.
3.  **Create Lambda Function:**
    * Create a new Python Lambda function.
    * Attach the IAM policy you just created to the function's execution role.
    * Copy the code from `lambda_function.py` into the Lambda code editor. Remember to update the `output_bucket_name` variable in the code.
4.  **Create S3 Trigger:** In the Lambda console, add an S3 trigger.
    * Set the source bucket to your input bucket.
    * Set the event type to "All object create events".
    * Set the suffix to `.txt` to only trigger for text files.
5.  **Test:** Upload a `.txt` file to your input bucket. A corresponding `.json` analysis file should appear in your output bucket moments later.
>>>>>>> 4b4b7d014878d9c2e568639aacf38e2c9ec0c6c5
