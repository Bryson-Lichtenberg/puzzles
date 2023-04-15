cmake_minimum_required(VERSION 3.20)
project(Puzzles)

set(CMAKE_CXX_STANDARD 14)

add_executable(Puzzles main.cpp eight_puzzle.cpp eight_puzzle.h treeNode.cpp treeNode.h)
