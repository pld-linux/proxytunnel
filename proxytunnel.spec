Summary:	Proxy Tunnel ssh-over-https hack
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
Proxytunnel can currently do the following:
- Create tunnels using HTTP and HTTPS proxies (That understand the
  HTTP CONNECT command).
- Work as a back-end driver for an OpenSSH client, and create SSH
  connections through HTTP(S) proxies.
- Work as a stand-alone application, listening on a port for
  connections, and then tunneling these connections to a specified
  destination.

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
