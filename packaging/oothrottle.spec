Name:           oothrottle
Version:        0.1.0
Release:        1%{?dist}
Summary:        Dynamically throttles background process groups when system load hits thresholds.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oothrottle
Source0:        oothrottle-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oothrottle is a sovereign, capability-bounded LOAD THROTTLER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oothrottle
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oothrottle-uninstall

%files
/usr/bin/oothrottle
/usr/bin/oothrottle-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
