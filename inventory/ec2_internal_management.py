#!/usr/local/bin/python3
import boto3
import json

# AnsibleRole tag = Ansible Group Name
aptly_group=[]
arangodbmaster_group=[]
arangodbnode_group=[]
centos_group=[]
chefserver_group=[]
chefworkstation_group=[]
consul_group=[]
dnsforwarder_group=[]
elasticsearchmaster_group=[]
elasticsearchnode_group=[]
flink_group=[]
gitlab_group=[]
hadoop_group=[]
influxdb_group=[]
jenkinsmaster_group=[]
jenkinsnode_group=[]
kafka_group=[]
kubernetes_group=[]
nginx_group=[]
nifi_group=[]
openvpn_group=[]
pki_group=[]
rundeck_group=[]
sample_group=[]
sonarqube_group=[]
spark_group=[]
ubuntu_group=[]
vault_group=[]
zookeeper_group=[]

# Retrieve Hosts Based on AnsibleRole tag, Environment (management,development,staging,prod)
def get_hosts(ec2,fv):
    f = [{'Name':'tag:AnsibleRole', 'Values':[fv]},{'Name':'tag:env', 'Values':['management']}]
    hosts = []
    for each_in in ec2.instances.filter(Filters=f):
        if each_in.private_ip_address is not None:
            hosts.append(each_in.private_ip_address)
    return hosts

def  main():
    ec2 = boto3.resource("ec2")
    aptly_group = get_hosts(ec2,"aptly")
    arangodbmaster_group = get_hosts(ec2,"arangodbmaster")
    arangodbnode_group = get_hosts(ec2,"arangodbnode")
    centos_group = get_hosts(ec2,"centos")
    chefserver_group= get_hosts(ec2,"chefserver")
    chefworkstation_group= get_hosts(ec2,"chefworkstation")
    consul_group = get_hosts(ec2,"consul")
    dnsforwarder_group = get_hosts(ec2,"dnsforwarder")
    elasticsearchmaster_group = get_hosts(ec2,"elasticsearchmaster")
    elasticsearchnode_group = get_hosts(ec2,"elasticsearchnode")
    flink_group = get_hosts(ec2,"flink")
    gitlab_group = get_hosts(ec2,"gitlab")
    hadoop_group = get_hosts(ec2,"hadoop")
    influxdb_group = get_hosts(ec2,"influxdb")
    jenkinsmaster_group = get_hosts(ec2,"jenkinsmaster")
    jenkinsnode_group = get_hosts(ec2,"jenkinsnode")
    kafka_group = get_hosts(ec2,"kafka")
    kubernetes_group = get_hosts(ec2,"kubernetes")
    nginx_group = get_hosts(ec2,"nginx")
    nifi_group = get_hosts(ec2,"nifi")
    openvpn_group = get_hosts(ec2,"openvpn")
    pki_group = get_hosts(ec2,"pki")
    rundeck_group = get_hosts(ec2,"rundeck")
    sample_group = get_hosts(ec2,"sample")
    sonarqube_group = get_hosts(ec2,"sonarqube")
    spark_group = get_hosts(ec2,"spark")
    vault_group = get_hosts(ec2,"vault")
    ubuntu_group = get_hosts(ec2,"ubuntu")
    zookeeper_group = get_hosts(ec2,"zookeeper")
    all_groups = {
    'aptly': {'hosts': aptly_group, 'vars': {'group_name': 'Aptly Group'}},
    'arangodbmaster': {'hosts': arangodbmaster_group, 'vars': {'group_name': 'Arangodb Master Group'}},
    'arangodbnode': {'hosts': arangodbnode_group, 'vars': {'group_name': 'Arangodb Node Group'}},
    'centos': {'hosts': centos_group, 'vars': {'group_name': 'Centos Group'}},
    'chefserver': {'hosts': chefserver_group, 'vars': {'group_name': 'Chef Server Group'}},
    'chefworkstation': {'hosts': chefworkstation_group, 'vars': {'group_name': 'Chef Workstation Group'}},
    'consul': {'hosts': consul_group, 'vars': {'group_name': 'Consul Group'}},
    'dnsforwarder': {'hosts': dnsforwarder_group, 'vars': {'group_name': 'Dns Forwarder Group'}},
    'elasticsearchmaster': {'hosts': elasticsearchmaster_group, 'vars': {'group_name': 'Elastic Search Master Group'}},
    'elasticsearchnode': {'hosts': elasticsearchnode_group, 'vars': {'group_name': 'Elastic Search Node Group'}},
    'flink': {'hosts': flink_group, 'vars': {'group_name': 'Flink Group'}},
    'gitlab': {'hosts': gitlab_group, 'vars': {'group_name': 'Gitlab Group'}},
    'hadoop': {'hosts': hadoop_group, 'vars': {'group_name': 'Hadoop Group'}},
    'influxdb': {'hosts': influxdb_group, 'vars': {'group_name': 'Influxdb Group'}},
    'jenkinsmaster': {'hosts': jenkinsmaster_group, 'vars': {'group_name': 'Jenkins Master Group'}},
    'jenkinsnode': {'hosts': jenkinsnode_group, 'vars': {'group_name': 'Jenkins Node Group'}},
    'kafka': {'hosts': kafka_group, 'vars': {'group_name': 'Kafka Group'}},
    'kubernetes': {'hosts': kubernetes_group, 'vars': {'group_name': 'Kubernetes Group'}},
    'nginx': {'hosts': nginx_group, 'vars': {'group_name': 'Nginx Group'}},
    'nifi': {'hosts': nifi_group, 'vars': {'group_name': 'NiFi Group'}},
    'openvpn': {'hosts': openvpn_group, 'vars': {'group_name': 'OpenVPN Group'}},
    'pki': {'hosts': pki_group, 'vars': {'group_name': 'PKI Group'}},
    'rundeck': {'hosts': rundeck_group, 'vars': {'group_name': 'Rundeck Group'}},
    'sample': {'hosts': sample_group, 'vars': {'group_name': 'Sample Group'}},
    'sonarqube': {'hosts': sonarqube_group, 'vars': {'group_name': 'SonarQube Group'}},
    'spark': {'hosts': spark_group, 'vars': {'group_name': 'Spark Group'}},
    'ubuntu': {'hosts': ubuntu_group, 'vars': {'group_name': 'Ubuntu Group'}},
    'vault': {'hosts': vault_group, 'vars': {'group_name': 'Vault Group'}},
    'zookeeper': {'hosts': zookeeper_group, 'vars': {'group_name': 'Zookeeper Group'}}
    }
    print(json.dumps(all_groups))

if __name__=="__main__":
    main()
