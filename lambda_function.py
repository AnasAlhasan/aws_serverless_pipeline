import json
import boto3

# Initialize the S3 client
s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    # --- 1. Get File Info from the Trigger Event ---
    
    # Get the bucket name from the event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    
    # Get the file name (key) from the event
    file_key = event['Records'][0]['s3']['object']['key']
    
    print(f"File uploaded: {file_key} from bucket: {bucket_name}")

    try:
        # --- 2. Read the Uploaded File ---
        
        # Get the file object from S3
        file_obj = s3.get_object(Bucket=bucket_name, Key=file_key)
        
        # Read the file's content
        file_content = file_obj['Body'].read().decode('utf-8')
        
        # --- 3. Analyze the File ---
        
        lines = file_content.split('\n')
        word_count = len(file_content.split())
        char_count = len(file_content)
        
        # Create a dictionary with the analysis
        analysis_result = {
            'source_file': file_key,
            'line_count': len(lines),
            'word_count': word_count,
            'character_count': char_count,
            'first_line': lines[0] if len(lines) > 0 else None
        }
        
        # --- 4. Save the Analysis to the Output Bucket ---
        
        # Define your output bucket
        output_bucket_name = '[your-unique-name]-output-analysis'
        
        # Define the new file name (e.g., "my_file.txt" -> "my_file.json")
        output_key = file_key.replace('.txt', '.json')
        
        # Save the analysis as a JSON string
        s3.put_object(
            Bucket=output_bucket_name,
            Key=output_key,
            Body=json.dumps(analysis_result, indent=2)
        )
        
        print(f"Successfully saved analysis to {output_key} in {output_bucket_name}")
        
        return {
            'statusCode': 200,
            'body': json.dumps('Analysis complete!')
        }
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error processing file: {str(e)}")
        }