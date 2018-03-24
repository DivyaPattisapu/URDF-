cmake_minimum_required(VERSION 2.8.3)
project(urdf)
find_package(catkin REQUIRED COMPONENTS
  nav_msgs
  roscpp
  tf
)


catkin_package()

install(
  DIRECTORY launch meshes urdf
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)

## Declare a C++ executable

