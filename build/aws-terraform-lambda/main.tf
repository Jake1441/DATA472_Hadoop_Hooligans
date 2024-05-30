data "archive_file" "lambda" {
  type        = "zip"
  source_file = "jre141-api-lambda-code.py"
  output_path = "lambda_function_payload.zip"
}

resource "aws_lambda_function" "test_lambda" {
  # If the file is not in the current working directory you will need to include a
  # path.module in the filename.
  filename      = "lambda_function_payload.zip"
  function_name = "data472-jre141-terraform-lambda-test"
  role          = "arn:aws:iam::454456403374:role/DATA472-Lambda"
  handler       = "jre141-api-lambda-code.lambda_handler"
  
  source_code_hash = data.archive_file.lambda.output_base64sha256
  timeout = "123"
  runtime = "python3.12"
  tags = {
    UserName = "jre141"
  }
  environment {
    variables = {
      foo = "bar"
    }

  }
  
}

