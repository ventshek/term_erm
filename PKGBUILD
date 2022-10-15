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
makedepends=(git make python-build python-installer python-wheel)
#checkdepends=()
#optdepends=()
provides=(term_erm)
#conflicts=()
#replaces=()
#backup=()
#options=()
install="sh script.sh"
#changelog=
source=("git+$url")
#noextract=()
md5sums=('SKIP')
#validpgpkeys=()
_name=${pkgname#python-}
# prepare() {
#         cd "$pkgname-$pkgver"
#         patch -p1 -i "$srcdir/$pkgname-$pkgver.patch"
# }

build() {
    cd "$pkgname"
    python -m build --wheel --no-isolation
}

package() {
    cd "$pkgname"
    python -m installer --destdir="$pkgdir" dist/*.whl
}

        # cd /home/user/test/src/Grand-Unified-Bash-Catalogue/Terminal_Project
        # python -m nuitka --show-scons --show-progress --onefile --remove-output --warn-implicit-exceptions --warn-unusual-code --disable-console main.py
        # mv main.bin $pkgname-$pkgver
