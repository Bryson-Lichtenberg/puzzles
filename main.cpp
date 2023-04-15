#include "eight_puzzle.h"
#include "treeNode.h"
#include <iostream>



int main() {
    //eight_puzzle rootBoard;
    //rootBoard.scramble();
    //cout << rootBoard.toString() << endl << endl;
    //rootBoard.solve();

    string setOrScramble = "";
    treeNode tree;
    cout << "set, scramble, or preset" << endl;
    cin >> setOrScramble;
    if(setOrScramble == "set") {
        int tile = 0;
        vector<int> board;
        cout << "enter each number from top left to bottom right one at a time" << endl;
        for(int i = 0; i < 9; i++) {
            cin >> tile;
            board.push_back(tile);
        }
        tree.setBoard(board);
    }
    else if(setOrScramble == "scramble") {
        int numMoves = 0;
        cout << "enter number of moves" << endl;
        cin >> numMoves;
        tree.scramble(numMoves);
    }
    else if(setOrScramble == "preset") {
        vector<int> board = {3, 5, 7, 4, 8, 6, 1, 0, 2};
        tree.setBoard(board);
    }
    cout << "Start" << endl << tree.getBoard().toString() << endl << endl;
    tree.addFirstNode();
    tree.solve();



















/*
    while(eightPuzzle.calcHScore() != 0) {
        cout << "Enter Next Move (wsad)" << endl;
        cin >> move;
        if(move == 'w') {
            eightPuzzle.up();
        }
        else if(move == 's') {
            eightPuzzle.down();
        }
        else if(move == 'a') {
            eightPuzzle.left();
        }
        else if(move == 'd') {
            eightPuzzle.right();
        }
        cout << eightPuzzle.toString() << endl;
    }

*/
    //cout << endl << endl << "CONGRATION. YOU DONE IT" << endl;

    return 0;
}
