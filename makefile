default:
	make -s run

run:
	python3 do_your_pilers_work.py

gcc:
	gcc test.c -o testC

g++:
	g++ test.cpp -o testCpp

go:
	go build -o testGo test.go

javac:
	javac test.java

node:
	node test.js > /dev/null

python3:
	python3 test.py > /dev/null

rustc:
	rustc test.rs -o testRust

tsc:
	tsc testts.ts

lua:
	lua test.lua > /dev/null

ruby:
	ruby test.rb > /dev/null

clean:
	rm -v testC || true
	rm -v testCpp || true
	rm -v testGo || true
	rm -v test.class || true
	rm -v testRust || true
	rm -v testts.js || true

