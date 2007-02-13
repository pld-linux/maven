
# TODO:
#  - cleanups in lib directory -- replace jar files 
#    with package dependencies

Summary:	Java project management and project comprehension tool
Summary(pl.UTF-8):	Narzędzie do zarządzania projektami Javy ułatwiajęce ich zrozumienie
Name:		maven
Version:	1.0.2
Release:	0.1
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/maven/binaries/%{name}-%{version}.tar.gz
# Source0-md5:	47624c83b907fa16e8257bc5b351f84a
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

%description -l pl.UTF-8
Maven to narzędzie do zarządzania projektami w Javie, ułatwiające ich
zrozumienie. Jest oparty na idei obiektowego modelu projektu (POM -
Project Object Model), w której wszystkie wytwory Mavena są wynikiem
konsultowania z dobrze zdefiniowanym modelem projektu.

Intencją Mavena jest uczynić rozwój wewnątrzprojektowy wysoko
zarządzalnym w nadziei pozostawienia większej ilości czasu na rozwój
międzyprojektowy. Można to nazwać zapylaniem międzyprojektowym lub
dzieleniem wiedzy o rozwoju projektów - do tego Maven próbuje
zachęcić.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
ln -sf %{_datadir}/%{name}/bin/maven $RPM_BUILD_ROOT%{_bindir}/maven

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
install bin/maven $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
install bin/forehead.conf $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
cp -r lib $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -r plugins $RPM_BUILD_ROOT%{_datadir}/%{name}
#cp -r repository $RPM_BUILD_ROOT%{_datadir}/%{name}
install maven-project.xsd $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/maven
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%attr(755,root,root) %{_datadir}/%{name}/bin/maven
%{_datadir}/%{name}/bin/forehead.conf
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/plugins
#%{_datadir}/%{name}/repository
%{_datadir}/%{name}/maven-project.xsd
