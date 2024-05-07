variable "name" {
  description = "Value of the Name tag for the EC2 instance"
  type        = string
  default     = "DATA472-jre141-testserver"
}

variable "course" {
  description = "The course name"
  default     = "DATA472"
  type        = string

}

variable "username" {
  description = "The student or user name"
  default     = "jre141"
  type        = string

}