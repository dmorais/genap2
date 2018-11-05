# genap2
Scripts to install and manage Galaxy on GenAP2

## Galaxy-install-playbook
### Container Set up and Galaxy install

This is a set of Ansible playbooks to provision a LXC CentOS 7 container
and install the latest Galaxy version on the server. Furthermore, there
are playbooks to install/manage ngnix, postgres, supervisord and conda.


### Requirements
These roles require ansible ansible 2.6.2 or higher and images with 
CentOS 7 or higher.


## Playbooks

There are several playbooks to run and their order matters during 
installation.

* **addkey.yml** - Adds pub key to list of host 

* **main.yml** - This is the first playbook to be ran. It coordinated the
calling of other roles. After the main is finished you should have the
Galaxy user created, postgres, nginx and supervisord installed and
configured, and uwsgi installed.

* **manage-galaxy-with-supervisor.yml** -This playbook has functions to 
start/stop supervisord and ngnix, and to start/stop/restart Galaxy or an
specific Galaxy handler.

* **post_tool-installation.yml** - This playbook is run after the whole 
installation is done and the samtools package version (16,18,19) has been
installed. It also requires an admin API key created from the Galaxy UI. 
It performs a series of setup  and copies the genome loc files and chromossome
lenght to the Galaxy server.


### Role Variables
A temple of variables is provided on group_vars and host_vars



# How to Run


Configure the OS and install Galaxy
```
ansible-playbook main.yml
```

Once installed start supervisor
```
ansible-playbook manage-galaxy-with-supervisor.yml --tags "supervisor-start, stat"
```
The stat tags gives the output of the command. Galaxy should start automatically when supervisord stats.
 

Start/stop/restart Galaxy
```
ansible-playbook manage-galaxy-with-supervisor.yml --tags "galaxy-start, stat"
ansible-playbook manage-galaxy-with-supervisor.yml --tags "galaxy-stop, stat"
ansible-playbook manage-galaxy-with-supervisor.yml --tags "galaxy-resstart, stat"
```

Once Galaxy has been started create an admin user and an API they for this user.
Add the API key to the host_var template and intall samtools package version 16, 18, 19

Now run the post-tool-installation.yml
```
ansible-playbook post-tool-installation.yml
```