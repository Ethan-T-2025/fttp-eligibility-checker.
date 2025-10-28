#!/bin/bash

while IFS= read -r address; do
  echo "Checking: $address"
  result=$(python3 check_nbn_eligibility.py "$address")

  echo "Result: $result"

  if [[ "$result" == *"Eligible for FTTP"* ]]; then
    echo "Sending email for $address"
    echo "Your address $address is eligible for FTTP upgrade!" | mail -s "FTTP Upgrade Available" user@example.com
  fi
done < addresses.txt
