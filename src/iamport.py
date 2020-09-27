import argparse
import aws

parser = argparse.ArgumentParser()

parser.add_argument("-p", "--provider", default=True)

args = parser.parse_args()

if args.provider == "aws":
    aws.iamport()
else:
    print('Usage: $ python iamport.py [-p aws]')
