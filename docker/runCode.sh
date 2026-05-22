#!/bin/sh -l

# Bash script file used for automated regression tests with Docker and GitHub actions.

REPO_NAME="PP_Repository_Template"
REPO_URL="https://github.com/Propulsion-Power-TU-Delft/PP_Repository_Template.git"

echo "Docker Container for $REPO_NAME Repository"
usage="$(basename "$0") [-h] [-b branch_name]
where:
    -h  show this help text
    -b  branch name
    -s  script with tests
"

flags=""
branch=""       # Repository branch to check out
testscript=""   # Script to run in Docker container
workdir=$PWD
export CCACHE_DIR=$workdir/ccache

# Parse arguments from terminal inputs
if [ "$#" -ne 0 ]; then
  while [ "$(echo $1 | cut -c1)" = "-" ]
    do
        case "$1" in
            -b)
                    branch=$2
                    shift 2
                ;;
            -s)
                    testscript=$2
                    shift 2
                ;;
            *)
                    echo "$usage" >&2
                    exit 1
                ;;
    esac
    done
fi

# Clone source code using git into directory "src"
# Here you do everything needed to set up the code as if it were on a new system..
if [ ! -z "$branch" ]; then
  name="$REPO_NAME_$(echo $branch | sed 's/\//_/g')"
  echo "Branch provided. Cloning to $PWD/src/$name"
  if [ ! -d "src" ]; then
    mkdir "src"
  fi
  cd "src"
  git clone --recursive $REPO_URL $name
  cd $name
  export REPO_DIR=$PWD
  git config --add remote.origin.fetch '+refs/pull/*/merge:refs/remotes/origin/refs/pull/*/merge'
  git config --add remote.origin.fetch '+refs/heads/*:refs/remotes/origin/refs/heads/*'
  git fetch origin
  git checkout $branch
  git submodule update
else
    echo "Branch not specified, use -b to provide a branch."
    exit 1
fi


# For python applications, activate virtual environment and install required modules
python3 -m venv /home/ubuntu/pyenv 
virtualenv -p /usr/bin/python3 /home/ubuntu/pyenv 
. /home/ubuntu/pyenv/bin/activate 
python3 -m pip install -r $REPO_DIR/requirements.txt 

# Optional: update python environment variables if applicable
export REPO_HOME=$PWD
export PYTHONPATH=$PYTHONPATH:$REPO_HOME
export PATH=$PATH:$REPO_HOME/bin/

# Steps needed to run test script
echo "Running regression tests for $name"

cd regressiontests

if [ ! -z "$testscript"]; then
    python3 $testscript
else
    echo "Test script not specified, use -s to specify the file name containing describing the regression tests."
    exit 1
fi 
