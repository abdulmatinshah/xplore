#!/bin/bash

PROJECT_NAME=woyd

function die {
    echo -e $1
    exit 1
}

function testcase {
    declare -i FAIL
    FAIL=0
    ${@:2} || FAIL=1
    [ $FAIL = 1 ] && die "\n###[ $1 FAILED :( ]###\n"
    echo -e "\n===[ $1 PASSED ]===\n"
}

testcase 'FLAKE 8'      flake8 --config=setup.cfg
testcase 'LINTING SCSS' gulp scsslint
#testcase 'DJANGO TESTS' python manage.py test

exit 0
