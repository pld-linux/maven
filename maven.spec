# $Revision: 1.2 $

# TODO:
#  - cleanups in lib directory -- replace jar files 
#    with package dependencies

%define		beta	beta-10

Summary:	Java project management and project comprehension tool
Summary(pl):	Narzêdzie do zarz±dzania projektami Javy u³atwiajêce ich zrozumienie 
Name:		maven
Version:	1.0
%define		buildname	%{version}-%{beta}
Release:	0.%(echo %{beta}|tr - .)
Group:		Development/Languages/Java
License:	Apache
Source0:	http://maven.apache.org/builds/release/%{buildname}/maven-%{buildname}.tar.gz
# Source0-md5:	4179bd3fdb5371f6c59424194447ecde
Patch0:		%{name}-MAVEN_HOME.patch
URL:		http://maven.apache.org/
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Maven is a Java project management and project comprehension
tool. Maven is based on the concept of a project object model
(POM) in that all the artifacts produced by Maven are a result of
consulting a well defined model for your project.

The intent of Maven is to make intra-project development highly
manageable in the hopes of providing more time for cross-project
development. You might call it cross-project pollination or the
sharing of project development knowledge, this is what Maven
attempts to encourage.

# %description -l pl
# maven

%prep
%setup -q -n %{name}-%{buildname}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
ln -s %{_datadir}/%{name}/bin/maven $RPM_BUILD_ROOT/%{_bindir}/maven

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
install bin/maven $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
install bin/forehead.conf $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
cp -r lib $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r plugins $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r repository $RPM_BUILD_ROOT%{_datadir}/%{name}
install maven-project.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_bindir}/maven

%attr(755,root,root) %{_datadir}/%{name}/bin/maven
%{_datadir}/%{name}/bin/forehead.conf
%dir %{_datadir}/%{name}/bin
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/plugins
%{_datadir}/%{name}/repository
%{_datadir}/%{name}/maven-project.xsd
