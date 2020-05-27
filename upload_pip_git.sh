#!/bin/bash

EGG_FOLDER="$1.egg-info/"
COMMIT_MESSAGE="$2"

rm -r build/
rm -r dist/
rm -r ${EGG_FOLDER}

python setup.py sdist
python setup.py bdist_wheel
twine upload dist/*

# UPLOAD TO GIT REPOSITORY
git add .
git commit -m ${COMMIT_MESSAGE}
git push -u origin master
