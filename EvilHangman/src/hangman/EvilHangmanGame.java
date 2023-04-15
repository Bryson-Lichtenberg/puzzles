package hangman;

import java.io.File;
import java.io.IOException;
import java.util.*;

public class EvilHangmanGame implements IEvilHangmanGame{
  private Set<String> masterSet;
  private Set<String> largestSubSet;
  private Map<String, Set<String>> subSets;
  private SortedSet<Character> guessedLetters;

  public EvilHangmanGame() {
    this.masterSet= new HashSet<String>();
    this.subSets= new HashMap<String, Set<String>>();
    this.guessedLetters = new TreeSet<Character>();
    this.largestSubSet = new HashSet<String>();
  }

  public String getCurrentKey() {
    StringBuilder currentKey = new StringBuilder(largestSubSet.toArray()[0].toString());
    for(int i = 0; i < currentKey.length(); i++) {
      Character charAtI = '-';
      for(Character c : guessedLetters) {
        if(currentKey.charAt(i) == c) {
          charAtI = c;
        }
      }
      currentKey.setCharAt(i, charAtI);
    }
    return currentKey.toString();
  }

  @Override
  public void startGame(File dictionary, int wordLength) throws IOException, EmptyDictionaryException {
    masterSet.clear();
    subSets.clear();
    guessedLetters.clear();
    largestSubSet.clear();
    if(!dictionary.exists()) {
      throw new IOException();
    }

    Scanner inScanner = new Scanner(dictionary);

    while(inScanner.hasNext()) {
      String next = inScanner.next();
      if(next.length() == wordLength) {
        masterSet.add(next);
      }
    }
    if(masterSet.isEmpty()) {
      throw new EmptyDictionaryException();
    }
  }

  @Override
  public Set<String> makeGuess(char guess) throws GuessAlreadyMadeException {
    guess = Character.toLowerCase(guess);
    if(guessedLetters.contains(guess)) {
      throw new GuessAlreadyMadeException();
    }
    guessedLetters.add(guess);
    //Loop through all words in the master set generating the subsetKey for each word, then add the word to the Set<String> associated with the key in the map
    if(largestSubSet.isEmpty()) {
      for(String s : masterSet) {
        String subsetKey = getSubsetKey(s, guess);
        if(subSets.containsKey(subsetKey)) {
          subSets.get(subsetKey).add(s);
        }
        else {
          subSets.put(subsetKey, new HashSet<String>());
          subSets.get(subsetKey).add(s);
        }
      }
    }
    else {
      for(String s : largestSubSet) {
        String subsetKey = getSubsetKey(s, guess);
        if(subSets.containsKey(subsetKey)) {
          subSets.get(subsetKey).add(s);
        }
        else {
          subSets.put(subsetKey, new HashSet<String>());
          subSets.get(subsetKey).add(s);
        }
      }
    }

    //set largestSubSet to the largest set in the subSets maps
    int largestSubSetSize = 0;
    String largestSubSetKey = "";
    //Choose largest or tie-break
    for(Map.Entry<String, Set<String>> entry : subSets.entrySet()) {

      if(entry.getValue().size() == largestSubSetSize) {
        //Choose group where the letter doesn't appear in the key
        if(!largestSubSetKey.contains("" + guess)) {
          continue;
        }
        if(!entry.getKey().contains("" + guess)) {
          largestSubSetKey = entry.getKey();
          continue;
        }
        //Choose group with the fewest counts of the guessed letter
        int currCount = 0;
        int otherCount = 0;
        for(int j = 0; j < largestSubSetKey.length(); j++) {
          if(largestSubSetKey.charAt(j) == guess) {
            currCount++;
          }
          if(entry.getKey().charAt(j) == guess) {
            otherCount++;
          }
        }
        if(otherCount < currCount) {
          largestSubSetKey = entry.getKey();
          continue;
        }
        if(otherCount > currCount) {
          continue;
        }
        //Choose group with the right most letter
        //if both have same right most letter, choose next right most letter. repeat until a choice is made.
        for(int j = largestSubSetKey.length(); j > 0; j--) {
          if(largestSubSetKey.charAt(j - 1) == guess && entry.getKey().charAt(j - 1) != guess) {
            break;
          }
          if(largestSubSetKey.charAt(j - 1) != guess && entry.getKey().charAt(j - 1) == guess) {
            largestSubSetKey = entry.getKey();
            break;
          }
        }
      }
      if(entry.getValue().size() > largestSubSetSize) {
        largestSubSetSize= entry.getValue().size();
        largestSubSetKey = entry.getKey();
      }
    }
    //clear largestSubSet, fill with largestSubSet
    largestSubSet.clear();
    for(String s : subSets.get(largestSubSetKey)) {
      largestSubSet.add(s);
    }
    //clear the subSets map
    subSets.clear();

    return largestSubSet;
  }

  @Override
  public SortedSet<Character> getGuessedLetters() {
    return guessedLetters;
  }

  public String getSubsetKey(String word, Character guessedLetter) {
    StringBuilder subsetKey = new StringBuilder(word);
    for(int i = 0; i < word.length(); i++) {
      if(subsetKey.charAt(i) != guessedLetter) {
        subsetKey.setCharAt(i, '-');
      }
    }
    return subsetKey.toString();
  }
}
