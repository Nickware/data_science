NVCC = nvcc
NVCC_FLAGS = -O3 -std=c++17
SRC = main.cu kernel.cu metrics.cu init.cpp io.cpp
BIN = simulacion_particulas

$(BIN): $(SRC)
	$(NVCC) $(NVCC_FLAGS) $(SRC) -o $(BIN)

clean:
	rm -f $(BIN)
	rm -rf datos
