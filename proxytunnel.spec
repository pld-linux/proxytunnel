Summary:	Proxy Tunnel ssh-over-https hack
Summary(pl):	Tunel proxy ssh-po-https
Name:		proxytunnel
Version:	1.5.0
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://proxytunnel.sourceforge.net/files/%{name}-%{version}.tgz
# Source0-md5:	2a36409580391e25421fc06e82eed4ce
URL:		http://proxytunnel.sourceforge.net/
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

%description -l pl
ProxyTunnel to program ³±cz±cy stdin i stdout do serwera gdzie¶ w
sieci poprzez standardowe proxy HTTPS. Jest u¿ywany g³ównie do
tunelowania sesji SSH poprzez proxy HTTP(S), co pozwala na robienie
wielu rzeczy, które nie by³yby mo¿liwe bez niego. ProxyTunnel
aktualnie potrafi:
- tworzyæ tunele przy u¿yciu proxy HTTP i HTTPS (rozumiej±cych
  polecenie HTTP CONNECT),
- dzia³aæ jako sterownik backendu dla klienta OpenSSH i tworzyæ
  po³±czenia SSH poprzez proxy HTTP(S),
- dzia³aæ jako samodzielna aplikacja, nas³uchuj±c na jakim¶ porcie na
  po³±czenia, a nastêpnie tuneluj±c te po³±czenia na podany adres.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT

install -D proxytunnel $RPM_BUILD_ROOT%{_bindir}/proxytunnel
install -D debian/proxytunnel.1 $RPM_BUILD_ROOT%{_mandir}/man1/proxytunnel.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS CHANGES README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
