%bcond_with itests
%bcond_without bootstrap
%bcond_without repolib

%define repodir %{_javadir}/repository.jboss.com/org/apache/maven/%{version}-brew
%define repodirlib %{repodir}/lib
%define repodirsrc %{repodir}/src

%define repo_dir m2_home_local/repository
%define maven_settings_file %{_builddir}/%{name}/settings.xml

Name:		maven
Version:	2.0.8
Release:	%{bootstrap_release %rel}
Summary:	Java project management and project comprehension tool

Group:		Development/Languages/Java
License:	Apache v2
URL:		http://maven.apache.org/

# svn export http://svn.apache.org/repos/asf/maven/components/tags/maven-%{version} maven
# tar czf maven-src.tar.gz maven
Source0:		http://execve.pl/PLD/maven/%{name}-src.tar.gz
# Source0-md5:	8db6e8515fe317f635befa39b074016a

# svn export -r {2007-03-31} http://svn.apache.org/repos/asf/maven/plugins/trunk maven-plugins
# tar czf maven-plugins-070331-src.tar.gz maven-plugins
Source2:		http://execve.pl/PLD/maven/%{name}-plugins-070705-src.tar.gz
# Source2-md5:	7e9d3175131910d64c95fdf4d60651fa

# We need to replace the javadoc plugin as the 2.3-SNAPSHOT included above 
# has several bugs
# svn export http://svn.apache.org/repos/asf/maven/plugins/tags/maven-javadoc-plugin-2.4 maven-javadoc-plugin
Source22: 		http://execve.pl/PLD/maven/maven-javadoc-plugin-2.4-src.tar.gz
# Source22-md5:	c3c1014b8548f94f91f3b679a5500e4b

# No source location for these. They are ascii files generated from maven
# repositories, and are not in cvs/svn
# The files were originally aquired from: http://repo1.maven.org/maven2/
Source3:		http://execve.pl/PLD/maven/m2_pom_repo.tar.gz
# Source3-md5:	a4b18868658fe3e3c58d0f4e9bf66bee

# As with above, these files are from the maven repositories, and are not in 
# cvs/svn
# The files were originally aquired from: http://repo1.maven.org/maven2/
Source4:		http://execve.pl/PLD/maven/m2_jar_repo.tar.gz
# Source4-md5:	00976d79948c93be23cdda62300dc8c2
Source5:		%{name}-script

Source6:		maven-JPackageRepositoryLayout.java
Source7:		maven-settings.xml

# svn export -r '{2006-03-08}' http://svn.apache.org/repos/asf/maven/plugins/trunk/maven-site-plugin maven-site-plugin
# tar czf maven-maven-site-plugin.tar.gz maven-site-plugin 
Source8:	http://execve.pl/PLD/maven/%{name}-maven-site-plugin.tar.gz
# Source8-md5:	2ba3a4baeb3d4d9d7b8121a6ae05578d

Source9:	%{name}-run-it-tests.sh

# svn export http://svn.apache.org/repos/asf/maven/components/tags/maven-2.0.8/maven-model
# cd maven-model
# mvn -P all-models package 
# Find model jar in target/maven-model-2.0.8.jar
Source10:	%{name}-model-v3.jar
Source11:	%{name}-MavenJPackageDepmap.java
Source12:	%{name}-addjdom-depmap.xml
Source13:	%{name}-empty-dep.pom

# Empty jar file with just a manifest. No source destination to specify
Source14:	%{name}-empty-dep.jar
Source15:	%{name}-jpp-script
Source16:	%{name}-jpp-readme.html
Source17:	%{name}-versionless-depmap.xml

Source99:		maven-doxia-modules.pom
Source100:		maven-component-info.xml

Patch0:		maven-addjdomtobootstrappath.patch
Patch1:		%{name}-jpprepolayout.patch
Patch2:		%{name}-fastjar-manifest-fix.patch
Patch3:		%{name}-plugins-doxiaupdatefix.patch
Patch4:		%{name}-plugins-catch-uncaught-exceptions.patch
Patch5:		%{name}-plugins-dependency-plugin-import-fix.patch
Patch6:		%{name}-%{version}-excludeexternaljars.patch
Patch7:		%{name}-site-plugin-addservletdep.patch
Patch8:		%{name}-enable-bootstrap-repository.patch
Patch9:		%{name}-use-unversioned-classworlds.patch
Patch10:	%{name}-plugins-disablecobertura.patch
Patch11:	%{name}-shade-plugin-replacement.patch
Patch12:	%{name}-sourcetarget.patch
Patch13:	%{name}-plugins-MJAVADOC-137-AbstractJavadocMojo.patch
# The maven javadoc plugin 2.5 pre-reqs maven 2.0.9, we lower to 2.0.8
Patch14:	%{name}-javadoc-plugin-pom.patch
# javadoc 2.4 uses an old doxia method
Patch15:	%{name}-plugins-javadoc-newdoxia.patch
# This plugin can't cope with a JAR without a JDK version on it
Patch16:	%{name}-plugins-project-info-reports-jdkversion.patch
Patch17:	%{name}-MNG-3139.patch
Patch18:	%{name}-plugins-jpprepolayout.patch
Patch19:	%{name}-plugins-disableenforcer.patch
Patch20:	%{name}-commons-cli-1.1.patch

### PLDIZED DEPENDENCIES {{{
### BRs {{{
BuildRequires:	ant >= 1.6.5
BuildRequires:	ant-junit
BuildRequires:	antlr >= 2.7.4
BuildRequires:	ant-nodeps
BuildRequires:	java-bsh >= 1.3.0
BuildRequires:	java-commons-beanutils >= 1.7.0
BuildRequires:	java-commons-cli >= 1.0
BuildRequires:	java-commons-collections >= 3.1
BuildRequires:	java-commons-io >= 1.1
BuildRequires:	java-commons-lang >= 2.1
BuildRequires:	java-commons-logging >= 1.0.4
BuildRequires:	java-commons-validator >= 1.1.4
BuildRequires:	java-dom4j >= 1.6.1
BuildRequires:	java-gnu-regexp >= 1.1.4
BuildRequires:	java-httpunit >= 1.6
BuildRequires:	java-jdom >= 1.0
BuildRequires:	java-junit >= 3.8.2
BuildRequires:	java-oro >= 2.0.8
BuildRequires:	java-qdox >= 1.5
BuildRequires:	java-rhino >= 1.5
BuildRequires:	java-xalan >= 2.6.0
BuildRequires:	java-xerces >= 2.7.1
BuildRequires:	java-xmlunit
BuildRequires:	java-xom
%{buildrequires_jdk}
BuildRequires:	jpackage-utils >= 0:1.7.2
BuildRequires:	rpmbuild(macros) >= 1.557
BuildRequires:	sed >= 4.0
%if %{with itests}
BuildRequires:	java-log4j >= 1.2.13
BuildRequires:	java(xml-commons-apis) >= 1.3.02
%endif
### }}}

### Rs {{{
Requires:	ant >= 1.6.5
Requires:	antlr >= 2.7.4
Requires:	java-bsh >= 1.3.0
Requires:	java-commons-beanutils >= 1.7.0
Requires:	java-commons-cli >= 1.0
Requires:	java-commons-collections >= 3.1
Requires:	java-commons-io >= 1.1
Requires:	java-commons-lang >= 2.1
Requires:	java-commons-logging >= 1.0.4
Requires:	java-commons-validator >= 1.1.4
Requires:	java-dom4j >= 1.6.1
Requires:	java-gnu-regexp >= 1.1.4
Requires:	java-httpunit >= 1.6
Requires:	java-jdom >= 1.0
Requires:	java-junit >= 3.8.2
Requires:	java-oro >= 2.0.8
Requires:	java-qdox >= 1.5
Requires:	java-rhino >= 1.5
Requires:	java-xalan >= 2.6.0
Requires:	java-xerces >= 2.7.1
Requires:	java-xmlunit
Requires:	java-xom
Requires(post):	java-commons-cli >= 1.0
Requires(post):	java-commons-lang >= 2.1
Requires(post):	java-commons-logging >= 1.0.4
Requires(post):	java-jdom >= 1.0
Requires(post):	jpackage-utils >= 0:1.7.2
Requires(postun):	jpackage-utils >= 0:1.7.2
### }}}
### END OF PLDIZED DEPENDENCIES }}}

### DEPENDENCIES NOT PACKAGED FOR PLD {{{
BuildRequires:	java-velocity >= 1.4
Requires:		velocity >= 1.4
### }}}

### DEPENDENCIES THAT NEEDS INVESTIGATION {{{
# Is java(mail) enough?
BuildRequires:	glassfish-javamail
Requires:		glassfish-javamail
# java(servlet)?
BuildRequires:	tomcat5-servlet-2.4-api
Requires:		tomcat5-servlet-2.4-api
# C library??? Or some java bindings?
BuildRequires:	xmlrpc
Requires:		xmlrpc
# WTF is that?
BuildRequires:	aqute-bndlib
### }}}

### OLD JPP DEPENDENCIES {{{
### BRs {{{
#BuildRequires:	cglib >= 2.1.0
BuildRequires:	checkstyle4 >= 4.1
BuildRequires:	checkstyle4-optional >= 4.1
BuildRequires:	classworlds >= 1.1
BuildRequires:	jaxen >= 1.1
#BuildRequires:	jmock >= 1.0.1
BuildRequires:	jline >= 0.8.1
BuildRequires:	jsch >= 0.1.20
BuildRequires:	jtidy >= 1.0
BuildRequires:	maven2-common-poms >= 1.0-5
BuildRequires:	maven-jxr >= 1.0-2
BuildRequires:	maven-wagon >= 1.0-0.1.b2
BuildRequires:	maven-doxia >= 1.0-0.a9
BuildRequires:	nekohtml >= 0.9.3
BuildRequires:	plexus-ant-factory >= 1.0-0.a1.2
BuildRequires:	plexus-bsh-factory >= 1.0-0.a7s.2
BuildRequires:	plexus-archiver >= 1.0-0.1.a8
BuildRequires:	plexus-compiler >= 1.5.1
BuildRequires:	plexus-container-default >= 1.0
BuildRequires:	plexus-i18n >= 1.0
BuildRequires:	plexus-interactivity >= 1.0
BuildRequires:	plexus-utils >= 1.2
BuildRequires:	plexus-velocity >= 1.1.2
BuildRequires:	pmd >= 3.6
BuildRequires:	saxon-scripts
BuildRequires:	saxpath

%if %{without bootstrap}
BuildRequires:	%{name} = %{version}
BuildRequires:	maven2-plugin-ant
BuildRequires:	maven2-plugin-assembly
BuildRequires:	maven2-plugin-clean
BuildRequires:	maven2-plugin-compiler
BuildRequires:	maven2-plugin-install
BuildRequires:	maven2-plugin-jar
BuildRequires:	maven2-plugin-javadoc
BuildRequires:	maven2-plugin-plugin
BuildRequires:	maven2-plugin-resources
BuildRequires:	maven2-plugin-shade
BuildRequires:	maven2-plugin-site
BuildRequires:	maven2-plugin-surefire
BuildRequires:	maven-shared-archiver
BuildRequires:	maven-doxia-sitetools
BuildRequires:	maven-embedder
BuildRequires:	maven-scm >= 0:1.0-0.b3.2
BuildRequires:	maven-scm-test >= 0:1.0-0.b3.2
BuildRequires:	maven-shared-common-artifact-filters
BuildRequires:	maven-shared-dependency-analyzer
BuildRequires:	maven-shared-dependency-tree
BuildRequires:	maven-shared-downloader
BuildRequires:	maven-shared-file-management >= 1.0
BuildRequires:	maven-shared-io
BuildRequires:	maven-shared-plugin-testing-harness >= 1.0
BuildRequires:	maven-shared-repository-builder
BuildRequires:	maven-shared-invoker
BuildRequires:	maven-shared-jar
BuildRequires:	maven-shared-model-converter
BuildRequires:	maven-shared-plugin-testing-tools
BuildRequires:	maven-shared-plugin-tools-api
BuildRequires:	maven-shared-plugin-tools-beanshell
BuildRequires:	maven-shared-plugin-tools-java
BuildRequires:	maven-shared-reporting-impl
BuildRequires:	maven-shared-verifier
BuildRequires:	maven-surefire >= 2.0
BuildRequires:	maven-surefire-provider-junit
BuildRequires:	maven-surefire-booter >= 2.0
BuildRequires:	modello >= 1.0-0.a8.3
BuildRequires:	modello-maven-plugin >= 1.0-0.a8.3
BuildRequires:	plexus-digest
BuildRequires:	plexus-maven-plugin >= 1.3.5
BuildRequires:	plexus-mail-sender
BuildRequires:	plexus-resources
%endif
# }}}

### Rs {{{
Requires:	aqute-bndlib
#Requires:	cglib >= 2.1.0
Requires:	checkstyle4 >= 4.1
Requires:	classworlds >= 1.
Requires(post):	classworlds >= 1.1
#Requires:	tomcat5-parent
Requires:	jaxen >= 1.1
#Requires:	jmock >= 1.0.1
Requires:	jline >= 0.8.1
Requires:	jsch >= 0.1.20
Requires(post):	jsch >= 0.1.20
Requires:	jtidy >= 1.0
Requires:	maven2-common-poms >= 1.0-5
Requires:	maven-jxr >= 1.0
Requires:	maven-wagon >= 1.0-0.1.b2
Requires(post):	maven-wagon >= 1.0-0.1.b2
Requires:	nekohtml >= 0.9.3
Requires:	plexus-ant-factory >= 1.0-0.a1.2
Requires:	plexus-bsh-factory >= 1.0-0.a7s.2
Requires:	plexus-archiver >= 1.0-0.a6
Requires:	plexus-compiler >= 1.5.1
Requires:	plexus-container-default >= 1.0
Requires(post):	plexus-container-default >= 1.0
Requires:	plexus-i18n >= 1.0
Requires:	plexus-interactivity >= 1.0
Requires(post):	plexus-interactivity >= 1.0
Requires:	plexus-utils >= 1.2
Requires(post):	plexus-utils >= 1.2
Requires:	plexus-velocity >= 1.1.2
Requires:	pmd >= 3.6

### Bootstrap {{{
%if %{without bootstrap}
Requires:		%{name} = %{version}
Requires:	maven-doxia >= 1.0-0.a9
Requires(post):	maven-doxia >= 1.0-0.a9
Requires:	maven-scm >= 0:1.0-0.b3.2
Requires:	maven-scm-test >= 0:1.0-0.b3.2
Requires:	maven-shared-invoker
Requires:		 maven-shared-io
Requires:	maven-shared-file-management >= 1.0-4
Requires:	maven-shared-jar
Requires:	maven-shared-model-converter
Requires:	maven-shared-verifier
Requires:	maven-surefire >= 2.0
Requires:	maven-surefire-booter >= 2.0
Requires:	modello >= 1.0-0.a8.3
Requires:	modello-maven-plugin >= 1.0-0.a8.3
%endif
### }}}

### }}}
### END OF OLD JPP DEPENDENCIES }}}

BuildRoot:		%{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch:	noarch

%description
Maven is a software project management and comprehension tool. Based on the 
concept of a project object model (POM), Maven can manage a project's build,
reporting and documentation from a central piece of information.

%package        javadoc
Summary:	Javadoc for %{name}
Group:	Development/Documentation
Requires(post):	/bin/rm,/bin/ln
Requires(postun):	/bin/rm

%description    javadoc
%{summary}.

%package        manual
Summary:	Documents for %{name}
Group:	Development/Documentation

%description    manual
%{summary}.

%package        plugin-ant
Summary:	Ant plugin for maven
Group:	Development/Build Tools
Requires:	ant >= 1.6.5
Requires:	ant-junit
Requires:	ant-nodeps
Requires:	junit >= 3.8.2
Requires:	maven-wagon >= 1.0-0.1.b2
Requires:	plexus-utils >= 1.2
Requires:	xalan-j2 >= 2.6.0
Requires:		xml-commons-apis >= 1.3.02
Requires:		plexus-container-default
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}

%description    plugin-ant
Generates an Ant build file for the project.

%package        plugin-antlr
Summary:	Antlr plugin for maven
Group:	Development/Build Tools
Requires:	antlr >= 2.7.4
Requires:		plexus-container-default
Requires:	plexus-i18n >= 1.0
%if %{without bootstrap}
Requires:	maven-doxia >= 1.0-0.a9
Requires:	maven-doxia-sitetools >= 1.0
%endif
Requires:	plexus-utils >= 1.2
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}

%description    plugin-antlr
Generates sources from an Antlr grammar.

%package        plugin-antrun
Summary:	Antrun plugin for maven
Group:	Development/Build Tools
Requires:	ant >= 1.6.5
Requires:		maven-embedder
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:		maven-shared-reporting-impl

%description    plugin-antrun
Runs a set of ant tasks from a phase of the build.


%package        plugin-assembly
Summary:	Assembly plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
%if %{without bootstrap}
Requires:	modello >= 1.0-0.a8.3
%endif
Requires:	plexus-archiver >= 1.0
Requires:	plexus-utils >= 1.2
Requires:		maven-shared-file-management >= 1.0
Requires:		maven-shared-archiver
Requires:		plexus-container-default
Requires:		maven-shared-repository-builder
Requires:		maven-shared-common-artifact-filters
Requires:		maven-shared-plugin-testing-tools
Requires:		maven-shared-test-tools
Requires:	jmock >= 1.0.1
Requires:	jdom >= 1.0
Requires:	jaxen >= 1.1
Requires:		saxpath
Requires:	junit >= 3.8.2

%description    plugin-assembly
Builds an assembly (distribution) of sources and/or binaries.

%package        plugin-changelog
Summary:	Changelog plugin for maven
Group:	Development/Build Tools
%if %{without bootstrap}
Requires:	maven-scm
%endif
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	maven-doxia >= 1.0-0.a9
Requires:	maven-doxia-sitetools >= 1.0
Requires:	maven-scm >= 0:1.0-0.b3.2
Requires:		maven-shared-reporting-impl

%description    plugin-changelog
The Maven Changelog Plugin generates reports regarding the recent changes in
your Software Configuration Management or SCM.

%package        plugin-changes
Summary:	Changes plugin for maven
Group:	Development/Build Tools
%if %{without bootstrap}
Requires:	maven-doxia
Requires:	maven-doxia-sitetools >= 1.0
%endif
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	velocity
Requires:	commons-httpclient
Requires:	plexus-velocity >= 1.1.2
Requires:	plexus-mail-sender
Requires:	glassfish-javamail
Requires:	jakarta-commons-lang
Requires:	velocity
Requires:		maven-shared-reporting-impl

%description    plugin-changes
The Maven Changes Plugin is used to inform users of the changes that have 
occured between different releases of your project.  

%package        plugin-checkstyle
Summary:	Checkstyle plugin for maven
Group:	Development/Build Tools
Requires:	checkstyle4 >= 4.1
Requires:		checkstyle4-optional >= 4.1
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	plexus-utils >= 1.2
Requires:	plexus-velocity >= 1.1.2
Requires:	plexus-resources
Requires:		maven-shared-reporting-impl

%description    plugin-checkstyle
Generates a checkstyle report.


%package        plugin-clean
Summary:	Clean plugin for maven
Group:	Development/Build Tools
Requires:	junit >= 3.8.2
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	plexus-utils >= 1.2

%description    plugin-clean
Cleans up files generated during build.

%package        plugin-compiler
Summary:	Compiler plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	plexus-compiler >= 1.5.1
Requires:	plexus-utils >= 1.2

%description    plugin-compiler
Compiles Java sources.

%package        plugin-dependency
Summary:	Dependency plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	plexus-archiver >= 1.0
Requires:	plexus-utils >= 1.2
Requires:	maven-shared-file-management >= 1.0-4
Requires:	junit >= 3.8.2
Requires:	plexus-container-default
Requires:	maven-shared-dependency-analyzer
Requires:	maven-shared-dependency-tree

%description    plugin-dependency
The dependency plugin provides the capability to manipulate artifacts. It can
copy and/or unpack artifacts from local or remote repositories to a specified
location.

%package        plugin-deploy
Summary:	Deploy plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}

%description    plugin-deploy
Deploys the built artifacts to a remote repository.


%package        plugin-doap
Summary:	Description of a Project (DOAP) plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	plexus-utils

%description    plugin-doap
The Maven DOAP Plugin generates a Description of a Project (DOAP) file from
a POM.


%package        plugin-docck
Summary:	DOCCK plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	plexus-utils
Requires:	maven-shared-plugin-tools-beanshell >= 2.2
Requires:	maven-shared-plugin-tools-java >= 2.2
Requires:	commons-httpclient
Requires:	jakarta-commons-logging >= 1.0.4
Requires:	maven-shared-file-management >= 1.0-4
Requires:	maven-shared-plugin-tools-api
Requires:		maven-shared-reporting-impl

%description    plugin-docck
The Maven DOCCK Plugin checks that a project complies with the 
Plugin Documentation Standard.


%package        plugin-ear
Summary:	Ear plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	plexus-utils >= 1.2
Requires:	maven-shared-verifier
Requires:	xmlunit

%description    plugin-ear
Generates an EAR from the current project.


%package        plugin-eclipse
Summary:	Eclipse plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	plexus-utils >= 1.2
Requires:	plexus-archiver >= 1.0
Requires:	jmock >= 1.0.1
Requires:	jdom >= 1.0
Requires:	jaxen >= 1.1
Requires:		saxpath
Requires:	plexus-interactivity >= 1.0
Requires:		maven-shared-plugin-testing-tools
Requires:		maven-shared-test-tools
Requires:	aqute-bndlib

%description    plugin-eclipse
Generates an Eclipse project file for the current project.


%package        plugin-ejb
Summary:	EJB plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}

%description    plugin-ejb
Builds an EJB (and optional client) from the current project.


%package        plugin-gpg
Summary:	GPG plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	jakarta-commons-lang
Requires:	plexus-utils
Requires:	jakarta-commons-lang
Requires:	junit >= 3.8.2

%description    plugin-gpg
The Maven GPG Plugin signs all of the project's attached artifacts with GnuPG.


%package        plugin-help
Summary:	Help plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	maven-shared-plugin-tools-api

%description    plugin-help
Gets information about the working environment for the project.


%package        plugin-idea
Summary:	Idea plugin for maven
Group:	Development/Build Tools
Requires:	dom4j >= 1.6.1
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	maven-wagon >= 1.0-0.1.b2
Requires:	plexus-utils >= 1.2
Requires:	jmock >= 1.0.1

%description    plugin-idea
Creates/updates an IDEA workspace for the current project 
(individual modules are created as IDEA modules).


%package        plugin-install
Summary:	Install plugin for maven
Group:	Development/Build Tools
Requires:	plexus-digest >= 1.0
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}

%description    plugin-install
Installs the built artifact into the local repository.

%package        plugin-invoker
Summary:	Invoker plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
%if %{without bootstrap}
Requires:	maven-shared
Requires:	maven-shared-invoker
Requires:	maven-shared-file-management >= 1.0-4
Requires:		maven-shared-io
%endif
Requires:	bsh

%description    plugin-invoker
The Maven Invoker Plugin is used to run a set of Maven projects and makes 
sure that each project execution is successful, and optionally verifies 
the output from a given project execution.

%package        plugin-jar
Summary:	Jar plugin for maven
Group:	Development/Build Tools
Requires:	jakarta-commons-lang >= 2.1
Requires:		%{name} = %{version}-%{release}
Requires:	maven-shared-archiver >= 2.3
Requires(postun):		%{name} = %{version}-%{release}
Requires:	plexus-utils >= 1.2

%description    plugin-jar
Builds a JAR from the current project.


%package        plugin-javadoc
Summary:	Javadoc plugin for maven
Group:	Development/Build Tools
Requires:	jakarta-commons-lang >= 2.1
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
%if %{without bootstrap}
Requires:	modello >= 1.0-0.a8.3
%endif
Requires:	plexus-archiver >= 1.0
Requires:	plexus-utils >= 1.2
Requires:		maven-shared-reporting-impl

%description    plugin-javadoc
Generates Javadoc for the project.

%package        plugin-one
Summary:	One plugin for maven
Group:	Development/Build Tools
Requires:	junit >= 3.8.2
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	plexus-archiver >= 1.0
Requires:	plexus-utils >= 1.2
Requires:	junit >= 3.8.2
Requires:	maven-shared-model-converter

%description    plugin-one
A plugin for interacting with legacy Maven 1.x repositories and builds.


%package        plugin-plugin
Summary:	Plugin plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	maven-shared-plugin-tools-beanshell >= 2.2
Requires:	maven-shared-plugin-tools-java >= 2.2
Requires:		maven-shared-reporting-impl
Requires:	maven-doxia >= 1.0-0.a9
Requires:	plexus-utils >= 1.2
Requires:	plexus-container-default

%description    plugin-plugin
Creates a Maven plugin descriptor for any Mojo's found in the source tree, 
to include in the JAR.


%package        plugin-pmd
Summary:	Pmd plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	plexus-utils >= 1.2
Requires:	plexus-resources
Requires:	pmd >= 3.3
Requires:	jaxen >= 1.1
Requires:	xom
Requires:		maven-shared-reporting-impl

%description    plugin-pmd
Generates a PMD report.


%package        plugin-project-info-reports
Summary:	Project-info-reports plugin for maven
Group:	Development/Build Tools
Requires:	httpunit >= 1.6
Requires:	jakarta-commons-validator >= 1.1.4
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	plexus-i18n >= 1.0
Requires:		maven-shared-reporting-impl
Requires:	maven-shared-jar
Requires:	maven-shared-dependency-tree
Requires:	maven-wagon
Requires:	maven-scm >= 0:1.0-0.b3.2
Requires:	maven-doxia >= 1.0-0.a9
Requires:	maven-doxia-sitetools >= 1.0

%description    plugin-project-info-reports
Generates standard project reports.

%package        plugin-rar
Summary:	Rar plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}

%description    plugin-rar
Builds a RAR from the current project.


%package        plugin-remote-resources
Summary:	Remote Resources plugin for maven
Group:	Development/Build Tools
Requires:	junit >= 3.8.2
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	plexus-container-default
Requires:	plexus-utils
Requires:	plexus-velocity
Requires:	velocity
%if %{without bootstrap}
Requires:	maven-shared
Requires:	maven-shared-downloader
Requires:	plexus-resources
%endif

%description    plugin-remote-resources
The Maven Remote Resources Plugin is used to retrieve JARs of resources
from remote repositories, processes those resources, and incorporate them
into JARs built with maven.

%package        plugin-repository
Summary:	Repository plugin for maven
Group:	Development/Build Tools
Requires:	junit >= 3.8.2
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	plexus-archiver >= 1.0

%description    plugin-repository
Plugin to help with repository-based tasks.

%package        plugin-resources
Summary:	Resources plugin for maven
Group:	Development/Build Tools
#Requires:	jakarta-commons-io >= 1.1
Requires:	plexus-utils >= 1.2
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}

%description    plugin-resources
Copies the resources to the output directory for including in the JAR.

%package        plugin-site
Summary:	Site plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
%if %{without bootstrap}
Requires:	maven-doxia >= 1.0-0.a9
Requires:	maven-doxia-sitetools >= 1.0
%endif
Requires:	plexus-utils >= 1.2

%description    plugin-site
Generates a site for the current project.

%package        plugin-source
Summary:	Source plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	plexus-archiver >= 1.0
Requires:	plexus-utils >= 1.2
Requires:	plexus-container-default >= 1.0
Requires:	junit >= 3.8.2

%description    plugin-source
Builds a JAR of sources for use in IDEs and distribution to the repository.


%package        plugin-stage
Summary:	Stage plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	maven-wagon
Requires:	plexus-utils
Requires:	junit >= 3.8.2

%description    plugin-stage
Maven Stage Plugin copies artifacts from one repository to another.


%package        plugin-verifier
Summary:	Verifier plugin for maven
Group:	Development/Build Tools
Requires:	junit >= 3.8.2
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
%if %{without bootstrap}
Requires:	modello >= 1.0-0.a8.3
%endif
Requires:	plexus-utils >= 1.2

%description    plugin-verifier
Useful for integration tests - verifies the existence of certain conditions.

%package        plugin-war
Summary:	War plugin for maven
Group:	Development/Build Tools
Requires:		%{name} = %{version}-%{release}
Requires(postun):		%{name} = %{version}-%{release}
Requires:	plexus-utils >= 1.2
Requires:	junit >= 3.8.2

%description    plugin-war
Builds a WAR from the current project.

%if %{with repolib}
%package repolib
Summary:	Artifacts to be uploaded to a repository library
Group:	Development/Libraries/Java

%description repolib
Artifacts to be uploaded to a repository library.
This package is not meant to be installed but so its contents
can be extracted through rpm2cpio.
%endif

%prep
#rpm -ql maven-surefire

%setup -q -c -n %{name}

# Extract the plugins
tar xzf %{SOURCE2}

# We need to replace the javadoc plugin as the 2.3-SNAPSHOT included above 
# has several bugs
rm -rf maven-plugins/maven-javadoc-plugin
rm -rf maven-plugins/maven-enforcer-plugin
tar xzf %{SOURCE22} -C maven-plugins

# Use an older version of site plugin because newer one requires newer doxia 
# (1.0a8) which is not compatible with the older one (1.0a7) which is needed 
# by other parts of maven
#rm -rf maven-plugins/maven-site-plugin
#tar xzf %{SOURCE8}

# javadoc 2.4 uses an old doxia method
%patch15

# This plugin can't cope with a JAR without a JDK version on it
%patch16

%patch17

%patch18
%patch19

%patch20

# Remove dependencies on org.codehaus.doxia.* (it is now
# org.apache.maven.doxia, and in the interest of maintaining just one
# doxia jar, we substitute things accordingly)

for i in    maven-plugins/maven-changelog-plugin/src/main/java/org/apache/maven/plugin/changelog/FileActivityReport.java \
            maven-plugins/maven-changelog-plugin/src/main/java/org/apache/maven/plugin/changelog/ChangeLogReport.java \
            maven-plugins/maven-changelog-plugin/src/main/java/org/apache/maven/plugin/changelog/DeveloperActivityReport.java \
            maven-plugins/maven-javadoc-plugin/src/main/java/org/apache/maven/plugin/javadoc/JavadocReport.java \
            maven-plugins/maven-plugin-plugin/src/main/java/org/apache/maven/plugin/plugin/PluginReport.java \
            maven/maven-reporting/maven-reporting-api/src/main/java/org/apache/maven/reporting/MavenReport.java \
            maven-plugins/maven-antlr-plugin/src/main/java/org/apache/maven/plugin/antlr/AntlrHtmlReport.java \
            maven-plugins/maven-pmd-plugin/src/main/java/org/apache/maven/plugin/pmd/AbstractPmdReport.java \
            maven-plugins/maven-pmd-plugin/src/main/java/org/apache/maven/plugin/pmd/CpdReportGenerator.java \
            maven-plugins/maven-pmd-plugin/src/main/java/org/apache/maven/plugin/pmd/PmdReport.java \
            maven-plugins/maven-pmd-plugin/src/main/java/org/apache/maven/plugin/pmd/PmdReportListener.java \
            maven-plugins/maven-checkstyle-plugin/src/main/java/org/apache/maven/plugin/checkstyle/CheckstyleReport.java \
            maven-plugins/maven-checkstyle-plugin/src/main/java/org/apache/maven/plugin/checkstyle/CheckstyleReportGenerator.java; do

    sed -i -e s:org.codehaus.doxia.sink.Sink:org.apache.maven.doxia.sink.Sink:g $i
    sed -i -e s:org.codehaus.doxia.site.renderer.SiteRenderer:org.apache.maven.doxia.siterenderer.Renderer:g $i
    sed -i -r -e s:\(\\s+\)SiteRenderer\(\\s+\):\\1Renderer\\2:g $i
done

# Remove existing binaries from source trees
#find . -name "*.jar" -exec rm -f '{}' \;

%patch0
%patch1
%patch2
%patch3
%patch4
%patch5

# keep external jars out of uber jar only in non-bootstrap mode
%if %{without bootstrap}
%patch6
%endif


%patch7

%if %{with bootstrap}
%patch8
%endif

%patch9
%patch10
%patch11
%patch12
# javadoc 2.5 no longer needs this patch
#%patch13
# javadoc 2.5 pre-reqs maven 2.0.9 by default
#%patch14

# FIXME: Maven eclipse plugin tests are disabled for now, until a way
# is found to stop it from connecting to the web despite offline mode.
rm -rf maven-plugins/maven-eclipse-plugin/src/test/*

# FIXME: Disabled items:

#Disabled goal (because we don't want a jetty dependency)
rm -f maven-plugins/maven-site-plugin/src/main/java/org/apache/maven/plugins/site/SiteRunMojo.java

# Disabled test because it needs cglib
rm -f maven-plugins/maven-release-plugin/src/test/java/org/apache/maven/plugins/release/PrepareReleaseMojoTest.java

# Disabled test because it needs mock
rm -f maven/maven-artifact-manager/src/test/java/org/apache/maven/artifact/testutils/MockManager.java 
rm -f maven/maven-artifact-manager/src/test/java/org/apache/maven/artifact/repository/metadata/AbstractRepositoryMetadataTest.java

# extract poms and jars (if any)
tar xzf %{SOURCE3}

# extract jars iff in bootstrap mode
%if %{with bootstrap}
tar xzf %{SOURCE4}
%endif

# Copy model-v3
cp -p %{SOURCE10} m2_repo/repository/JPP/maven2/model-v3.jar

mkdir external_repo
ln -s %{_javadir} external_repo/JPP

cp -p %{SOURCE6} maven/maven-artifact/src/main/java/org/apache/maven/artifact/repository/layout/JPackageRepositoryLayout.java
cp -p %{SOURCE11} maven/maven-artifact/src/main/java/org/apache/maven/artifact/repository/layout/MavenJPackageDepmap.java

# FIXME: bootstrap-mini has no dependencies, so we copy the file there 
# (for now). Since bootstrap classes are not in the final package, there 
# will be no duplicates.
mkdir -p maven/bootstrap/bootstrap-mini/src/main/java/org/apache/maven/artifact/repository/layout/
cp -p %{SOURCE11} maven/bootstrap/bootstrap-mini/src/main/java/org/apache/maven/artifact/repository/layout/MavenJPackageDepmap.java

cp -p %{SOURCE7} %{maven_settings_file}
sed -i -e "s|<url>__INTERNAL_REPO_PLACEHOLDER__</url>|<url>file://`pwd`/m2_repo/repository</url>|g" %{maven_settings_file}
%if %{with bootstrap}
sed -i -e "s|<url>__EXTERNAL_REPO_PLACEHOLDER__</url>|<url>file://`pwd`/external_repo</url>|g" %{maven_settings_file}
%else
sed -i -e "s|<url>__EXTERNAL_REPO_PLACEHOLDER__</url>|<url>file://%{_datadir}/%{name}/repository</url>|g" %{maven_settings_file}
%endif

sed -i -e "s|__INTERNAL_REPO_PLACEHOLDER__|file://`pwd`/m2_repo/repository|g" maven/bootstrap/bootstrap-mini/src/main/java/org/apache/maven/bootstrap/download/OnlineArtifactDownloader.java

%if %{with bootstrap}
sed -i -e "s|__EXTERNAL_REPO_PLACEHOLDER__|file://`pwd`/external_repo|g" maven/bootstrap/bootstrap-mini/src/main/java/org/apache/maven/bootstrap/download/OnlineArtifactDownloader.java
%else
sed -i -e "s|__EXTERNAL_REPO_PLACEHOLDER__|file://%{_datadir}/%{name}/repository|g" maven/bootstrap/bootstrap-mini/src/main/java/org/apache/maven/bootstrap/download/OnlineArtifactDownloader.java
%endif

# Copy the empty dependency jar/pom in place
mkdir -p m2_repo/repository/JPP/maven2/default_poms
cp -p %{SOURCE13} m2_repo/repository/JPP/maven2/default_poms/JPP.maven-empty-dep.pom
cp -p %{SOURCE14} m2_repo/repository/JPP/maven2/empty-dep.jar

%build
# Fix maven-remote-resources-plugin
# we now use plexus-velocity 1.1.7 which has the correct descriptor with a hint.
rm -f maven-plugins/maven-remote-resources-plugin/src/main/resources/META-INF/plexus/components.xml

# Wire in jdom dependency
cp -p maven/maven-artifact/pom.xml maven/maven-artifact/pom.xml.withoutjdom
saxon -o maven/maven-artifact/pom.xml maven/maven-artifact/pom.xml.withoutjdom /usr/share/java-utils/xml/mavenjpp-mapdeps.xsl map=%{SOURCE12}
saxon -o m2_repo/repository/JPP/maven2/poms/JPP.maven2-artifact.pom maven/maven-artifact/pom.xml.withoutjdom /usr/share/java-utils/xml/mavenjpp-mapdeps.xsl map=%{SOURCE12}

# for uber jar
cp -p maven/maven-core/pom.xml maven/maven-core/pom.xml.withoutjdom
saxon -o maven/maven-core/pom.xml maven/maven-core/pom.xml.withoutjdom /usr/share/java-utils/xml/mavenjpp-mapdeps.xsl map=%{SOURCE12}

cp -p maven/bootstrap/bootstrap-installer/pom.xml maven/bootstrap/bootstrap-installer/pom.xml.withoutjdom
saxon -o maven/bootstrap/bootstrap-installer/pom.xml maven/bootstrap/bootstrap-installer/pom.xml.withoutjdom /usr/share/java-utils/xml/mavenjpp-mapdeps.xsl map=%{SOURCE12}

mkdir -p maven/maven-plugins/maven-assembly-plugin/target/generated-resources/plexus/META-INF/plexus/components.xml
touch maven/maven-plugins/maven-assembly-plugin/target/generated-resources/plexus/META-INF/plexus/components.xml

# Build maven
export MAVEN_REPO_LOCAL=`pwd`/%{repo_dir}
export M2_SETTINGS_FILE=%{maven_settings_file}

# In bootstrap mode, we want it looking at default poms only (controlled via 
# maven-common-poms). This enables us to change naming structures without 
# breaking build.

export MAVEN_OPTS="$MAVEN_OPTS -Dmaven.repo.local=$MAVEN_REPO_LOCAL -Dmaven2.ignore.versions -Dmaven2.offline.mode -Dmaven.test.failure.ignore=true -Dmaven2.jpp.depmap.file=%{SOURCE17}"
export M2_HOME=`pwd`/maven/home/apache-%{name}-%{version}

%if %{with bootstrap}
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven2.jpp.default.repo=`pwd`/external_repo"
%else
export MAVEN_OPTS="$MAVEN_OPTS -Dmaven2.jpp.default.repo=%{_datadir}/%{name}/repository"
%endif

cd %{name} # {{{

[ -z "$JAVA_HOME" ] && JAVA_HOME=%{_jvmdir}/java
export JAVA_HOME

mkdir bootstrap/lib
ln -s $(build-classpath jdom) bootstrap/lib/jdom.jar
export CLASSPATH=`pwd`/bootstrap/lib/jdom.jar
export JDOMCLASS=$CLASSPATH
./bootstrap.sh --prefix=`pwd`/home  --settings=%{maven_settings_file}
unset CLASSPATH

cd - # cd %{name} }}}

# Update the classworlds jar name in the mvn script
sed -i -e s:"/core/boot/classworlds-\*.jar":/core/boot/classworlds\*.jar:g $M2_HOME/bin/mvn

# In non-bootstrap mode, external jars are kept out of the uber jar. Copy those
# jars in for now (linked in %%post)

%if %{without bootstrap}
(cd $M2_HOME/lib
cp ../../../../m2_home_local/repository/com/jcraft/jsch/0.1.24/jsch-0.1.24.jar jsch.jar
cp ../../../../m2_home_local/repository/org/codehaus/plexus/plexus-utils/1.4.6/plexus-utils-1.4.6.jar plexus-utils.jar
cp ../../../../m2_home_local/repository/commons-cli/commons-cli/1.0/commons-cli-1.0.jar commons-cli.jar
cp ../../../../m2_home_local/repository/org/apache/maven/doxia/doxia-sink-api/1.0-alpha-7/doxia-sink-api-1.0-alpha-7.jar doxia-sink-api.jar
cp ../../../../m2_home_local/repository/org/codehaus/plexus/plexus-container-default/1.0-alpha-8/plexus-container-default-1.0-alpha-8.jar plexus-container-default.jar
cp ../../../../m2_home_local/repository/org/codehaus/plexus/plexus-interactivity-api/1.0-alpha-4/plexus-interactivity-api-1.0-alpha-4.jar plexus-interactivity-api.jar
cp ../../../../m2_home_local/repository/jtidy/jtidy/4aug2000r7-dev/jtidy-4aug2000r7-dev.jar jtidy.jar
)

build-jar-repository -s -p $M2_HOME/lib jdom maven-wagon/file maven-wagon/http-lightweight maven-wagon/http-shared maven-wagon/provider-api maven-wagon/ssh maven-wagon/ssh-common maven-wagon/ssh-external
%endif

# Build plugins
cd maven-plugins # {{{

# Build the plugin-plugin first, as it is needed to build itself later on
# NOTE: Build of this plugin for the first time is expected to cause errors. 
# That is why we build it first with -fn . Subsequent builds should not have 
# errors, and if they do, they will be caught when all plugins are built 
# again below. See: http://mail-archives.apache.org/mod_mbox/maven-users/200511.mbox/%3c4374C819.7090609@commonjava.org%3e

(cd maven-plugin-plugin
$M2_HOME/bin/mvn -e --batch-mode -s %{maven_settings_file} $MAVEN_OPTS -npu --no-plugin-registry -fn clean install 
)

# Disable clover plugin. We don't have a clover package yet.
sed -i -e s:"<module>maven-clover-plugin</module>"::g pom.xml

# Now build everything
# FIXME: Need to build in two stages to get around gcj bug that causes plugin reload to fail
#$M2_HOME/bin/mvn -e --batch-mode -s %{maven_settings_file} $MAVEN_OPTS -Dmaven.test.skip=true -npu --no-plugin-registry -fn verify  
$M2_HOME/bin/mvn -e --batch-mode -s %{maven_settings_file} $MAVEN_OPTS -Dmaven.test.skip=true -npu --no-plugin-registry verify  
$M2_HOME/bin/mvn -e --batch-mode -s %{maven_settings_file} $MAVEN_OPTS -Dmaven.test.skip=true -npu --no-plugin-registry --fail-at-end jar:jar install:install

cd - # }}}

%if %{without bootstrap}
# Build model-all JAR  (for model-v3 classes)
cd maven/maven-model # {{{

$M2_HOME/bin/mvn -e -s %{maven_settings_file} $MAVEN_OPTS -P all-models package

cd - # }}}
%endif

# Build complete. Run it tests.

%if %{with itests}

(cd maven

# One of the tests (#63) needs tools.jar. Fix the path for it
sed -i -e s:"<systemPath>\${java.home}/../lib/tools.jar</systemPath>":"<systemPath>$JAVA_HOME/lib/tools.jar</systemPath>":g maven-core-it/it0063/pom.xml 

(cd integration-tests/maven-core-it-plugin
$M2_HOME/bin/mvn -s %{maven_settings_file} $MAVEN_OPTS org.apache.maven.plugins:maven-plugin-plugin:2.1.1-SNAPSHOT:descriptor org.apache.maven.plugins:maven-resources-plugin:2.2-SNAPSHOT:resources org.apache.maven.plugins:maven-compiler-plugin:2.1-SNAPSHOT:compile org.apache.maven.plugins:maven-jar-plugin:2.1-SNAPSHOT:jar org.apache.maven.plugins:maven-install-plugin:2.2-SNAPSHOT:install
$M2_HOME/bin/mvn -s %{maven_settings_file} $MAVEN_OPTS org.apache.maven.plugins:maven-install-plugin:2.2-SNAPSHOT:install-file -DgroupId=org.apache.maven.plugins -DartifactId=maven-core-it-plugin -Dversion=%{version}-JPP -Dpackaging=maven-plugin -Dfile=target/maven-core-it-plugin-1.0-SNAPSHOT.jar
)

for i in `find integration-tests/maven-core-it-support -name pom.xml`; do
    cd `dirname $i` # {{{
        $M2_HOME/bin/mvn -s %{maven_settings_file} $MAVEN_OPTS org.apache.maven.plugins:maven-plugin-plugin:2.1.1-SNAPSHOT::descriptor org.apache.maven.plugins:maven-resources-plugin:2.2-SNAPSHOT:resources org.apache.maven.plugins:maven-compiler-plugin:2.1-SNAPSHOT:compile  org.apache.maven.plugins:maven-jar-plugin:2.1-SNAPSHOT:jar org.apache.maven.plugins:maven-install-plugin:2.2-SNAPSHOT:install
    cd - # }}}
done

# Test 41 expects core-it-support 1.2 to be packed as a coreit-artifact
(cd integration-tests/maven-core-it-support/1.2
$M2_HOME/bin/mvn -s %{maven_settings_file} $MAVEN_OPTS org.apache.maven.plugins:maven-install-plugin:2.2-SNAPSHOT:install-file -DgroupId=org.apache.maven -DartifactId=maven-core-it-support -Dversion=1.2 -Dpackaging=coreit-artifact -Dfile=target/maven-core-it-support-1.2.jar
)

OLD_MAVEN_OPTS=$MAVEN_OPTS
MAVEN_OPTS="$MAVEN_OPTS -Dmaven.settings.file=$M2_SETTINGS_FILE -Dmaven2.ignore.versions  -Dmaven2.jpp.mode -Dmaven2.jpp.mode=true"
sh -x %{SOURCE9}
export MAVEN_OPTS=$OLD_MAVEN_OPTS
)

%endif

# Build docs

# Manual iteration should not be needed, but there is a bug in the javadoc 
# plugin which makes this necessary. See: 
# http://jira.codehaus.org/browse/MJAVADOC-157

(cd maven
for dir in `find -maxdepth 1 -type d`; do

    if [ "$dir" == "./maven-core-it-runner" ]; then
        continue
    fi

    if [ ! -f $dir/pom.xml ]; then
        continue
    fi 

    cd $dir # {{{
    $M2_HOME/bin/mvn -s %{maven_settings_file} $MAVEN_OPTS -Dmaven2.usejppjars org.apache.maven.plugins:maven-javadoc-plugin:2.3-SNAPSHOT:javadoc
    cd - # }}}
done
)
(cd maven-plugins
for dir in `find -maxdepth 1 -type d`; do

    if [ "$dir" == "./maven-clover-plugin" ]; then
        continue
    fi

    if [ ! -f $dir/pom.xml ]; then
        continue
    fi

    cd $dir # {{{
    $M2_HOME/bin/mvn -s %{maven_settings_file} $MAVEN_OPTS -Dmaven2.usejppjars org.apache.maven.plugins:maven-javadoc-plugin:2.3-SNAPSHOT:javadoc
    cd - # }}}
done
)

%install
rm -rf $RPM_BUILD_ROOT

export M2_HOME=`pwd`/maven/home/apache-%{name}-%{version}

# Repository
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/repository

# Items in /usr/bin/
install -dm 755 $RPM_BUILD_ROOT%{_bindir}
install -pm 755 %{SOURCE5} $RPM_BUILD_ROOT%{_bindir}/mvn
install -pm 755 %{SOURCE15} $RPM_BUILD_ROOT%{_bindir}/mvn-jpp

# maven.home
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/bin
cp -p $M2_HOME/bin/* $RPM_BUILD_ROOT%{_datadir}/%{name}/bin

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/boot

%if %{with bootstrap}
cp -p $M2_HOME/boot/classworlds* $RPM_BUILD_ROOT%{_datadir}/%{name}/boot/classworlds.jar
%endif

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/conf
install -m 644 $M2_HOME/conf/* $RPM_BUILD_ROOT%{_datadir}/%{name}/conf

install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/lib
cp -p $M2_HOME/lib/* $RPM_BUILD_ROOT%{_datadir}/%{name}/lib

# Also, link maven jars from /usr/share/java
install -dm 755 $RPM_BUILD_ROOT%{_javadir}/%{name}
for library in $RPM_BUILD_ROOT%{_datadir}/%{name}/lib/maven-%{version}-uber.jar; do
    ln -s ../../%{name}/lib/`basename $library` $RPM_BUILD_ROOT%{_javadir}/%{name}/maven-uber.jar
done

# Install component poms and jars
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/poms
cd %{name} # {{{
    for project in maven-artifact \
        maven-artifact-manager \
        maven-artifact-test \
        maven-core \
        maven-error-diagnostics \
        maven-model \
        maven-monitor \
        maven-plugin-api \
        maven-plugin-descriptor \
        maven-plugin-parameter-documenter \
        maven-plugin-registry \
        maven-profile \
        maven-project \
        maven-repository-metadata \
        maven-settings; do 

        artifactname=`echo $project | sed -e s:^maven-::g`
        cp -p $project/pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-$artifactname.pom

        # dependency fragments
        %add_to_maven_depmap org.apache.maven $project %{version} JPP/%{name} $artifactname

        install -m 644 $project/target/$project-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$artifactname-%{version}.jar

%if %{without bootstrap}
        if [ "$project" == "maven-model" ]; then
          install -m 644 $project/target/$project-%{version}-all.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/$artifactname-all-%{version}.jar
        fi
%endif

    done
cd - # }}}

# reporting api
cp -p %{name}/maven-reporting/maven-reporting-api/pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-reporting-api.pom
%add_to_maven_depmap org.apache.maven.reporting maven-reporting-api %{version} JPP/%{name} reporting-api
install -m 644 %{name}/maven-reporting/maven-reporting-api/target/*jar $RPM_BUILD_ROOT%{_javadir}/%{name}/reporting-api-%{version}.jar 

# script, script-ant and script-beanshell
cp -p %{name}/maven-script/pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-script.pom
%add_to_maven_depmap org.apache.maven maven-script %{version} JPP/%{name} script

cp -p %{name}/maven-script/maven-script-ant/pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-script-ant.pom
%add_to_maven_depmap org.apache.maven maven-script-ant %{version} JPP/%{name} script-ant
install -pm 644 %{name}/maven-script/maven-script-ant/target/maven-script-ant-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/script-ant-%{version}.jar

cp -p %{name}/maven-script/maven-script-beanshell/pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-script-beanshell.pom
%add_to_maven_depmap org.apache.maven maven-script-beanshell %{version} JPP/%{name} script-beanshell
install -pm 644 %{name}/maven-script/maven-script-beanshell/target/maven-script-beanshell-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}/script-beanshell-%{version}.jar

# reporting pom
cp -p %{name}/maven-reporting/pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-reporting.pom
%add_to_maven_depmap org.apache.maven.reporting maven-reporting %{version} JPP/%{name} reporting

# maven pom
cp -p %{name}/pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}-maven.pom
%add_to_maven_depmap org.apache.maven maven %{version} JPP/%{name} maven

# Create versionless symlinks
(cd $RPM_BUILD_ROOT%{_javadir}/%{name} && for jar in *-%{version}*; do ln -sf ${jar} `echo $jar | sed  "s|-%{version}||g"`; done)

# plugins
install -dm 755 $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/

cd maven-plugins # {{{
    for targetdir in `find -mindepth 2 -maxdepth 2 -type d -name target`; do

        # Find the version version
        pluginname=`echo $targetdir | sed -e s:"^\\./"::g -e s:"/target$"::g`
        pluginversion=`ls $targetdir/*jar | awk -F / '{print $NF}' | sed -e s:"^$pluginname-"::g -e s:"\\.jar$"::g`
        artifactname=`echo $pluginname | sed -e s:^maven-::g`

        #jar 
        cp -p $targetdir/*jar $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/$artifactname-$pluginversion.jar
        ln -s $artifactname-$pluginversion.jar $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/$artifactname.jar

        # pom
        cp -p `dirname $targetdir`/pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.%{name}.plugins-$artifactname.pom
        %add_to_maven_depmap org.apache.maven.plugins $pluginname $pluginversion JPP/%{name}/plugins $artifactname

    done
cd - # }}}

# g=org.apache.maven.plugins a=maven-plugins needs to be copied manually, as 
# it get's changed to a=plugins (a=plugins and a=maven-plugins is the same 
# file, but the former is needed for compatiblity while newer projects use 
# the latter)
cp -p maven-plugins/target/*jar $RPM_BUILD_ROOT%{_datadir}/%{name}/plugins/maven-plugins.jar
cp -p maven-plugins/pom.xml $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.maven.plugins-maven-plugins.pom
%add_to_maven_depmap org.apache.maven.plugins maven-plugins 9-SNAPSHOT JPP/%{name}/plugins maven-plugins

# The empty dependencies
mkdir -p $RPM_BUILD_ROOT%{_datadir}/%{name}/poms
mkdir -p $RPM_BUILD_ROOT%{_javadir}/%{name}
cp -p %{SOURCE13} $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.maven-empty-dep.pom
cp -p %{SOURCE14} $RPM_BUILD_ROOT%{_javadir}/%{name}/empty-dep.jar

# For backwards compatibility
ln -s JPP.maven-core.pom $RPM_BUILD_ROOT%{_datadir}/%{name}/poms/JPP.maven-mavencore.pom

# javadocs
install -dm 755 $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

(cd maven
    for doc_dir in `find . -type d -name apidocs`; do 
        module=`echo $doc_dir | sed -e s:"^\\./"::g -e s:"/target/site/apidocs$"::g`
        targetdir=$RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/$module
        install -dm 755  $targetdir
        cp -pr $doc_dir/* $targetdir
    done
)

(cd maven-plugins
    for doc_dir in `find . -type d -name apidocs`; do 
        module=`echo $doc_dir | sed -e s:"^\\./"::g -e s:"/target/site/apidocs$"::g`
        targetdir=$RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}/$module
        install -dm 755 $targetdir
        cp -pr $doc_dir/* $targetdir
    done
)

# manual and jpp readme
install -dm 755 $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p %{name}/home/apache-%{name}-%{version}/*.txt $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
cp -p %{SOURCE16} $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}

# create appropriate links in /usr/share/java
ln -sf %{_datadir}/%{name}/poms $RPM_BUILD_ROOT%{_javadir}/%{name}
ln -sf %{_datadir}/%{name}/plugins $RPM_BUILD_ROOT%{_javadir}/%{name}

# Create repository links
ln -s %{_javadir} $RPM_BUILD_ROOT%{_datadir}/%{name}/repository/JPP

# Create the bootstrap repo
%if %{with bootstrap}
install -dm 755  $RPM_BUILD_ROOT%{_datadir}/%{name}/bootstrap_repo
tar xzf %{SOURCE4}
mv m2_repo/repository/JPP $RPM_BUILD_ROOT%{_datadir}/%{name}/bootstrap_repo/
rmdir -p m2_repo/repository
%endif

%if %{with repolib}
install -d -m 755 $RPM_BUILD_ROOT%{repodir}
install -d -m 755 $RPM_BUILD_ROOT%{repodirlib}
install -p -m 644 %{SOURCE100} $RPM_BUILD_ROOT%{repodir}/component-info.xml
sed -i 's/@VERSION@/%{version}-brew/g' $RPM_BUILD_ROOT%{repodir}/component-info.xml
tag=`echo %{name}-%{version}-%{release} | sed 's|\.|_|g'`
sed -i "s/@TAG@/$tag/g" $RPM_BUILD_ROOT%{repodir}/component-info.xml
install -d -m 755 $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE8} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE9} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE10} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE11} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE12} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE13} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE14} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE15} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE16} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE17} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{SOURCE22} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH0} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH1} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH2} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH3} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH4} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH5} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH6} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH7} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH8} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH9} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH10} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH11} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH12} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH14} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH16} $RPM_BUILD_ROOT%{repodirsrc}
install -p -m 644 %{PATCH18} $RPM_BUILD_ROOT%{repodirsrc}
for jar in project.jar settings.jar model.jar profile.jar artifact-manager.jar repository-metadata.jar artifact.jar plugin-registry.jar error-diagnostics.jar; do
    cp -p %{buildroot}%{_javadir}/%{name}/${jar} %{buildroot}%{repodirlib}/maven-${jar}
done
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post

# clear the old links
find %{_datadir}/%{name}/boot/ -type l -exec rm -f '{}' \;
find %{_datadir}/%{name}/lib/ -type l -exec rm -f '{}' \;

%if %{without bootstrap}
build-jar-repository -s -p %{_datadir}/%{name}/boot classworlds

build-jar-repository -s -p %{_datadir}/%{name}/lib \
                commons-cli \
                commons-lang \
                commons-logging \
                jsch \
                jtidy \
                maven-doxia/sink-api \
                maven-wagon/file \
                maven-wagon/http-lightweight \
                maven-wagon/http-shared \
                maven-wagon/provider-api \
                maven-wagon/ssh \
                maven-wagon/ssh-common \
                maven-wagon/ssh-external \
                plexus/container-default \
                plexus/interactivity-api \
                plexus/utils
%endif

build-jar-repository -s -p %{_datadir}/%{name}/lib \
                jdom

%update_maven_depmap

# We create links in %post in the dir's below. rm -rf them.
%preun -n %{name}
[ $1 = 0 ] || exit 0
rm -rf %{_datadir}/%{name}/lib/*
rm -rf %{_datadir}/%{name}/core/*

%postun
# FIXME: This doesn't always remove the plugins dir. It seems that rpm doesn't
# honour the Requires(postun) as it should, causing maven to get uninstalled 
# before some plugins are
if [ -d %{_javadir}/%{name} ] ; then rmdir --ignore-fail-on-non-empty %{_javadir}/%{name} >& /dev/null; fi
%update_maven_depmap

%files -n %{name}
%defattr(-,root,root,-)
%doc %{name}/maven-core/*.txt
%attr(0755,root,root) %{_bindir}/mvn
%attr(0755,root,root) %{_bindir}/mvn-jpp
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/bin
%{_datadir}/%{name}/bin/*.bat
%config(noreplace) %{_datadir}/%{name}/bin/*.conf
%attr(0755,root,root) %{_datadir}/%{name}/bin/m2
%attr(0755,root,root) %{_datadir}/%{name}/bin/mvn
%attr(0755,root,root) %{_datadir}/%{name}/bin/mvnDebug
%{_datadir}/%{name}/boot
%{_datadir}/%{name}/conf
%{_datadir}/%{name}/lib
%{_datadir}/%{name}/plugins/maven-plugins*jar
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/poms
%{_datadir}/%{name}/repository
%{_mavendepmapfragdir}
%{_javadir}/%{name}

%if %{with bootstrap}
%{_datadir}/%{name}/bootstrap_repo
%endif

%files javadoc
%defattr(-,root,root,-)
%doc %{_javadocdir}/*

%files manual
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{version}

%files plugin-ant
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/ant-plugin*.jar

%files plugin-antlr
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/antlr-plugin*.jar

%files plugin-antrun
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/antrun-plugin*.jar

%files plugin-assembly
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/assembly-plugin*.jar

%files plugin-changelog
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/changelog-plugin*.jar

%files plugin-changes
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/changes-plugin*.jar

%files plugin-checkstyle
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/checkstyle-plugin*.jar

%files plugin-clean
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/clean-plugin*.jar

%files plugin-compiler
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/compiler-plugin*.jar

%files plugin-dependency
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/dependency-plugin*.jar

%files plugin-deploy
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/deploy-plugin*.jar

%files plugin-doap
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/doap-plugin*.jar

%files plugin-docck
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/docck-plugin*.jar

%files plugin-ear
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/ear-plugin*.jar

%files plugin-eclipse
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/eclipse-plugin*.jar

%files plugin-ejb
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/ejb-plugin*.jar

%files plugin-gpg
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/gpg-plugin*.jar

%files plugin-help
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/help-plugin*.jar

%files plugin-idea
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/idea-plugin*.jar

%files plugin-install
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/install-plugin*.jar

%files plugin-invoker
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/invoker-plugin*.jar

%files plugin-jar
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/jar-plugin*.jar

%files plugin-javadoc
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/javadoc-plugin*.jar

%files plugin-one
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/one-plugin*.jar

%files plugin-plugin
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/plugin-plugin*.jar

%files plugin-pmd
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/pmd-plugin*.jar

%files plugin-project-info-reports
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/project-info-reports-plugin*.jar

%files plugin-rar
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/rar-plugin*.jar

%files plugin-remote-resources
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/remote-resources-plugin*.jar

%files plugin-repository
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/repository-plugin*.jar

%files plugin-resources
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/resources-plugin*.jar

%files plugin-site
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/site-plugin*.jar

%files plugin-source
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/source-plugin*.jar

%files plugin-stage
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/stage-plugin*.jar

%files plugin-verifier
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/verifier-plugin*.jar

%files plugin-war
%defattr(-,root,root,-)
%dir %{_datadir}/%{name}/plugins
%{_datadir}/%{name}/plugins/war-plugin*.jar

%if %{with repolib}
%files repolib
%defattr(0644,root,root,0755)
%{_javadir}/repository.jboss.com
%endif

%changelog
* Fri Mar 12 2010 David Walluck <dwalluck@redhat.com> 0:2.0.8-26
- more merging with RHEL-4-EP-5 0:2.0.8-10.40

* Fri Mar 12 2010 David Walluck <dwalluck@redhat.com> 0:2.0.8-25
- update java source files from RHEL-4-EP-5 0:2.0.8-10.40

* Thu Mar 11 2010 David Walluck <dwalluck@redhat.com> 0:2.0.8-24
- merge some patches from RHEL-4-EP-5 0:2.0.8-10.40

* Wed Sep 02 2009 Ralph Apel <r.apel@r-apel.de> 0:2.0.8-23
- rebuild without_bootstrap

* Wed Sep 02 2009 Ralph Apel <r.apel@r-apel.de> 0:2.0.8-22
- try to relax maven-surefire requirements
- drop excessive BRs in bootstrap mode

* Thu Jun 11 2009 David Walluck <dwalluck@redhat.com> 0:2.0.8-21
- add repolib

* Fri May 22 2009 David Walluck <dwalluck@redhat.com> 0:2.0.8-20
- update maven-surefire BuildRequires

* Mon May 04 2009 Yong Yang <yyang@redhat.com> - 0:2.0.8-19
- Rebuild

* Tue Apr 21 2009 Yong Yang <yyang@redhat.com> - 0:2.0.8-18
- Build model-all.jar for model-v3 needed by maven-shared-model-converter, Merged from RHEL-4-EP-5 0:2.0.8-10.17

* Tue Apr 21 2009 Yong Yang <yyang@redhat.com> - 0:2.0.8-17
- rebuild in non-bootstrap mode with plexus-cdc alpha10

* Tue Apr 21 2009 Yong Yang <yyang@redhat.com> - 0:2.0.8-16
- rebuild in bootstrap mode with plexus-cdc alpha10

* Thu Apr 02 2009 Yong Yang <yyang@redhat.com> - 0:2.0.8-15
- fix jpp depmap issues of maven-shared-plugin-tools-api, maven-shared-plugin-tools-beanshell, maven-shared-plugin-tools-java
- cp maven-assembly-plugin/../components.xml manually to fix java.io.FileNotFoundException
- rebuild in non-bootstrap mode

* Thu Apr 02 2009 Yong Yang <yyang@redhat.com> - 0:2.0.8-14
- rebuild in bootstrap mode to fix PluginDescriptor issue

* Wed Apr 01 2009 Fernando Nasser <fnasser@redhat.com> - 0:2.0.8-13
- Build in bootstrap mode

* Mon Mar 23 2009 Yong Yang <yyang@redhat.com> - 0:2.0.8-12
- add maven2-plugins-jpprepolayout.patch

* Mon Mar 23 2009 Yong Yang <yyang@redhat.com> - 0:2.0.8-11
- rebuild in non-bootstrap mode

* Mon Mar 23 2009 Yong Yang <yyang@redhat.com> - 0:2.0.8-10
- remove Obsoletes: maven-surefire-plugin

* Tue Mar 16 2009 Yong Yang <yyang@redhat.com> - 0:2.0.8-9
- Merge from RHEL-4-EP-5, add missing BRs/Reqs, add patches

* Tue Mar 11 2009 Yong Yang <yyang@redhat.com> - 0:2.0.8-8
- Add missing Requires: maven-shared-plugin-tools-java, maven-shared-plugin-tools-beanshell for subpackage plugin-plugin

* Tue Mar 10 2009 Yong Yang <yyang@redhat.com> - 0:2.0.8-7
- Add Requires: tomcat5, excalibur-avalon-logkit, excalibur-avalon-framework

* Wed Mar 05 2009 Yong Yang <yyang@redhat.com> - 0:2.0.8-6
- Provides: maven2-bootstrap >= 2.0.7

* Wed Mar 05 2009 Yong Yang <yyang@redhat.com> - 0:2.0.8-5
- Add Obsoletes maven2-bootstrap <= 2.0.7, maven-release, maven-surefire-plugin

* Wed Mar 04 2009 Deepak Bhole <dbhole@redhat.com> - 0:2.0.8-4
- Add patch for commons-cli 1.1

* Fri Feb 20 2009 Yong Yang <yyang@redhat.com> 2.0.8-3
- add new maven-parent jpp depmap

* Wed Feb 18 2009 Yong Yang <yyang@redhat.com> 2.0.8-2
- Import from dbhloes maven2 2.0.8 list, Initializing build with bootstrap mode on JPP6
- Fix many BRs, jpp depmaps

* Tue Mar 20 2007 Deepak Bhole <dbhole@redhat.com> 0:2.0.4-10jpp.6
- Build without bootstrap

* Tue Mar 20 2007 Deepak Bhole <dbhole@redhat.com> 2.0.4-10jpp.5
- Force gcj_support to 0

* Tue Mar 20 2007 Deepak Bhole <dbhole@redhat.com> 2.0.4-10jpp.4
- Build without gcj for now

* Fri Mar 16 2007 Deepak Bhole <dbhole@redhat.com> 0:2.0.4-10jpp.3
- Added gcj support
- Fix up per Fedora spec
- Added source locations/generation methods for binary %%SOURCEes
- Added workaround for gcj bug that causes plugin reload to fail

* Wed Dec 13 2006 Deepak Bhole <dbhole@redhat.com> 2.0.4-10jpp.2
- Build without bootstrap

* Mon Dec 04 2006 Deepak Bhole <dbhole@redhat.com> 2.0.4-10jpp.1
- Synch with jpp
- From dbhole@redhat:
  - Added a new mapping system
  - Added a jpp howto
  - Added support for plugin mixing
  - Wired in /usr/share/maven2/repository as one of the default repos
  - Moved poms over to maven2-common-poms
  - Reverted to original plugin groupid's
  - Installer maven-{artifact-ant,embedder,meeper,script}
- From r.apel@r-apel.de:
  - Fix maven-site-plugin pom in maven2-jpp-mapping.patch
  - Add maven-shared-file-management to plugin-assembly Requires 
  - Add post/postun Requires for javadoc

* Wed Jul 12 2006 Fernando Nasser <fnasser@redhat.com> - 0:2.0.4-4jpp_1rh
- Merge with upstream

* Mon Jul 10 2006 Deepak Bhole <dbhole@redhat.com> - 0:2.0.4-4jpp
- Additional fixes (mostly to the dependency transformer xsl) for itests.
- Added a --with regereratedpoms switch.

* Wed Jul 05 2006 Deepak Bhole <dbhole@redhat.com> - 0:2.0.4-3jpp
- Added partial support for it tests, and appropriate fixes.

* Thu Jun 29 2006 Fernando Nasser <fnasser@redhat.com> - 0:2.0.4-2jpp_2rh
- Rebuild

* Tue Jun 27 2006 Fernando Nasser <fnasser@redhat.com> - 0:2.0.4-2jpp_1rh
- Full build

* Mon Jun 26 2006 Fernando Nasser <fnasser@redhat.com> - 0:2.0.4-2jpp_0rh
- Merge with upstream
- Bootstrap building

* Thu Jun 22 2006 Deepak Bhole <dbhole@redhat.com> - 0:2.0.4-2jpp
- Fixes for Tuscany building

* Fri Jun 02 2006 Deepak Bhole <dbhole@redhat.com> - 0:2.0.4-1jpp
- Upgrade to 2.0.4

* Wed May 31 2006 Fernando Nasser <fnasser@redhat.com> - 0:2.0.2-1jpp_1rh
- First Red Hat build

* Wed Feb 22 2006 Deepak Bhole <dbhole@redhat.com> - 0:2.0.2-1jpp
- Initial build.
# vim:foldmethod=marker
