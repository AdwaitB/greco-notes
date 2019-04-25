
```bash
echo "NIX Env loading"
source ~/.nix-profile/etc/profile.d/nix.sh
. /home/abauskar/.nix-profile/etc/profile.d/nix.sh

echo "Pybatsim simulations"

nix-shell https://github.com/oar-team/kapack/archive/master.tar.gz -A pybatsim
nix-shell https://github.com/oar-team/kapack/archive/master.tar.gz -A batsim_temperature


python3 launcher.py schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/simple/"}'
./batsim -p ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/simple/platform_simple.xml \
       -w ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/simple/workload_simple.json \
       --events ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/simple/events_simple.json \
       -T 2 --enable-dynamic-jobs --forward-unknown-event

python3 launcher.py schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1day_2019-03-10_2019-03-11/"}'
./batsim -p ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1day_2019-03-10_2019-03-11/platform.xml \
      -w ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1day_2019-03-10_2019-03-11/workload.json \
      --events ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1day_2019-03-10_2019-03-11/events.json \
      -T 2 --enable-dynamic-jobs --forward-unknown-event

python3 launcher.py schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1week_2019-03-01_2019-03-08/"}'
./batsim -p ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1week_2019-03-01_2019-03-08/platform.xml \
     -w ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1week_2019-03-01_2019-03-08/workload.json \
     --events ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/1week_2019-03-01_2019-03-08/events.json \
     -T 2 --enable-dynamic-jobs --forward-unknown-event

python3 launcher.py schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/2weeks_2019-03-01_2019-03-15/"}'
./batsim -p ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/2weeks_2019-03-01_2019-03-15/platform.xml \
    -w ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/2weeks_2019-03-01_2019-03-15/workload.json \
    --events ../../simulator-prototype/platform-generator/qarnot-extractor/sample-data/OLD/2weeks_2019-03-01_2019-03-15/events.json \
    -T 2 --enable-dynamic-jobs --forward-unknown-event

python3 launcher.py schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../transient/04-03_18-03_2m", "update_period":600}'
./batsim -p ../../transient/04-03_18-03_2m/platform.xml \
    -w ../../transient/04-03_18-03_2m/workload.json \
    --events ../../transient/04-03_18-03_2m/events.json \
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
oarsub -l host=1 -I -t deploy

echo "Copy the disk file"
cp /grid5000/virt-images/ubuntu1804-x64-min-2019041715.qcow2 /tmp/

echo "Create the image file"
qemu-img create -f qcow2 -o backing_file=/tmp/ubuntu1804-x64-min-2019041715.qcow2 /tmp/greco_simulation.qcow2

echo "Pick a MAC"
g5k-subnets -im

echo "Create the VM"
virsh create ~/XML/greco_simulation.xml

echo "Get IP Address od domain"
virsh domifaddr greco_simulator

echo "kadeploy"
kadeploy3 -f $OAR_NODE_FILE -e debian9-x64-base -k
```