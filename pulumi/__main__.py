import pulumi
import pulumi_aws as aws

# Create a new IAM role for the Lambda function
role = aws.iam.Role('lambda-role',
    assume_role_policy="""{
        "Version": "2012-10-17",
        "Statement": [
            {
                "Action": "sts:AssumeRole",
                "Effect": "Allow",
                "Principal": {
                    "Service": "lambda.amazonaws.com"
                }
            }
        ]
    }""",
)

# Attach a basic execution policy to the role
aws.iam.RolePolicyAttachment('lambda-policy',
    policy_arn='arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole',
    role=role,
)

# Create a new Lambda function
function = aws.lambda_.Function('civo-batch',
    code=pulumi.AssetArchive({
        '.': pulumi.FileArchive('../lambdas/civo/my-deployment-package.zip'),
    }),
    handler='civo.lambda_handler',
    role=role.arn,
    runtime='python3.8',
    timeout=30,
)