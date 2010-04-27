#!/bin/sh

ARGS=$@
ORIG_ARGS=$ARGS

if [ -z "$JAVA_HOME" ]; then
  echo You must specify the JAVA_HOME environment variable
  exit 1
fi

JAVACMD="$JAVA_HOME/bin/java"

BOOTSTRAP_JAR=bootstrap-mini/bootstrap-mini.jar

# TODO: get rid of M2_HOME once integration tests are in here
PREFIX=`dirname $M2_HOME`

# OS specific support.  $var _must_ be set to either true or false.
cygwin=false;
case "`uname`" in
  CYGWIN*) cygwin=true ;;
esac

if [ "$cygwin" = "true" ]; then
  PREFIX=`cygpath -w $PREFIX`
  JAVA_HOME=`cygpath -w $JAVA_HOME`
fi

ARGS=$ORIG_ARGS

(
  # TODO: should we be going back to the mini now that we have the real thing?
  cd maven-core-it-verifier
  $JAVACMD $MAVEN_OPTS -jar ../bootstrap/$BOOTSTRAP_JAR package $ARGS
  ret=$?; if [ $ret != 0 ]; then exit $ret; fi
)
ret=$?; if [ $ret != 0 ]; then exit $ret; fi

(
  cd ./maven-core-it
  echo
  echo "Running maven-core integration tests ..."
  echo
  ./maven-core-it.sh $ARGS
  ret=$?; if [ $ret != 0 ]; then exit $ret; fi
)
ret=$?; if [ $ret != 0 ]; then exit $ret; fi
