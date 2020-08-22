#!/bin/bash

yaml_file=$1
out_file=$2

docker run --rm -v "${PWD}":/workdir mikefarah/yq yq r -j --prettyPrint $yaml_file > $out_file
exit $?
