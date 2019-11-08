#!/bin/bash
ansible-playbook -i inventory/ec2_external_production.py -u ubuntu --private-key ../credentials/KEY-PAIR-HERE.pem site.yml -e 'ansible_python_interpreter=/usr/bin/python3' -vv
