
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