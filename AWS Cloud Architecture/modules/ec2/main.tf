resource "aws_instance" "test-instance" {
  ami           = var.ec2_ami_id
  instance_type = var.ec2_instance_type
  subnet_id     = var.ec2_subnet_id
  key_name      = var.ec2_key_name
  vpc_security_group_ids = [var.security_group_id]
  tags = {
    Name = var.ec2_instance_name
    Environment = var.ec2_environment
  }
}