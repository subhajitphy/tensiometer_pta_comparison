# Installation instruction
### On linux
```
conda create -n tension python=3.9.16 anaconda
conda install -c conda-forge jupyterlab
conda activate tension
pip install tensiometer
python -m ipykernel install --user --name tension
```

Now run the jupyter notebook with kernal **tension**

### How to connect to jupyter lab via ssh tunneling
```
$ Login to iitr server with ssh -p 2299 username@gswarup.iitr.ac.in
$ source /media/root1/3PAR/sdandapat/miniconda3/bin/activate
$ pip install tensiometer
$ screen -S <screenname>
$ python -m ipykernel install --user --name "kernal_name"
$ conda activate ptacomp
$ jupyter lab --no-browser --port xxxx
<copy the token link>
$ ctrl+a+d
$ Come to your local system and type: 
ssh -NfL localhost:xxxx:localhost:xxxx -p 2299 username@gswarup.iitr.ac.in
$ Now paste the token link to your browser
$ change the kernal to "kernal_name" on while running jupyter notebook
```
