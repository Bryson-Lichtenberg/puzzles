#ifndef PUZZLES_EIGHT_PUZZLE_H
#define PUZZLES_EIGHT_PUZZLE_H
#include <vector>
#include <string>
#include <iostream>
#include "time.h"
using namespace std;



class eight_puzzle {


private:
    //int board[9] = {0, 1, 2, 3, 4, 5, 6, 7, 8};
    vector<int> board = {0, 1, 2, 3, 4, 5, 6, 7, 8};
    int hScore = 0;
    string moves[4];
    vector<vector<int>> previousBoards;
    vector<eight_puzzle> children;
    //DO ALL THE RECURSION IN ONE LEVEL. DON'T PASS IN STUFF... CALL THE RECURSIVE FUNCTIONS ON THE CHILDREN

    bool leafNode = true;


public:
    eight_puzzle(){}
    ~eight_puzzle(){}

    eight_puzzle(vector<vector<int>> ancestors) {
        previousBoards = ancestors;
    }

    bool isLeaf() {
        return leafNode;
    }

    void isNotLeaf() {
        leafNode = false;
    }

    bool solve() {
        if(calcHScore() == 0) {
            printPreviousBoards();
            cout << toString() << endl;
            return true;
        }
        if(previousBoards.size() >= 50) {
            //cout << "TOO DEEP" << endl << endl;
            return false;
        }
        if(isRepeat()) {
            cout << "DEAD END" << endl << endl;
            return false;
        }
        addBoard();
        //Generate Sorted list of Moves
        vector<string> nextMoves = sortNextMoves(generateNextMoves());
        //Fill Children
        fillChildren(nextMoves);
        //cout << "Board Node at Depth " << (previousBoards.size() - 1) << endl;
       // cout << toString() << endl << endl;
       // cout << "CHILDREN" << endl;
//        for(unsigned int i = 0; i < children.size(); i++) {
//            cout << children[i].toString() << endl << "hScore " << calcHScore() << ": " << endl << endl;
//        }
        for(unsigned int i = 0; i < children.size(); i++) {
            children[i].solve();
        }
    }


    vector<eight_puzzle> fillChildren(vector<string> nextMoves) {
        //fills Children Vector in order
        for(unsigned int i = 0; i < nextMoves.size(); i++) {
            if(nextMoves.at(i) == "up") {
                eight_puzzle tempEightPuzzle(previousBoards);
                up();
                tempEightPuzzle.setBoard(board);
                children.push_back(tempEightPuzzle);
                down();
            }
            if(nextMoves.at(i) == "down") {
                eight_puzzle tempEightPuzzle(previousBoards);
                down();
                tempEightPuzzle.setBoard(board);
                children.push_back(tempEightPuzzle);
                up();
            }
            if(nextMoves.at(i) == "left") {
                eight_puzzle tempEightPuzzle(previousBoards);
                left();
                tempEightPuzzle.setBoard(board);
                children.push_back(tempEightPuzzle);
                right();
            }
            if(nextMoves.at(i) == "right") {
                eight_puzzle tempEightPuzzle(previousBoards);
                right();
                tempEightPuzzle.setBoard(board);
                children.push_back(tempEightPuzzle);
                left();
            }
        }
        return children;
    }



    string toString() {
        string print = "";
        for(int i = 0; i < 9; i++) {
            print += to_string(board[i]);
            print += " ";
            if((i == 2) || (i == 5)) {
                print += "\n";
            }
        }
        return print;
    }

    int calcHScore() {
        hScore = 0;
        for(int i = 1; i < 9; i++) {
            hScore += abs(floor(i / 3) - floor(board[i] / 3)) + abs(i % 3 - board[i] % 3);
        }
        return hScore;
    }

    unsigned int calcMScore() {
        return previousBoards.size() + calcHScore();
    }

    bool up() {
        int i = 0;
        while(board[i] != 0) {
            i++;
        }
        if((i + 3) > 8) {
            return false;
        }
        board[i] = board[i + 3];
        board[i + 3] = 0;
        return true;
    }
    bool down() {
        int i = 0;
        while(board[i] != 0) {
            i++;
        }
        if((i - 3) < 0) {
            return false;
        }
        board[i] = board[i - 3];
        board[i - 3] = 0;
        return true;
    }
    bool right() {
        int i = 0;
        while(board[i] != 0) {
            i++;
        }
        if((i % 3) == 0) {
            return false;
        }
        board[i] = board[i - 1];
        board[i - 1] = 0;
        return true;
    }
    bool left() {
        int i = 0;
        while(board[i] != 0) {
            i++;
        }
        if((i % 3) == 2) {
            return false;
        }
        board[i] = board[i + 1];
        board[i + 1] = 0;
        return true;
    }

    void scramble(int numMoves) {
        string lastMove = "";
        int i = 0;
        int numberOfPossibleMoves = 0;
        string thisMove = "";
        srand(time(NULL));



        for(int k = 0; k < numMoves; k++) {

            cout << toString() << endl << endl;

            //in the loop
            moves[0] = "";
            moves[1] = "";
            moves[2] = "";
            moves[3] = "";
            i = 0;
            while(board[i] != 0) {
                i++;
            }
            numberOfPossibleMoves = 0;
            //Up
            if(((i + 3) < 8) && lastMove != "down") {
                moves[numberOfPossibleMoves] = "up";
                numberOfPossibleMoves++;
            }
            //Down
            if(((i - 3) > 0) && lastMove != "up") {
                moves[numberOfPossibleMoves] = "down";
                numberOfPossibleMoves++;
            }
            //Right
            if(((i % 3) != 0) && lastMove != "left") {
                moves[numberOfPossibleMoves] = "right";
                numberOfPossibleMoves++;
            }
            //Left
            if(((i % 3) != 2) && lastMove != "right") {
                moves[numberOfPossibleMoves] = "left";
                numberOfPossibleMoves++;
            }

            thisMove = moves[rand() % numberOfPossibleMoves];

            if(thisMove == "up") {
                up();
            }
            else if(thisMove == "down") {
                down();
            }
            else if(thisMove == "right") {
                right();
            }
            else if(thisMove == "left") {
                left();
            }
            lastMove = thisMove;
        }
    }

    bool isRepeat() {
        int numMatch = 0;
        for(unsigned int i = 0; i < previousBoards.size(); i++) {
            numMatch = 0;
            for(int j = 0; j < 9; j++) {
                if(board[j] == previousBoards[i][j]) {
                    numMatch++;
                }
            }
            if(numMatch == 9) {
                return true;
            }
        }
        return false;
    }

    vector<vector<int>> getPreviousBoards() {
        return previousBoards;
    }

    void fillPreviousBoards(vector<vector<int>> ancestors) {
        vector<int> tempBoardVector;
        for(unsigned int i = 0; i < ancestors.size(); i++) {
            for(int j = 0; j < 9; j++) {
                tempBoardVector.push_back(ancestors[i][j]);
            }
            previousBoards.push_back(tempBoardVector);
        }
    }

    void setBoard(vector<int> newBoard) {
        for(int i = 0; i < 9; i++) {
            board[i] = newBoard[i];
        }
    }

    vector<int> getBoard() {
        vector<int> thisBoard;
        for(int i = 0; i < 9; i++) {
            thisBoard.push_back(board[i]);
        }
        return thisBoard;
    }



    vector<string> generateNextMoves() {
        vector<string> nextMoves;
        int i = 0;
        //Find 0
        while(board[i] != 0) {
            i++;
        }
        //Check / Add Up
        if((i + 3) < 8) {
            up();
            if(!isRepeat()) {
                nextMoves.push_back("up");
            }
            down();
        }
        //Down
        if((i - 3) > 0) {
            down();
            if(!isRepeat()) {
                nextMoves.push_back("down");
            }
            up();
        }
        //Right
        if((i % 3) != 0) {
            right();
            if(!isRepeat()) {
                nextMoves.push_back("right");
            }
            left();
        }
        //Left
        if((i % 3) != 2) {
            left();
            if(!isRepeat()) {
                nextMoves.push_back("left");
            }
            right();
        }
        return nextMoves;
    }

    vector<string> sortNextMoves(vector<string> nextMoves) {
        vector<int> mScores;
        for(unsigned int i = 0; i < nextMoves.size(); i++) {
            if(nextMoves.at(i) == "up") {
                up();
                mScores.push_back(calcHScore());
                down();
            }
            if(nextMoves.at(i) == "down") {
                down();
                mScores.push_back(calcHScore());
                up();
            }
            if(nextMoves.at(i) == "left") {
                left();
                mScores.push_back(calcHScore());
                right();
            }
            if(nextMoves.at(i) == "right") {
                right();
                mScores.push_back(calcHScore());
                left();
            }
        }
        int smallestMScore = 0;
        string tempMoveString = "";
        for(unsigned int i = 0; i < mScores.size(); i++) {
            smallestMScore = mScores.at(i);
            for(unsigned int j = i; j < mScores.size(); j++) {
                if(mScores.at(j) < smallestMScore) {
                    tempMoveString = nextMoves.at(j);
                    smallestMScore = mScores.at(j);

                    mScores.at(j) = mScores.at(i);
                    nextMoves.at(j) = nextMoves.at(i);

                    mScores.at(i) = smallestMScore;
                    nextMoves.at(i) = tempMoveString;
                }
            }
        }

        return nextMoves;
    }



    void addBoard() {
        vector<int> newBoard;
        for(int i = 0; i < 9; i++) {
            newBoard.push_back(board[i]);
        }
        previousBoards.push_back(newBoard);
    }
    void popBoard() {
        previousBoards.pop_back();
    }

    void straightSolve() {
        //string nextMove = "";
        int i = 0;
        int numberOfPossibleMoves = 0;
        int lastMScore = 0;
        string lastMove = "";
        vector<int> mScores;
        int lowestMScore = 0;
        int lowestMScoreIndex = 0;
        previousBoards.clear();
        //&& (calcHScore() < lastMScore)
        //while((calcHScore() > 0)) {
        for(int k = 0; k < 100; k++) {
            addBoard();
            cout << "NUMBER OF MOVES: " << previousBoards.size() << endl;
            lowestMScore = 0;
            mScores.clear();
            moves[0] = "";
            moves[1] = "";
            moves[2] = "";
            moves[3] = "";
            i = 0;
            while(board[i] != 0) {
                i++;
            }
            numberOfPossibleMoves = 0;
            //Up
            if(((i + 3) < 8) && lastMove != "down") {
                up();
                if(!isRepeat()) {
                    moves[numberOfPossibleMoves] = "up";
                    numberOfPossibleMoves++;
                    mScores.push_back(calcHScore());
                    cout << "Child " << numberOfPossibleMoves << " hScore: " << calcHScore() << endl;
                    cout << toString() << endl << endl;
                }
                else {cout << "isRepeat" << endl;}
                down();
            }
            //Down
            if(((i - 3) > 0) && lastMove != "up") {
                down();
                if(!isRepeat()) {
                    moves[numberOfPossibleMoves] = "down";
                    numberOfPossibleMoves++;
                    mScores.push_back(calcHScore());
                    cout << "Child " << numberOfPossibleMoves << " hScore: " << calcHScore() << endl;
                    cout << toString() << endl << endl;
                }
                else {cout << "isRepeat" << endl;}
                up();
            }
            //Right
            if(((i % 3) != 0) && lastMove != "left") {
                right();
                if(!isRepeat()) {
                    moves[numberOfPossibleMoves] = "right";
                    numberOfPossibleMoves++;
                    mScores.push_back(calcHScore());
                    cout << "Child " << numberOfPossibleMoves << " hScore: " << calcHScore() << endl;
                    cout << toString() << endl << endl;
                }
                else {cout << "isRepeat" << endl;}
                left();
            }
            //Left
            if(((i % 3) != 2) && lastMove != "right") {
                left();
                if(!isRepeat()) {
                    moves[numberOfPossibleMoves] = "left";
                    numberOfPossibleMoves++;
                    mScores.push_back(calcHScore());
                    cout << "Child " << numberOfPossibleMoves << " hScore: " << calcHScore() << endl;
                    cout << toString() << endl << endl;
                }
                else {cout << "isRepeat" << endl;}
                right();
            }
            if(mScores[0] != 0) {
                lowestMScore = mScores[0];
            }
            for(unsigned int j = 0; j < mScores.size(); j++) {
                if(mScores[j] <= lowestMScore) {
                    lowestMScore = mScores[j];
                    lowestMScoreIndex = j;
                }
            }
            if(moves[lowestMScoreIndex] == "up") {
                up();
                lastMove = "up";
            }
            if(moves[lowestMScoreIndex] == "down") {
                down();
                lastMove = "down";
            }
            if(moves[lowestMScoreIndex] == "right") {
                right();
                lastMove = "right";
            }
            if(moves[lowestMScoreIndex] == "left") {
                left();
                lastMove = "left";
            }
            lastMScore = lowestMScore;
            cout << endl << "NEXT STATE" << endl;
            cout << toString() << endl << endl;
            //printPreviousBoards();
        }

        cout << "Final State MScore: " << calcHScore() << endl;
        cout << toString() << endl;
    }

    void printPreviousBoards() {
        cout << "Previous Boards******************************************************************************" << endl;
        for(unsigned int i = 0; i < previousBoards.size(); i++) {
            for(int j = 0; j < 9; j++) {
                cout << previousBoards[i][j] << " ";
                if((j == 2) || (j == 5)) {
                    cout << endl;
                }
            }
            cout << endl << endl;
        }
    }





};


#endif //PUZZLES_EIGHT_PUZZLE_H
