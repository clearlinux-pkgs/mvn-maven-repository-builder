#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-maven-repository-builder
Version  : 1.0.alpha.2
Release  : 4
URL      : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-repository-builder/1.0-alpha-2/maven-repository-builder-1.0-alpha-2.jar
Source0  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-repository-builder/1.0-alpha-2/maven-repository-builder-1.0-alpha-2.jar
Source1  : https://repo1.maven.org/maven2/org/apache/maven/shared/maven-repository-builder/1.0-alpha-2/maven-repository-builder-1.0-alpha-2.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-maven-repository-builder-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-maven-repository-builder package.
Group: Data

%description data
data components for the mvn-maven-repository-builder package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-repository-builder/1.0-alpha-2
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-repository-builder/1.0-alpha-2/maven-repository-builder-1.0-alpha-2.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-repository-builder/1.0-alpha-2
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/maven/shared/maven-repository-builder/1.0-alpha-2/maven-repository-builder-1.0-alpha-2.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-repository-builder/1.0-alpha-2/maven-repository-builder-1.0-alpha-2.jar
/usr/share/java/.m2/repository/org/apache/maven/shared/maven-repository-builder/1.0-alpha-2/maven-repository-builder-1.0-alpha-2.pom
