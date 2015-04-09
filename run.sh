#!/bin/sh

SRC=$(find $1 -name "*.java")
CLASS=$(basename ${SRC} .java)

echo_run() {
  echo "$@" && eval $@
}

compile() {
  mkdir -p class
  echo_run javac -J-Dfile.encoding=UTF-8 -d class ${SRC}
}

execute() {
  echo_run java -cp class ${CLASS}
}

compile && execute
