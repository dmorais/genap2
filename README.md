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


## How to run

There are several playbooks to run and their order matters during 
installation.

* **addkey.yml** - Adds pub key to list of host 

* **main.yml** - This is the first playbook to be ran. It coordinated the
calling of other roles. After the main is finished you should have the
Galaxy user created, postgres, nginx and supervisord installed and
configured, and uwsgi installed.


### Role Variables

#### Users
* host_home_dir: Galaxy user home dir
* host_galaxy_root_dir: base dir to all Galaxy files
* galaxy_user: Galaxy user on server
* remote_user: server remote user

#### Host
* host_tool_dependency_dir:  tool dependency dir
* host_shed_tools_dir:  shed tools dir


#### Miniconda
* miniconda_home: Dir wher conda will be installed and called from
* miniconda_modify_path: yes
* miniconda_rcfile: $HOME/.bashrc
* miniconda_installed: yes
* miniconda_lib: "{{ miniconda_home }}/lib" 

**NOTE:** Other conda especific configs are in the role/miniconda/defaults  
