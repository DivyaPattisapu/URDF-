#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
    DESTDIR_ARG="--root=$DESTDIR"
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/divya/catkin_ws/src/rqt/rqt_py_common"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/divya/catkin_ws/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/divya/catkin_ws/install/lib/python2.7/dist-packages:/home/divya/catkin_ws/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/divya/catkin_ws/build" \
    "/usr/bin/python" \
    "/home/divya/catkin_ws/src/rqt/rqt_py_common/setup.py" \
    build --build-base "/home/divya/catkin_ws/build/rqt/rqt_py_common" \
    install \
    $DESTDIR_ARG \
    --install-layout=deb --prefix="/home/divya/catkin_ws/install" --install-scripts="/home/divya/catkin_ws/install/bin"
