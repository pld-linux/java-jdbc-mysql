# NOTE:
# - don't even try to compile it from source. It requires compiler from
#   java-sun = 1.5 AND rt.jar from java-sun-jre = 1.6
%include	/usr/lib/rpm/macros.java
Summary:	MySQL Connector/J - JDBC driver for MySQL
Summary(pl.UTF-8):	MySQL Connector/J - sterownik JDBC dla MySQL-a
Name:		java-jdbc-mysql
Version:	5.1.7
Release:	2
License:	GPL v2+ + MySQL FLOSS Exception
Group:		Libraries/Java
Source0:	http://sunsite.informatik.rwth-aachen.de/mysql/Downloads/Connector-J/mysql-connector-java-%{version}.tar.gz
# Source0-md5:	5150e0a6cc4b4487e1f9134659e466c2
URL:		http://www.mysql.com/products/connector/j/
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
Provides:	mysql-connector-j
Obsoletes:	mysql-connector-j
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MySQL Connector/J is a native Java driver that converts JDBC (Java
Database Connectivity) calls into the network protocol used by the
MySQL database. It lets developers working with the Java programming
language easily build programs and applets that interact with MySQL
and connect all corporate data, even in a heterogeneous environment.
MySQL Connector/J is a Type IV JDBC driver and has a complete JDBC
feature set that supports the capabilities of MySQL.

MySQL Connector/J is the official JDBC driver for MySQL.

%description -l pl.UTF-8
MySQL Connector/J to natywny sterownik Javy konwertujący wywołania
JDBC (Java Database Connectivity) na protokół sieciowy używany przez
bazę danych MySQL. Pozwala programistom pracować z użyciem języka
programowania Java łatwo tworząc programy i aplety współpracujące z
MySQL-em i łączyć wszystkie zbiorcze dane, nawet w środowisku
heterogenicznym. MySQL Connector/J jest sterownikiem JDBC typu IV i ma
pełny zbiór możliwości JDBC obsługujący MySQL-a.

MySQL Connector/J to oficjalny sterownik JDBC dla MySQL-a.

%package doc
Summary:	Documentation for MySQL Connector/J
Summary(pl.UTF-8):	Dokumentacja dla MySQL Connector/J
Group:		Documentation
Obsoletes:	mysql-connector-j

%description doc
Documentation for MySQL Connector/J.

%description doc -l pl.UTF-8
Dokumentacja dla MySQL Connector/J.

%prep
%setup -q -n mysql-connector-java-%{version}
rm docs/README

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
install mysql-connector-java-%{version}-bin.jar \
	$RPM_BUILD_ROOT%{_javadir}/mysql-connector-java-%{version}.jar
ln -s mysql-connector-java-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/mysql-connector-java.jar
ln -s mysql-connector-java-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/jdbc-mysql.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES EXCEPTIONS-CONNECTOR-J README
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs/*
