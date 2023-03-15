# Installation instruction
### On linux
```
conda create -n tension python=3.9.16 anaconda
conda activate tension
pip install tensiometer
python -m ipykernel install --user --name tension
```

Now run the jupyter notebook with kernal **tension**

### How to connect to jupyter lav via ssh tunneling
```
$ Login to iitr server with ssh -p 2299 username@gswarup.iitr.ac.in
$ source /media/root1/3PAR/sdandapat/miniconda3/bin/activate
$ screen -S <screenname>
$ conda activate ptacomp
$ jupyter notebook --no-browser --port xxxx
<copy the token link>
$ ctrl+a+d
$ Come to your local system and type: 
ssh -NfL localhost:xxxx:localhost:xxxx username@gswarup.iitr.ac.in
$ Now paste the token link to your browser
```
