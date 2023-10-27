

.PHONY: donut run clean

donut: donut.cpp
	g++ donut.cpp -o donut

run:
	./donut

clean:
	rm -r donut