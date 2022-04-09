//write a function: boolean[] solution(String[] plates) At Acme Insurance you are given a task to implement a function to check is a plate is valid. This is to make sure the consuming integration gets everything it needs to properly contact the DMV. THe DMV has a set of requirements which allows a valid plate. The function you implement will be used to check a valid plate. The function you implement will be used to check a valid plate before sending it to the DMV. The plate must be 6 digits long which can consist of alpha numeric digits.This is a legacy system and has issues with certain characters and digits. The system is unable to process "O" and "0"(zero) given the similarity between the 2. The DMV requires that there is a minimum of 2 numbers and that 2 characters/digits must not be duplicated next to one and other. When all these requirements are met the function should return which plates are valid and which are not
// you can also use imports, for example:
import java.util.*;
import java.util.Scanner;

// you can write to stdout for debugging purposes, e.g.
// System.out.println("this is a debug message");

class Solution {
    public static boolean solution(String[] plates){
        if (plates.length == 6){
            for(int i = 0; i < plates.length; i++){
                if(plates[i].matches("[0-9]{2}")){
                    for(int j = i+1; j < plates.length; j++){
                        if(plates[i] != plates[j]){
                            return true;
                        }
                    }
                }
            }
        }
        else {
            return false;
            }
              
    }
}

public class plates {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int n = scanner.nextInt();
        String[] plates = new String[n];
        for (int i = 0; i < n; i++) {
            plates[i] = scanner.next();
        }
        Solution solution = new Solution();
        solution.solution(plates);
    }
}