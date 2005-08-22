%bcond_without	bindist		# don't use binary distribution (not finished)
Summary:	MySQL Connector/J
Name:		mysql-connector-j
Version:	3.1.10
Release:	0.1
License:	GPL v2+ + MySQL FLOSS Exception
Group:		Libraries
Source0:	http://mysql.mirror.ok.ee/Downloads/Connector-J/%{name}ava-%{version}.tar.gz
# Source0-md5:	337f7f31e726fb615d3f4f062030d1b5
URL:		http://www.mysql.com/products/connector/j/
%{!?with_bindist:BuildRequires:  jakarta-ant >= 1.5}
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

%package doc
Summary:	Documentation for MySQL Connector/J
Group:		Documentation

%description doc
Documentation for MySQL Connector/J.

%prep
%setup -q -n mysql-connector-java-%{version}
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
