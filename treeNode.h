#ifndef PUZZLES_TREENODE_H
#define PUZZLES_TREENODE_H
#include "eight_puzzle.h"


class treeNode {


private:
    eight_puzzle board;
    vector<eight_puzzle> children;
    vector<string> previousMoves;
    vector<string> possibleMoves;
    bool isRoot;

    vector<eight_puzzle> tree;

public:

    void solve() {

        int lowestMScoreIndex = indexOfLowestMScore();


        //while lowestMScoreIndex's hScore > 0
        //add it's children to tree
        //lowestMScoreIndex.isNotLeaf()
        //tree{lowestMScoreIndex].popBoard();
        //recalculate lowestMScoreIndex

        while(tree[lowestMScoreIndex].calcHScore() > 0) {
            //create children
            tree[lowestMScoreIndex].addBoard();
            vector<string> nextMoves = tree[lowestMScoreIndex].sortNextMoves(tree[lowestMScoreIndex].generateNextMoves());
            vector<eight_puzzle> nodeChildren = tree[lowestMScoreIndex].fillChildren(nextMoves);
            //add children to tree
            for(unsigned int i = 0; i < nodeChildren.size(); i++) {
                tree.push_back(nodeChildren[i]);
                if((tree.size() % 10000) == 0) {
                    cout << "NUMBER OF NODES: " << tree.size() << endl;
                }
            }
            //cout << "NUMBER OF NODES: " << tree.size() << endl;
            //tree.erase(tree.begin()+lowestMScoreIndex);
            tree[lowestMScoreIndex].isNotLeaf();
            //tree[lowestMScoreIndex].popBoard();
            lowestMScoreIndex = indexOfLowestMScore();


        }


        tree[lowestMScoreIndex].printPreviousBoards();
        cout << tree[lowestMScoreIndex].toString() << endl << endl;
        cout << "NUMBER OF NODES: " << tree.size() << endl << endl;
        cout << "Solved in " << tree[lowestMScoreIndex].getPreviousBoards().size() << " moves" << endl;
    }

    int indexOfLowestMScore() {
        int index = 0;
        while(!tree[index].isLeaf()) {
            index++;
        }
        int lowestMScore = tree[index].calcMScore();
        for(unsigned int i = 0; i < tree.size(); i++) {
            if(tree[i].isLeaf() && (tree[i].calcMScore() < lowestMScore)) {
                lowestMScore = tree[i].calcMScore();
                index = i;
            }
        }
        return index;
    }

    void addFirstNode() {
        tree.push_back(board);
    }
    void setBoard(vector<int> newBoard) {
        board.setBoard(newBoard);
    }


    bool fillTree() {
        if(board.isRepeat()) {
            cout << "DEAD END**************************************************************************" << endl << endl;
            return false;
        }
        if(board.calcHScore() == 0) {
            printPreviousBoards();
            cout << "SOLVED!" << endl;
            cout << board.toString() << endl;
            return true;
        }
        board.addBoard();
        fillChildren();
        //cout << printChildren();
        cout << "NODE" << endl;
        cout << board.toString() << endl << endl;
        cout << "CHILDREN" << endl;
        for(unsigned int i = 0; i < children.size(); i++) {
            cout << children.at(i).toString() << endl << endl;
        }
        for(unsigned int i = 0; i < children.size(); i++) {
            fillTree(children.at(i), children.at(i).getPreviousBoards());
        }
    }

    bool fillTree(eight_puzzle boardNode, vector<vector<int>> previousBoards) {
        boardNode.fillPreviousBoards(previousBoards);
        if(boardNode.isRepeat()) {
            cout << "DEAD END***********************************************************************" << endl << endl;
            return false;
        }
        if(boardNode.calcHScore() == 0) {
            printPreviousBoards();
            cout << "SOLVED!" << endl;
            cout << board.toString() << endl;
            return true;
        }
        boardNode.addBoard();
        fillChildren();
        //cout << printChildren();
        cout << "NODE" << endl;
        cout << board.toString() << endl << endl;
        cout << "CHILDREN" << endl;
        for(unsigned int i = 0; i < children.size(); i++) {
            cout << children.at(i).toString() << endl << endl;
        }
        for(unsigned int i = 0; i < children.size(); i++) {
            fillTree(children.at(i), children.at(i).getPreviousBoards());
        }
    }

    vector<eight_puzzle> fillChildren() {
        children.clear();
        //Generates a sorted list of nextMoves
        vector<string> nextMoves = sortNextMoves(board.generateNextMoves());
        //fills Children Vector in order
        for(unsigned int i = 0; i < nextMoves.size(); i++) {
            if(nextMoves.at(i) == "up") {
                eight_puzzle tempEightPuzzle;
                board.up();
                tempEightPuzzle.setBoard(board.getBoard());
                children.push_back(tempEightPuzzle);
                board.down();
            }
            if(nextMoves.at(i) == "down") {
                eight_puzzle tempEightPuzzle;
                board.down();
                tempEightPuzzle.setBoard(board.getBoard());
                children.push_back(tempEightPuzzle);
                board.up();
            }
            if(nextMoves.at(i) == "left") {
                eight_puzzle tempEightPuzzle;
                board.left();
                tempEightPuzzle.setBoard(board.getBoard());
                children.push_back(tempEightPuzzle);
                board.right();
            }
            if(nextMoves.at(i) == "right") {
                eight_puzzle tempEightPuzzle;
                board.right();
                tempEightPuzzle.setBoard(board.getBoard());
                children.push_back(tempEightPuzzle);
                board.left();
            }
        }
        return children;
    }
    
    vector<string> sortNextMoves(vector<string> nextMoves) {
        vector<int> mScores;
        for(unsigned int i = 0; i < nextMoves.size(); i++) {
            if(nextMoves.at(i) == "up") {
                board.up();
                mScores.push_back(board.calcHScore());
                board.down();
            }
            if(nextMoves.at(i) == "down") {
                board.down();
                mScores.push_back(board.calcHScore());
                board.up();
            }
            if(nextMoves.at(i) == "left") {
                board.left();
                mScores.push_back(board.calcHScore());
                board.right();
            }
            if(nextMoves.at(i) == "right") {
                board.right();
                mScores.push_back(board.calcHScore());
                board.left();
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

    void printPreviousBoards() {
        for(unsigned int i = 0; i < board.getPreviousBoards().size(); i++) {
            for(int j = 0; j < 9; j++) {
                cout << board.getPreviousBoards()[i][j] << " ";
                if((j ==2) || (j == 5)) {
                    cout << endl;
                }
            }
            cout << endl << endl;
        }
    }

    void scramble(int numMoves) {
        board.scramble(numMoves);
    }


    eight_puzzle getBoard() {
        return board;
    }

    string printChildren() {
        string childString = "Children layer";
        childString += to_string(board.getPreviousBoards().size());
        childString += "\n";
        for(unsigned int i = 0; i < children.size(); i++) {
            childString += children.at(i).toString();
            childString += "\n";
            childString += "\n";
        }
        return childString;
    }

};


#endif //PUZZLES_TREENODE_H
