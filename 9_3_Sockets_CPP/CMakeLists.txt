cmake_minimum_required(VERSION 4.0)
project(9_3_Sockets_CPP)

set(CMAKE_CXX_STANDARD 20)

add_executable(9_3_Sockets_CPP
        main.cpp )

add_executable(client_socket_target client_socket.cpp)
