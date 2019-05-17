
```bash
echo "NIX Env loading"

curl https://nixos.org/nix/install | sh
nix-env -i ipfs

source ~/.nix-profile/etc/profile.d/nix.sh
. /home/abauskar/.nix-profile/etc/profile.d/nix.sh

echo "Pybatsim simulations"

nix-shell https://github.com/oar-team/kapack/archive/master.tar.gz -A pybatsim
nix-shell https://github.com/oar-team/kapack/archive/master.tar.gz -A batsim_temperature

pybatsim schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../simulator-prototype/platform-generator/qarnot-extractor/sample-data/simple/"}'
python3 launcher.py schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../simulator-prototype/platform-generator/qarnot-extractor/sample-data/simple/"}'
./batsim -p ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/simple/platform.xml \
       -w ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/simple/workload_simple.json \
       --events ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/simple/events_simple.json \
       -T 2 --enable-dynamic-jobs --forward-unknown-event

pybatsim schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1day_2019-03-10_2019-03-11/"}'
python3 launcher.py schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1day_2019-03-10_2019-03-11/"}'
./batsim -p ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1day_2019-03-10_2019-03-11/platform.xml \
      -w ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1day_2019-03-10_2019-03-11/workload.json \
      --events ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1day_2019-03-10_2019-03-11/events.json \
      -T 2 --enable-dynamic-jobs --forward-unknown-event

pybatsim schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1week_2019-03-01_2019-03-08/"}'
python3 launcher.py schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1week_2019-03-01_2019-03-08/"}'
./batsim -p ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1week_2019-03-01_2019-03-08/platform.xml \
     -w ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1week_2019-03-01_2019-03-08/workload.json \
     --events ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1week_2019-03-01_2019-03-08/events.json \
     -T 2 --enable-dynamic-jobs --forward-unknown-event

pybatsim schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/2weeks_2019-03-01_2019-03-15/"}'
python3 launcher.py schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/2weeks_2019-03-01_2019-03-15/"}'
./batsim -p ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/2weeks_2019-03-01_2019-03-15/platform.xml \
    -w ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/2weeks_2019-03-01_2019-03-15/workload.json \
    --events ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/2weeks_2019-03-01_2019-03-15/events.json \
    -T 2 --enable-dynamic-jobs --forward-unknown-event

pybatsim schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../transient/04-03_18-03_2m", "update_period":600}'
python3 launcher.py schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../transient/04-03_18-03_2m", "update_period":600}'
./batsim -p ../../transient/04-03_18-03_2m/platform.xml \
    -w ../../transient/04-03_18-03_2m/workload.json \
    --events ../../transient/04-03_18-03_2m/events.json \
    -T 2 --enable-dynamic-jobs --forward-unknown-event

pybatsim schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../transient/23-04_2w", "update_period":600}'
python3 launcher.py schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../transient/23-04_2w", "update_period":600}'
./batsim -p ../../transient/23-04_2w/platform.xml \
    -w ../../transient/23-04_2w/workload.json \
    --events ../../transient/23-04_2w/events.json \
    -T 2 --enable-dynamic-jobs --forward-unknown-event

pybatsim schedulers/greco/transferHistoryStatic.py
python3 launcher.py schedulers/greco/transferHistoryStatic.py
./batsim -p ../../transient/23-04_2w_static/platform.xml \
    -w ../../transient/23-04_2w_static/workload.json \
    -T 2 --enable-dynamic-jobs
./batsim -p ../../transient/23-04_2w_static/platform.xml \
    -w ../../transient/23-04_2w_static/workload_empty.json \
    --events ../../transient/23-04_2w_static/events_transfers.txt \
    -T 2 --enable-dynamic-jobs --forward-unknown-event

pybatsim schedulers/greco/transferHistoryStatic.py -o '{"input_path":"../transient/04_10_2w_0920_0935_static"}'
python3 launcher.py schedulers/greco/transferHistoryStatic.py -o '{"input_path":"../transient/04_10_2w_0920_0935_static"}'
./batsim -p ../../transient/04_10_2w_0920_0935_static/platform.xml \
    -w ../../transient/04_10_2w_0920_0935_static/workload.json \
    -T 2
./batsim -p ../../transient/04_10_2w_0920_0935_static/platform.xml \
    -w ../../transient/04_10_2w_0920_0935_static/workload_empty.json \
    --events ../../transient/04_10_2w_0920_0935_static/events_transfers.txt \
    -T 2 --enable-dynamic-jobs --forward-unknown-event
```
```python
# PDB start python shell from PDB
!import code; code.interact(local=vars())
```

```bash
echo "Grid 5000"

echo "Create a subnet"
oarsub -I -l slash_22=1+{"virtual!='NO'"}/nodes=1
oarsub -l host=1,walltime=3 -I -t deploy

echo "kadeploy"
kadeploy3 -f $OAR_NODE_FILE -e ubuntu1804-x64-min -k
kadeploy3 -f $OAR_NODE_FILE -e ipfs-ubuntu-min -k

echo "List all images"
kaenv3 -l

echo "Nix issue"
sysctl kernel.unprivileged_userns_clone=1

echo "Custom environment"
ssh root@$OAR_NODE_FILE tgz-g5k > image.tgz
kaenv3 -p ubuntu1804-x64-min -u deploy > image.env
kaenv3 -a image.env
kadeploy3 -f $OAR_NODE_FILE -a image.env -k

echo "Add a User"
adduser username
usermod -aG sudo username

curl  -kns https://api.grid5000.fr/4.0/sites/rennes/deployment -X POST -H'Content-Type: application/json' -d '{
          "nodes": ["paravance-49.rennes.grid5000.fr",
                    "paravance-30.rennes.grid5000.fr",
                    "paravance-31.rennes.grid5000.fr"],
          "environment": {
             "kind" : "database",
             "name": "ubuntu1804-x64-min"
          },
          "ssh_authorized_keys" :"~/.ssh/.id_rsa.pub"
 }'
```

```bash
# Steps for running IPFS
ipfs init
ipfs daemon

kill -9 $(pidof ipfs)
```

```bash
# Vagrant
vagrant init ubuntu/bionic64
vagrant up
vagrant ssh

vagrant package --output ubuntu-ipfs.box
vagrant box remove ubuntu-ipfs
vagrant box add ubuntu-ipfs ubuntu-ipfs.box

vagrant destory
rm Vagrantfile
```

```bash
#Other stuff

#Python3
sudo ln -sfn /usr/bin/python3.6 /usr/bin/python
pip install virtualenv --user
export PATH=~/.local/bin/:$PATH
virtualenv venv
```