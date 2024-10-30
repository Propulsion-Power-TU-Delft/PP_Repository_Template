#!/bin/sh -l 

repo_link="https://github.com/Propulsion-Power-TU-Delft/PP_Repository_Template"
flags=""
branch=""
testfile=""
workdir=$PWD

export CCACHE_DIR=$workdir/ccache

if [ "$#" -ne 0 ]; then
  while [ "$(echo $1 | cut -c1)" = "-" ]
    do
        case "$1" in
            -b)
                    branch=$2
                    shift 2
                ;;
            -s)
                    testfile=$2
                    shift 2
                ;;
    esac
    done
fi

name="PPTeam_Repo_$(echo $branch | sed 's/\//_/g')"
export OWD=$PWD
echo "Branch provided. Cloning to $PWD/src/$name"
if [ ! -d "src" ]; then
  mkdir "src"
fi
cd "src"
git clone --recursive $repo_link $name
cd $name
git config --add remote.origin.fetch '+refs/pull/*/merge:refs/remotes/origin/refs/pull/*/merge'
git config --add remote.origin.fetch '+refs/heads/*:refs/remotes/origin/refs/heads/*'
git fetch origin
git checkout $branch
git submodule update
cd $OWD 

# Set up pythonpath
export PYTHONPATH=$PYTHONPATH:$OWD/src/$name/src/src_python

# Run regression tests
cd $OWD/src/$name/src/regressiontests/
python3 $testfile 

if [ $? -eq 0 ]; then
  echo "Tests passed"
  exit 0
else 
  echo "Tests failed"
  exit 1 
fi 
