#!/usr/local/bin/python3

import boto3
import json


sample_group=[]
openvpn_group=[]
ipaserver_group=[]
aptlyserver_group=[]
vaultserver_group=[]
gitlabserver_group=[]


def get_hosts(ec2,fv):
    f = {'Name':'tag:AnsibleRole', 'Values':[fv]}
    hosts = []
    for each_in in ec2.instances.filter(Filters=[f]):
        if each_in.private_ip_address is not None:
            hosts.append(each_in.private_ip_address)
    return hosts


def  main():
    ec2 = boto3.resource("ec2")
    sample_group = get_hosts(ec2,"sample")
    openvpn_group = get_hosts(ec2, "openvpn")
    ipaserver_group = get_hosts(ec2, "ipaserver")
    aptlyserver_group = get_hosts(ec2,"aptlyserver");
    vaultserver_group = get_hosts(ec2,"vaultserver");
    gitlabserver_group = get_hosts(ec2,"gitlabserver");

    all_groups = {
    'sample': {'hosts': sample_group, 'vars': {'group_name': 'Sample Group'}},
    'openvpn': {'hosts': openvpn_group, 'vars': {'group_name': 'Openvpn Group'}},
    'ipaserver': {'hosts': ipaserver_group, 'vars': {'group_name': 'IPAServer Group'}},
    'aptlyserver': {'hosts': aptlyserver_group, 'vars': {'group_name': 'Aptly Server Group'}},
    'vaultserver': {'hosts': vaultserver_group, 'vars': {'group_name': 'Vault Server Group'}},
    'gitlabserver': {'hosts': gitlabserver_group, 'vars': {'group_name': 'Gitlab Server Group'}}
    }

    print(json.dumps(all_groups))


if __name__=="__main__":
    main()
