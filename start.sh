echo "Cloning Repo...."
if [ -z $BRANCH ]
then
  echo "Cloning main branch...."
  git clone https://github.com/Dhhonu/my /my
else
  echo "Cloning $BRANCH branch...."
  git clone https://github.com/Dhhonu/my -b $BRANCH /my
fi
cd /forward
pip3 install -U -r requirements.txt
echo "Starting Bot.... By @DKBOTZ"
python3 bot.py
