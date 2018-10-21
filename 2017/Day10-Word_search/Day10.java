package summerofcode;

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
* Solution to task 10 of Summer of Code 2017
* author: Wojciech Czubak
* Copyright 2018
*/
public class Day10 {

    private static String filePath = "../10-wordsearch.txt";
    public final static String VOWELS = "aeiou";

    public static void main(String[] args) throws FileNotFoundException, IOException {
        Day10 wordSearch = new Day10();
        wordSearch.printAnswer();
    }

    public Day10() {

    }

    public void printAnswer() throws FileNotFoundException, IOException {
        Map<String, List<Letter>> easyAccessMap = new HashMap<>();
        Letter[][] wordSearchBoard;
        int totalLengthOfWords = 0;
        int numberOfVowels = 0;

        List<String> words = new ArrayList<>();

        // initialise word search board        
        try (BufferedReader bf = new BufferedReader(new FileReader(filePath))) {
            String line = bf.readLine();
            String[] boardSize = line.split("x");

            int row = 0;
            int col = 0;
            wordSearchBoard = new Letter[Integer.parseInt(boardSize[0])][Integer.parseInt(boardSize[1])];

            while (row < wordSearchBoard.length && (line = bf.readLine()) != null) {
                for (String l : line.split("")) {
                    Letter letter = new Letter(l, wordSearchBoard, row, col);
                    wordSearchBoard[row][col] = letter;
                    if (!easyAccessMap.containsKey(l)) {
                        easyAccessMap.put(l, new ArrayList<>());
                    }
                    easyAccessMap.get(l).add(letter);
                    col++;
                }
                row++;
                col = 0;
            }

            //searching words
            List<Letter> word = new ArrayList<>();
            boolean next;
            int easyAccessIndex = 0;
            int direction = 0;
            int cIndex = 0;
            String[] chars;
            Letter nextLetter = null;
            while ((line = bf.readLine()) != null) {
                line = line.trim();
                chars = line.split("");
                word.clear();
                next = true;
                cIndex = 1;
                easyAccessIndex = 0;
                while (next) {
                    if (word.isEmpty()) {
                        if (!easyAccessMap.containsKey(chars[0])) {
                            break;
                        }
                        word.add(easyAccessMap.get(chars[0]).get(easyAccessIndex));
                        nextLetter = word.get(0).getNextInDirection(direction);
                    }
                    if (nextLetter != null && nextLetter.letter.equals(chars[cIndex])) {
                        word.add(nextLetter);
                        nextLetter = nextLetter.getNextInDirection(direction);
                        cIndex++;
                    } else {
                        if (direction < 7) {
                            direction++;
                        } else {
                            direction = 0;
                            easyAccessIndex++;
                            next = easyAccessMap.get(chars[0]).size() > easyAccessIndex;
                        }
                        cIndex = 1;
                        word.clear();
                    }
                    if (word.size() == line.length()) {
                        totalLengthOfWords += line.length();
                        for (Letter l : word) {
                            l.isInWord = true;
                        }
                        cIndex = 1;
                        word.clear();
                        easyAccessIndex++;
                        next = easyAccessMap.get(chars[0]).size() > easyAccessIndex;
                    }
                }
            }
        }
        for (int r = 0; r < wordSearchBoard.length; r++) {
            for (int c = 0; c < wordSearchBoard[0].length; c++) {
                if (!wordSearchBoard[r][c].isInWord && wordSearchBoard[r][c].isVowel) {
                    numberOfVowels++;
                }
            }
        }
        System.out.println("Total length of words: " + totalLengthOfWords);
        System.out.println("Vowels left: " + numberOfVowels);

    }

    class Letter {

        String letter;
        Letter[][] board;
        boolean isVowel;
        boolean isInWord;
        private Map<Integer, int[]> nextInDirection;

        Letter(String letter, Letter[][] wordSearchBoard, int row, int column) {
            this.letter = letter;
            this.board = wordSearchBoard;
            isVowel = VOWELS.contains(letter);
            nextInDirection = new HashMap<>();
            nextInDirection.put(0, new int[]{row - 1, column}); // up
            nextInDirection.put(1, new int[]{row - 1, column + 1});//up-right
            nextInDirection.put(2, new int[]{row, column + 1}); //right
            nextInDirection.put(3, new int[]{row + 1, column + 1}); //right-down
            nextInDirection.put(4, new int[]{row + 1, column}); //down
            nextInDirection.put(5, new int[]{row + 1, column - 1}); //left-down
            nextInDirection.put(6, new int[]{row, column - 1}); //left
            nextInDirection.put(7, new int[]{row - 1, column - 1}); //left-up
        }

        public Letter getNextInDirection(int direction) {
            try {
                return board[nextInDirection.get(direction)[0]][nextInDirection.get(direction)[1]];
            } catch (IndexOutOfBoundsException ex) {
                return null;
            }
        }

        @Override
        public String toString() {
            return letter;
        }

    }
}
