
# TODO:
#  - cleanups in lib directory -- replace jar files 
#    with package dependencies

%define		beta	rc2

Summary:	Java project management and project comprehension tool
Summary(pl):	Narzêdzie do zarz±dzania projektami Javy u³atwiajêce ich zrozumienie
Name:		maven
Version:	1.0
%define		buildname	%{version}-%{beta}
Release:	0.%(echo %{beta}|tr - .)
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/maven/binaries/maven-%{buildname}.tar.gz
# Source0-md5:	2104228d1762413e35b80387f41db727
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

%description -l pl
Maven to narzêdzie do zarz±dzania projektami w Javie, u³atwiaj±ce ich
zrozumienie. Jest oparty na idei obiektowego modelu projektu (POM -
Project Object Model), w której wszystkie wytwory Mavena s± wynikiem
konsultowania z dobrze zdefiniowanym modelem projektu.

Intencj± Mavena jest uczyniæ rozwój wewn±trzprojektowy wysoko
zarz±dzalnym w nadziei pozostawienia wiêkszej ilo¶ci czasu na rozwój
miêdzyprojektowy. Mo¿na to nazwaæ zapylaniem miêdzyprojektowym lub
dzieleniem wiedzy o rozwoju projektów - do tego Maven próbuje
zachêciæ.

%prep
%setup -q -n %{name}-%{buildname}
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
