# TODO:
# - cleanups in lib directory -- replace jar files
#   with package dependencies
# - use source package

Summary:	Java project management and project comprehension tool
Summary(pl.UTF-8):	Narzędzie do zarządzania projektami Javy ułatwiajęce ich zrozumienie
Name:		maven
Version:	2.0.7
Release:	0.2
License:	Apache
Group:		Development/Languages/Java
Source0:	http://www.apache.org/dist/maven/binaries/%{name}-%{version}-bin.tar.bz2
# Source0-md5:	77d579221aed692ec63a44ab47bd87da
URL:		http://maven.apache.org/
Requires:	jdk
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Maven is a Java project management and project comprehension tool.
Maven is based on the concept of a project object model (POM) in that
all the artifacts produced by Maven are a result of consulting a well
defined model for your project.

The intent of Maven is to make intra-project development highly
manageable in the hopes of providing more time for cross-project
development. You might call it cross-project pollination or the
sharing of project development knowledge, this is what Maven attempts
to encourage.

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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/%{name}/bin}
ln -sf %{_datadir}/%{name}/bin/mvn $RPM_BUILD_ROOT%{_bindir}/mvn

install -d $RPM_BUILD_ROOT
install bin/mvn $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
cp -a bin/m2.conf $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
cp -a boot conf lib $RPM_BUILD_ROOT%{_datadir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc NOTICE.txt
%attr(755,root,root) %{_bindir}/mvn
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%{_datadir}/%{name}/bin/m2.conf
%attr(755,root,root) %{_datadir}/%{name}/bin/mvn
%{_datadir}/%{name}/boot
%{_datadir}/%{name}/conf
%{_datadir}/%{name}/lib
