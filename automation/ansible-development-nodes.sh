#!/bin/bash

# For Public Nodes
ansible-playbook -i inventory/ec2_external_development.py -u ubuntu --private-key ../credentials/KEY-PAIR-HERE.pem site_ubuntu.yml -e 'ansible_python_interpreter=/usr/bin/python3' -vv
ansible-playbook -i inventory/ec2_external_development.py -u centos --private-key ../credentials/KEY-PAIR-HERE.pem site_centos.yml -e 'ansible_python_interpreter=/usr/bin/python' -vv

# For Private Nodes
#ansible-playbook -i inventory/ec2_internal_development.py -u ubuntu --private-key ../credentials/KEY-PAIR-HERE.pem site_ubuntu.yml -e 'ansible_python_interpreter=/usr/bin/python3' -vv
#ansible-playbook -i inventory/ec2_internal_development.py -u centos --private-key ../credentials/KEY-PAIR-HERE.pem site_centos.yml -e 'ansible_python_interpreter=/usr/bin/python' -vv
