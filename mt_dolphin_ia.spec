%define name mt_dolphin_ia
%define version 0.1.98
%define release %mkrel 9

Summary: The Maitretarot (stupid) IA
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: Games/Cards
Source: http://www.nongnu.org/download/maitretarot/%{name}.pkg/%{version}/%{name}-%{version}.tar.bz2
URL: https://www.nongnu.org/maitretarot/
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: glib2-devel libmaitretarot-devel
BuildRequires: libmt_client-devel
Provides: maitretarot_ia

%description
mt_dolphin_ia is a basic (and idiot) AI for the Maitretarot server.
Maitretarot and its various clients make a Tarot game

%description -l fr
mt_dolphin_ia est une IA basique (et plutôt bête) pour le serveur
Maitretarot. Maitretarot et ses differents clients constituent un 
jeu de tarot.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog
%{_bindir}/*


