package hangman;

import java.io.File;
import java.util.Scanner;
import java.util.*;

public class EvilHangman {

    public static void main(String[] args) {
        int wordLength = Integer.parseInt(args[1]);
        int numGuesses = Integer.parseInt(args[2]);
        File inFile = new File(args[0]);
        EvilHangmanGame game = new EvilHangmanGame();
        try {
            game.startGame(inFile, wordLength);
        }
        catch(Exception e) {
            System.out.println(e);
        }
        Set<String> subSet = new HashSet<String>();
        boolean won = false;
        for(int i = 0; i < numGuesses; i++) {
            System.out.println("You have " + Integer.toString(numGuesses - i) + " guesses left");
            System.out.print("Used letters: ");
            for(Character c : game.getGuessedLetters()) {
                System.out.print(c);
                System.out.print(" ");
            }
            System.out.print("\n");
            System.out.print("Word: ");
            if(subSet.isEmpty()) {
                for(int j = 0; j < wordLength; j++) {
                    System.out.print("-");
                }
            }
            else {
                System.out.print(game.getCurrentKey());
            }
            System.out.print("\n");
            System.out.println("Enter guess: ");
            Scanner inChar = new Scanner(System.in);
            String guessString = inChar.nextLine();
            //Error handling for 0 chars, 2+ chars, or non-alphabet chars
            if(guessString.length() == 0) {
                System.out.println("You didn't enter a letter");
                i--;
                continue;
            }
            if(guessString.length() > 1) {
                System.out.println("You entered too many characters");
                i--;
                continue;
            }

            Character guessChar = guessString.toLowerCase().charAt(0);
            if(!Character.isLetter(guessChar)) {
                System.out.println("You didn't enter a letter");
                i--;
                continue;
            }
            try {
                subSet = game.makeGuess(guessChar);
            }
            catch (Exception e){
                i--;
                System.out.println(e);
            }
            StringBuilder temp = new StringBuilder(subSet.toArray()[0].toString());
            int correctGuess = 0;
            for(int j = 0; j < temp.length(); j++) {
                if(temp.charAt(j) == guessChar) {
                    correctGuess++;
                }
            }
            if(correctGuess > 0) {
                System.out.println("Yes, there is " + correctGuess + " " + guessChar);
                i--;
                if(!game.getCurrentKey().contains("" +'-')) {
                    System.out.println("You win! You guessed the word: " + game.getCurrentKey());
                    won = true;
                    break;
                }
            }
            else {
                System.out.println("Sorry, there are no " + guessChar + "'s");
            }

        }

        if(!won) {
            System.out.println("You lose!");
            System.out.println("The word was: " + subSet.toArray()[0]);
        }



    }

}
