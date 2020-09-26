import argparse
import aws

parser = argparse.ArgumentParser()

parser.add_argument("--provider", default=True)

args = parser.parse_args()

if args.provider == "aws":
    aws.iamport()
