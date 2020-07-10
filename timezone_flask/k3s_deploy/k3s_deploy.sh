#!/bin/bash

# andrew@openmarmot.com
# last update July 08 2020
# this pulls some data for variables 
# and then parses the yaml file replacing env variable references with actual 
# values

set -e

#aws account number
export aws_account="$(aws sts get-caller-identity --query Account --output text)"

eval "cat <<EOF
$(<$1)
EOF
" | kubectl apply -f -