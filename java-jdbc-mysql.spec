#
# Conditional build:
%bcond_without	bindist		# don't use binary distribution (not finished)
#
Summary:	MySQL Connector/J - JDBC driver for MySQL
Summary(pl):	MySQL Connector/J - sterownik JDBC dla MySQL-a
Name:		mysql-connector-j
Version:	3.1.13
Release:	0.1
License:	GPL v2+ + MySQL FLOSS Exception
Group:		Libraries
Source0:	http://mysql.tonnikala.org/Downloads/Connector-J/%{name}ava-%{version}.tar.gz
# Source0-md5:	b2fc8cc8990d85629b183f284a8f46d8
URL:		http://www.mysql.com/products/connector/j/
%{!?with_bindist:BuildRequires:	ant >= 1.5}
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

%description -l pl
MySQL Connector/J to natywny sterownik Javy konwertuj±cy wywo³ania
JDBC (Java Database Connectivity) na protokó³ sieciowy u¿ywany przez
bazê danych MySQL. Pozwala programistom pracowaæ z u¿yciem jêzyka
programowania Java ³atwo tworz±c programy i aplety wspó³pracuj±ce z
MySQL-em i ³±czyæ wszystkie zbiorcze dane, nawet w ¶rodowisku
heterogenicznym. MySQL Connector/J jest sterownikiem JDBC typu IV i ma
pe³ny zbiór mo¿liwo¶ci JDBC obs³uguj±cy MySQL-a.

MySQL Connector/J to oficjalny sterownik JDBC dla MySQL-a.

%package doc
Summary:	Documentation for MySQL Connector/J
Summary(pl):	Dokumentacja dla MySQL Connector/J
Group:		Documentation

%description doc
Documentation for MySQL Connector/J.

%description doc -l pl
Dokumentacja dla MySQL Connector/J.

%prep
%setup -q -n %{name}ava-%{version}
rm -f docs/README # duplicate

%build
%{!?with_bindist:ant}

%install
rm -rf $RPM_BUILD_ROOT

%if %{with bindist}
install -d $RPM_BUILD_ROOT%{_javadir}
install mysql-connector-java-%{version}-bin.jar $RPM_BUILD_ROOT%{_javadir}/mysql-connector-java-%{version}.jar
ln -s mysql-connector-java-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/mysql-connector-java.jar
%else
%{error:not finished}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES EXCEPTIONS-CONNECTOR-J README
%{_javadir}/*

%files doc
%defattr(644,root,root,755)
%doc docs/*
