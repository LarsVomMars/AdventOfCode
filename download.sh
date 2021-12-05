YEAR=$(date +%Y)
DAY=$(date +%d)
DIR_PATH=./$YEAR/$DAY/
if [ ! -d "$DIR_PATH" ]; then
mkdir -p $DIR_PATH
cd $DIR_PATH
aocd $YEAR $DAY > input
echo "LINES = [line.strip() for line in open(\"input\").readlines()]


def p1():
    pass


def p2():
    pass


print(\"1:\", p1())
print(\"2:\", p2())
" > main.py
fi
