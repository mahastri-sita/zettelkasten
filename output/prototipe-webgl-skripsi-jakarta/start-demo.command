#!/bin/zsh
set -e

DEMO_DIRECTORY="$(cd "$(dirname "$0")" && pwd)"
cd "$DEMO_DIRECTORY"

if ! command -v node >/dev/null 2>&1; then
  echo "Node.js belum tersedia. Instal Node.js, lalu buka berkas ini kembali."
  read -r "?Tekan Enter untuk menutup."
  exit 1
fi

if [[ ! -f "dist/index.html" ]]; then
  echo "Hasil demo belum tersedia; menyiapkan build lokal..."
  npm install --no-audit --no-fund
  npm run build
fi

node scripts/server.mjs

