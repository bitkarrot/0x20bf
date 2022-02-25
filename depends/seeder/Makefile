LDFLAGS_SSL="-L/usr/local/opt/openssl@1.1/lib"
export LDFLAGS_SSL
CXXFLAGS_SSL="-I/usr/local/opt/openssl@1.1/include"
export CXXFLAGS
PKG_CONFIG_PATH="/usr/local/opt/openssl@1.1/lib/pkgconfig"
export PKG_CONFIG_PATH

CXXFLAGS = $(CXXFLAGS_SSL) -O3 -g0 -march=native
LDFLAGS =  $(LDFLAGS_SSL) $(CXXFLAGS)

dnsseed: dns.o bitcoin.o netbase.o protocol.o db.o main.o util.o
	g++ -pthread $(LDFLAGS) -o dnsseed dns.o bitcoin.o netbase.o protocol.o db.o main.o util.o -lcrypto

%.o: %.cpp *.h
	g++ -std=c++11 -pthread $(CXXFLAGS) -Wall -Wno-unused -Wno-sign-compare -Wno-reorder -Wno-comment -c -o $@ $<
