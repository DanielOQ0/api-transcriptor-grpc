python -m pip install grpcio
python -m pip install grpcio-tools

//Ubicarse en la carpeta protocode
python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/transmision.proto
python -m grpc_tools.protoc -I../protos --python_out=. --pyi_out=. --grpc_python_out=. ../protos/transcribir.proto
