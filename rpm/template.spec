Name:           ros-indigo-ur5-moveit-config
Version:        1.1.5
Release:        0%{?dist}
Summary:        ROS ur5_moveit_config package

Group:          Development/Libraries
License:        BSD
URL:            http://moveit.ros.org/
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-indigo-joint-state-publisher
Requires:       ros-indigo-moveit-planners-ompl
Requires:       ros-indigo-moveit-ros-move-group
Requires:       ros-indigo-moveit-ros-visualization
Requires:       ros-indigo-robot-state-publisher
Requires:       ros-indigo-ur-description
Requires:       ros-indigo-xacro
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-ur-description

%description
An automatically generated package with all the configuration and launch files
for using the ur5 with the MoveIt Motion Planning Framework

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Mon Nov 03 2014 Alexander Bubeck <aub@ipa.fhg.de> - 1.1.5-0
- Autogenerated by Bloom

* Thu Sep 04 2014 MoveIt Setup Assistant <assistant@moveit.ros.org> - 1.0.4-0
- Autogenerated by Bloom

* Mon Aug 25 2014 MoveIt Setup Assistant <assistant@moveit.ros.org> - 1.0.3-0
- Autogenerated by Bloom

