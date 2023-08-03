dir="$(cd "$(dirname "$0")";pwd)"
cd "$dir"

sed 's/^#.*//g' resources/words.txt | sort -u > /tmp/words.ok.txt
sed 's/^#.*//g' resources/numbers.txt | sort -u > /tmp/numbers.ok.txt
sed 's/^#.*//g' resources/symbols.txt | sort -u > /tmp/symbols.ok.txt

python core.py /tmp/words.ok.txt /tmp/numbers.ok.txt /tmp/symbols.ok.txt | sort -u