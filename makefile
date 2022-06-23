test:
	python3 do_your_pilers_work.py

c:
	gcc test.c -o testC

cpp:
	g++ test.cpp -o testCpp

go:
	go build -o testGo test.go

java:
	javac test.java

javascript:
	node test.js

python:
	python3 test.py

rust:
	rustc test.rs -o testRust

typescript:
	tsc testts.ts
