# Maintainer: George Williams <ventshek@gmail.com>
pkgname=term_erm
pkgver=0.0.1
pkgrel=1
#epoch=
pkgdesc="Terminal and bash editor."
arch=(x86_64)
url="https://github.com/ventshek/term_erm.git"
license=('GPL')
#groups=()
depends=(python gtk3 vte3)
makedepends=(git make python-build python-installer python-wheel cython)
#checkdepends=()
#optdepends=()
provides=(term_erm)
#conflicts=()
#replaces=()
#backup=()
#options=()
install="script.sh"
#changelog=
source=("git+$url")
#noextract=()
md5sums=('SKIP')
#validpgpkeys=()
_name=${pkgname#python-}

build() {
    cd "$pkgname"
    python -m build --wheel --no-isolation
    cython main.py --embed
}

package() {
    cd "$pkgname"
    python -m installer --destdir="$pkgdir" dist/*.whl
    PYTHONLIBVER=python$(python3 -c 'import sys; print(".".join(map(str, sys.version_info[:2])))')$(python3-config --abiflags)
    gcc -Os $(python3-config --includes) main.c -o term_erm $(python3-config --ldflags) -l$PYTHONLIBVER
    cp "$src"/term_erm/term_erm /home/user
}