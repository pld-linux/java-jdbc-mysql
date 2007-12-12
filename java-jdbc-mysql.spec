%include	/usr/lib/rpm/macros.java
Summary:	MySQL Connector/J - JDBC driver for MySQL
Summary(pl.UTF-8):	MySQL Connector/J - sterownik JDBC dla MySQL-a
Name:		mysql-connector-j
Version:	5.0.8
Release:	2
License:	GPL v2+ + MySQL FLOSS Exception
Group:		Libraries
Source0:	http://mysql.tonnikala.org/Downloads/Connector-J/%{name}ava-%{version}.tar.gz
# Source0-md5:	7a3caaa764fd6266bc312d8930972e8f
URL:		http://www.mysql.com/products/connector/j/
BuildRequires:	ant >= 1.5
BuildRequires:	jaxp_parser_impl
BuildRequires:	jpackage-utils
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	jpackage-utils
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

%description doc
Documentation for MySQL Connector/J.

%description doc -l pl.UTF-8
Dokumentacja dla MySQL Connector/J.

%prep
%setup -q -n %{name}ava-%{version}
rm docs/README

%build
required_jars="jaxp_parser_impl"
CLASSPATH=$(build-classpath $required_jars)
export CLASSPATH
%ant

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}

# jars
install build/mysql-connector-java-%{version}/mysql-connector-java-%{version}-bin.jar \
	$RPM_BUILD_ROOT%{_javadir}/mysql-connector-java-%{version}.jar
ln -s mysql-connector-java-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/mysql-connector-java.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES EXCEPTIONS-CONNECTOR-J README
%{_javadir}/*.jar

%files doc
%defattr(644,root,root,755)
%doc docs/*
