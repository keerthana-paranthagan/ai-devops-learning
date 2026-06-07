import boto3
import json

client = boto3.client(
    service_name="bedrock-runtime",
    region_name="ap-south-1"
)

response = client.converse(
    modelId="anthropic.claude-3-haiku-20240307-v1:0",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "text": "Explain Terraform in one sentence."
                }
            ]
        }
    ]
)

print(json.dumps(response, indent=2, default=str))