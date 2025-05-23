Summary:	Proxy Tunnel ssh-over-https hack
Summary(pl.UTF-8):	Tunel proxy ssh-po-https
Name:		proxytunnel
Version:	1.12.3
Release:	1
License:	GPL
Group:		Applications
Source0:	https://github.com/proxytunnel/proxytunnel/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c42ea5a2f0a12ec2a4b5ff9fb570eaa8
URL:		https://github.com/proxytunnel/proxytunnel
BuildRequires:	asciidoc
BuildRequires:	openssl-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ProxyTunnel is a program that connects stdin and stdout to a server
somewhere on the network, through a standard HTTPS proxy. We mostly
use it to tunnel SSH sessions through HTTP(S) proxies, allowing us to
do many things that wouldn't be possible without ProxyTunnel.
ProxyTunnel can currently do the following:
- Create tunnels using HTTP and HTTPS proxies (That understand the
  HTTP CONNECT command).
- Work as a back-end driver for an OpenSSH client, and create SSH
  connections through HTTP(S) proxies.
- Work as a stand-alone application, listening on a port for
  connections, and then tunneling these connections to a specified
  destination.

%description -l pl.UTF-8
ProxyTunnel to program łączący stdin i stdout do serwera gdzieś w
sieci poprzez standardowe proxy HTTPS. Jest używany głównie do
tunelowania sesji SSH poprzez proxy HTTP(S), co pozwala na robienie
wielu rzeczy, które nie byłyby możliwe bez niego. ProxyTunnel
aktualnie potrafi:
- tworzyć tunele przy użyciu proxy HTTP i HTTPS (rozumiejących
  polecenie HTTP CONNECT),
- działać jako sterownik backendu dla klienta OpenSSH i tworzyć
  połączenia SSH poprzez proxy HTTP(S),
- działać jako samodzielna aplikacja, nasłuchując na jakimś porcie na
  połączenia, a następnie tunelując te połączenia na podany adres.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags} `pkg-config --libs openssl`"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	prefix=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS CHANGES README.md
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
