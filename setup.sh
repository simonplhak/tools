PWD = $(pwd)
# install project
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt;

# setup docker-pretty=ps

echo "alias docker-ps='docker-pretty-ps'" >> ~/.bashrc;
. ~/.bashrc;
cat <<EOT > #!${PWD}/env/bin/python3

import dockerprettyps

dockerprettyps.run_cli()
EOT
# /home/simon/.local/bin/docker-pretty-ps

