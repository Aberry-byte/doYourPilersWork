test:
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
	node test.js

python3:
	python3 test.py

rustc:
	rustc test.rs -o testRust

tsc:
	tsc testts.ts

lua:
	lua test.lua

ruby:
	ruby test.rb

clean:
	rm -v testC
	rm -v testCpp
	rm -v testGo
	rm -v test.class
	rm -v testRust
	rm -v testts.js

