%global commit 9cda9268309160120fffee216280a9ca83ac4644

Name:		python-misaki
Version:	0.9.4
Release:	1
Summary:	Grapheme-to-phoneme engine for Kokoro
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/semidark/misaki
# semidark fork: German G2P and the later number and date fixes.
Source0:	https://github.com/semidark/misaki/archive/%{commit}.tar.gz#/misaki-%{commit}.tar.gz
Patch0:		python-misaki-distro.patch
BuildArch:	noarch
BuildSystem:	python
BuildRequires:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(wheel)

%description
misaki turns text into the phoneme alphabet Kokoro expects. This package
follows the semidark fork, which adds German. It calls the system
espeak-ng library through phonemizer instead of shipping a copy.

English pronunciation uses the bundled lexicon. When spaCy and
en_core_web_sm are installed, homographs also get part-of-speech tags.
Nothing is downloaded at build or run time.

Japanese, Mandarin, Korean, Vietnamese and Hebrew grapheme-to-phoneme
support is not included.

%files
%doc README.md EN_PHONES.md
%license LICENSE
%{py_sitedir}/misaki
%{py_sitedir}/misaki-*.dist-info
