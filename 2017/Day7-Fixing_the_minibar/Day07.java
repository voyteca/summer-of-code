package summerofcode;

import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
* Solution to task 7 of Summer of Code 2017
* author: Wojciech Czubak
* Copyright 2018
*/
public class Day07 {

    private static String filePath = "C:/bin/07-program.txt";

    public static void main(String[] args) throws IOException {
        int pc = 0;
        List<String> instructions = new ArrayList<>();
        Map<String, Integer> registers = new HashMap<>();
        registers.put("a", 937);
        registers.put("b", 0);
        registers.put("c", 0);
        registers.put("d", 0);

        try (BufferedReader bf=new BufferedReader(new FileReader(filePath))) {
            String line;
            while ((line=bf.readLine())!=null) {
                instructions.add(line);
            }
        }

        while (pc < instructions.size()) {
            String[] instruction = instructions.get(pc).split(" ");
            if (instruction[0].equals("inc")) {
                int i = registers.get(instruction[1]);
                registers.put(instruction[1], ++i);
                pc++;
            } else if (instruction[0].equals("dec")) {
                int i = registers.get(instruction[1]);
                registers.put(instruction[1], --i);
                pc++;
            } else if (instruction[0].equals("set")) {
                registers.put(instruction[1], Integer.parseInt(instruction[2]));
                pc++;
            } else if (instruction[0].equals("cpy")) {
                registers.put(instruction[2], registers.get(instruction[1]));
                pc++;
            } else if (instruction[0].equals("jmp")) {
                pc = pc + Integer.parseInt(instruction[1]);
            } else if (instruction[0].equals("jpz")) {
                if (registers.get(instruction[1]) == 0) {
                    pc = pc + Integer.parseInt(instruction[2]);
                } else {
                    pc++;
                }
            }
        }       
        System.out.println(registers.get("a"));
    }
}
