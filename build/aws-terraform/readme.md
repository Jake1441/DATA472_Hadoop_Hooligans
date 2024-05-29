# Set up AWS
To use your IAM credentials to authenticate the Terraform AWS provider, set the AWS_ACCESS_KEY_ID environment variable.
export AWS_ACCESS_KEY_ID=
export AWS_SECRET_ACCESS_KEY=

make sure to check variables.tf and make the changes you see fit.

Not everything has been added to variables but the plan is to update it eventually to require less configuration on main.tf.

Use the following commands in terraform

terraform validate
terraform apply 
type yes.

the instance will be created with the DATA472 group with
public facing ip using ubuntu.

If you truly trust terraform  you can use 
terraform apply --auto-approve.