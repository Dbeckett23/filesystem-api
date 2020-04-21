# Stop on errors, print commands
# See https://vaneyckt.io/posts/safer_bash_scripts_with_set_euxo_pipefail/
set -Eeuo pipefail
set -x

#Set FLASK_DEBUG, FLASK_APP and INSTA485_SETTINGS environment variables
export FLASK_DEBUG=True
export FLASK_APP=filesystem
export INSTA485_SETTINGS=config.py


#Run the development server on port 8000
flask run --host 0.0.0.0 --port 8000