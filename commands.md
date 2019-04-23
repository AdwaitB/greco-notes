
```bash
echo "NIX Env loading"
source ~/.nix-profile/etc/profile.d/nix.sh
. /home/abauskar/.nix-profile/etc/profile.d/nix.sh

echo "Pybatsim simulations"

nix-shell https://github.com/oar-team/kapack/archive/master.tar.gz -A pybatsim
nix-shell https://github.com/oar-team/kapack/archive/master.tar.gz -A batsim_temperature


python3 launcher.py schedulers/greco/qarnotNodeSched.py -o '{"dataset_filename":"../simulator-prototype/platform-generator/qarnot-extractor/sample-data/simple/datasets_simple.json"}'
./batsim -p sample-data/simple/platform_simple.xml \
       -w sample-data/simple/workload_simple.json \
       --events sample-data/simple/events_simple.json \
       -T 2 --enable-dynamic-jobs --forward-unknown-event

python3 launcher.py schedulers/greco/qarnotNodeSched.py -o '{"dataset_filename":"../simulator-prototype/platform-generator/qarnot-extractor/sample-data/1day_2019-03-10_2019-03-11/datasets.json"}'
./batsim -p sample-data/1day_2019-03-10_2019-03-11/platform.xml \
      -w sample-data/1day_2019-03-10_2019-03-11/workload.json \
      --events sample-data/1day_2019-03-10_2019-03-11/events.json \
      -T 2 --enable-dynamic-jobs --forward-unknown-event

python3 launcher.py schedulers/greco/qarnotNodeSched.py -o '{"dataset_filename":"../simulator-prototype/platform-generator/qarnot-extractor/sample-data/1week_2019-03-01_2019-03-08/datasets.json"}'
./batsim -p sample-data/1week_2019-03-01_2019-03-08/platform.xml \
     -w sample-data/1week_2019-03-01_2019-03-08/workload.json \
     --events sample-data/1week_2019-03-01_2019-03-08/events.json \
     -T 2 --enable-dynamic-jobs --forward-unknown-event

python3 launcher.py schedulers/greco/qarnotNodeSched.py -o '{"dataset_filename":"../simulator-prototype/platform-generator/qarnot-extractor/sample-data/2weeks_2019-03-01_2019-03-15/datasets.json"}'
./batsim -p sample-data/2weeks_2019-03-01_2019-03-15/platform.xml \
    -w sample-data/2weeks_2019-03-01_2019-03-15/workload.json \
    --events sample-data/2weeks_2019-03-01_2019-03-15/events.json \
    -T 2 --enable-dynamic-jobs --forward-unknown-event

python3 launcher.py schedulers/greco/qarnotNodeSched.py -o '{"input_path":"../temp/04-03_18-03", "update_period":600}'
./batsim -p ../../temp/04-03_18-03/platform.xml \
    -w ../../temp/04-03_18-03/workload.json \
    --events ../../temp/04-03_18-03/events.json \
    -T 2 --enable-dynamic-jobs --forward-unknown-event
```
```python
# PDB start python shell from PDB
!import code; code.interact(local=vars())
```